import os
import re
import sys
import pyjson5
from pathlib import Path
import logging

# --- CONFIGURATION ---
ROOT_DIR = Path('.')
OUTPUT_FILE = Path('harvester_output.json')
LOG_FILE = Path('harvester.log')
FILE_EXTENSIONS = ('.json', '.json5', '.md', '.txt')

# --- LOGGING SETUP ---
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')

# --- REGEX PATTERNS v5 ---
# Flexible patterns to find keys that may or may not be quoted.
def create_flexible_pattern(key):
    return re.compile(fr"""
        (?:'|"|"|\s)*{key}(?:'|"|"|\s)*\s*:\s* # Match the key, with optional quotes and whitespace
        (                                  # Start capturing group for the value
            \[[\s\S]*?\]|                  # Capture a list
            \{{[\s\S]*?\}}
        ) # Capture an object
    """, re.DOTALL | re.IGNORECASE | re.VERBOSE)

PATTERNS = {
    "operators": create_flexible_pattern("operators"),
    "invariants": create_flexible_pattern("invariants"),
    "axioms": create_flexible_pattern("axioms"),
    "rewrite_rules": create_flexible_pattern("rewrite_rules"),
    "tier_info": create_flexible_pattern("tiers") 
}

# --- DATA STORE ---
harvested_data = {
    "operators": [], "invariants": [], "axioms": [], 
    "rewrite_rules": [], "tier_info": []
}

# --- HELPER FUNCTIONS ---

def get_tier_from_path(path_str):
    match = re.search(r'tier[-_]?([0-9]{1,2})|t([0-9]{1,2})', str(path_str), re.IGNORECASE)
    if match:
        return next((g for g in match.groups() if g is not None), "N/A")
    return "N/A"

def process_json_object(obj, tier_id, key):
    """Assigns data to the correct key in the harvested_data dictionary."""
    if not obj:
        return
        
    if isinstance(obj, list):
        # If we get a list of tier info dicts, process them
        if key == 'tier_info':
            for item in obj:
                if isinstance(item, dict):
                    item.setdefault('tier_id_source', tier_id)
                    harvested_data['tier_info'].append(item)
        else:
            harvested_data[key].extend(obj)
    elif isinstance(obj, dict):
        obj.setdefault('tier_id_source', tier_id)
        harvested_data[key].append(obj)


def harvest_from_content(content, file_path):
    tier_id = get_tier_from_path(file_path)
    
    for key, pattern in PATTERNS.items():
        for match_str in pattern.findall(content):
            try:
                # The regex captures the value (list or object string).
                # pyjson5 is robust enough to parse these strings directly.
                data = pyjson5.loads(match_str)
                process_json_object(data, tier_id, key)

            except (ValueError, TypeError) as e:
                logging.warning(f"Failed to parse block for key '{key}' from {file_path}: {e}\n--- Block Content ---\n{match_str[:200]}\n--------------------")
                continue

# --- MAIN EXECUTION ---

def main():
    print("Starting Phase 1: Harvesting semantic components (v5)...", file=sys.stderr)
    
    all_files = [p for p in ROOT_DIR.rglob('*') if p.suffix.lower() in FILE_EXTENSIONS]
    total_files = len(all_files)
    
    for i, file_path in enumerate(all_files):
        if file_path.name in (OUTPUT_FILE.name, LOG_FILE.name): continue

        sys.stderr.write(f"\rProcessing file {i+1}/{total_files}: {str(file_path)[:80]}...")
        sys.stderr.flush()
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            harvest_from_content(content, file_path)
        except Exception as e:
            logging.error(f"FATAL: Could not process file {file_path}: {e}")
            continue
            
    print("\nHarvesting complete. De-duplicating results...", file=sys.stderr)

    # De-duplicate results
    harvested_data['invariants'] = sorted(list(set(s for s in harvested_data['invariants'] if isinstance(s, str))))
    harvested_data['axioms'] = sorted(list(set(s for s in harvested_data['axioms'] if isinstance(s, str))))
    
    def dedupe_list_of_dicts(lod):
        return [pyjson5.loads(s) for s in set(pyjson5.dumps(d, sort_keys=True) for d in lod if isinstance(d, dict))]

    harvested_data['operators'] = dedupe_list_of_dicts(harvested_data['operators'])
    harvested_data['rewrite_rules'] = dedupe_list_of_dicts(harvested_data['rewrite_rules'])
    harvested_data['tier_info'] = dedupe_list_of_dicts(harvested_data['tier_info'])

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        pyjson5.dump(harvested_data, f, indent=2, quote_keys=True)

    print(f"\nPhase 1 complete. All unique components saved to '{OUTPUT_FILE}'. See '{LOG_FILE}' for details.", file=sys.stderr)
    summary = (f"Found:\n"
               f"- {len(harvested_data['operators'])} unique operators\n"
               f"- {len(harvested_data['invariants'])} unique invariants\n"
               f"- {len(harvested_data['axioms'])} unique axioms\n"
               f"- {len(harvested_data['rewrite_rules'])} unique rewrite rules\n"
               f"- {len(harvested_data['tier_info'])} unique tier definitions")
    print(summary, file=sys.stdout)
    logging.info(summary)

if __name__ == "__main__":
    main()