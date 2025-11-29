import os
import sys
import pyjson5
from pathlib import Path
import logging

# --- CONFIGURATION ---
HARVESTER_FILE = Path('harvester_output.json')
OUTPUT_FILE = Path('Tier_Master_Rules.json5')
LOG_FILE = Path('builder.log')

# --- LOGGING SETUP ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

# --- MAIN LOGIC ---

def build_master_rules():
    print("Starting Phase 2: Building Master Rules File...", file=sys.stderr)

    # 1. Load the harvested data
    if not HARVESTER_FILE.exists():
        logging.error(f"Harvester output file not found: {HARVESTER_FILE}")
        print(f"ERROR: Harvester output file not found: {HARVESTER_FILE}", file=sys.stderr)
        return None

    with open(HARVESTER_FILE, 'r', encoding='utf-8') as f:
        harvested_data = pyjson5.load(f)

    # 2. Initialize the master rules structure
    master_rules = {
        "meta": {
            "version": "1.0-bootstrapped",
            "author": "IGSOA Librarian Agent",
            "description": "Master rules bootstrapped from existing library files.",
            "source_file": str(HARVESTER_FILE)
        },
        "defaults": {
            "description": "No description provided yet.",
            "invariants": [], "operators": [], "axioms": [],
            "rewrite_rules": [], "interactions": [], "modules": [], "tests": []
        },
        "tiers": []
    }

    # 3. Process tier information
    # Create a dictionary to hold tiers for easy lookup
    tiers_dict = {}
    for tier_info in harvested_data.get('tier_info', []):
        tier_id = tier_info.get('tier')
        if tier_id is None:
            continue
        
        tiers_dict[tier_id] = {
            "tier": tier_id,
            "family_symbol": tier_info.get('family_symbol', ''),
            "family_name": tier_info.get('family_name', ''),
            "description": tier_info.get('description', ''),
            "operators": [], "invariants": [], "axioms": [], "rewrite_rules": []
        }
    
    # 4. Distribute harvested components into the correct tiers
    for op in harvested_data.get('operators', []):
        tier_id = op.get('tier_id_source', 'N/A')
        if tier_id in tiers_dict:
            tiers_dict[tier_id]['operators'].append(op)
    
    for inv in harvested_data.get('invariants', []):
        # Invariants are just strings, so we can't easily assign them to tiers yet
        # For now, we can add them to a general pool or try to guess based on context later
        pass # Not enough info to sort into tiers yet

    for axiom in harvested_data.get('axioms', []):
         # Same problem as invariants
        pass

    for rule in harvested_data.get('rewrite_rules', []):
        tier_id = rule.get('tier_id_source', 'N/A')
        if tier_id in tiers_dict:
            tiers_dict[tier_id]['rewrite_rules'].append(rule)

    # 5. Finalize the tiers list from the dictionary
    master_rules['tiers'] = sorted(list(tiers_dict.values()), key=lambda x: x['tier'])

    # Add unsorted items to a top-level key for manual review
    master_rules['unclassified_invariants'] = harvested_data['invariants']
    master_rules['unclassified_axioms'] = harvested_data['axioms']


    # 6. Write the final master file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        pyjson5.dump(master_rules, f, indent=2, quote_keys=True)

    print(f"Phase 2 complete. Master rules file created at '{OUTPUT_FILE}'.", file=sys.stderr)
    return master_rules

if __name__ == "__main__":
    build_master_rules()
