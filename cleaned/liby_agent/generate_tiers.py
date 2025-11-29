import os
import pyjson5
from pathlib import Path
import sys

# --- CONFIGURATION ---
BASE_DIR = Path(__file__).parent
MASTER_FILE = BASE_DIR / "Tier_Master_Rules.json5"
OUTPUT_DIR = BASE_DIR / "generated_tiers"

# --- HELPER FUNCTIONS ---

def load_master_rules():
    """Loads the master JSON5 rules file."""
    if not MASTER_FILE.exists():
        print(f"FATAL: Master rules file not found at {MASTER_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(MASTER_FILE, "r", encoding="utf-8") as f:
        return pyjson5.load(f)

def merge_with_defaults(tier_cfg, defaults):
    """Merges a tier's configuration with the global defaults for missing keys."""
    merged = defaults.copy()
    merged.update(tier_cfg)
    return merged

def build_file_content(tier_data):
    """Builds the content for all 6 standard files for a given tier."""
    tier = tier_data.get("tier", "N/A")
    family_symbol = tier_data.get("family_symbol", "")
    family_name = tier_data.get("family_name", "")

    files = {
        "metadata": {
            "tier": tier,
            "family_symbol": family_symbol,
            "family_name": family_name,
            "description": tier_data.get("description"),
            "invariants": tier_data.get("invariants", [])
        },
        "operator_pack": {
            "tier": tier,
            "family_symbol": family_symbol,
            "operators": tier_data.get("operators", [])
        },
        "interaction_table": {
            "tier": tier,
            "family_symbol": family_symbol,
            "interactions": tier_data.get("interactions", [])
        },
        "axiom_box": {
            "tier": tier,
            "family_symbol": family_symbol,
            "axioms": tier_data.get("axioms", [])
        },
        "rewrite_system": {
            "tier": tier,
            "family_symbol": family_symbol,
            "rewrite_rules": tier_data.get("rewrite_rules", [])
        },
        "module_pack": {
            "tier": tier,
            "family_symbol": family_symbol,
            "modules": tier_data.get("modules", [])
        }
    }
    return files

def write_json5_file(output_path, data_obj):
    """Writes a dictionary to a JSON5 file with pretty printing."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        pyjson5.dump(data_obj, f, indent=2, quote_keys=True)

# --- MAIN EXECUTION ---

def main():
    print("Starting Phase 3: Library Autogeneration...", file=sys.stderr)
    
    rules_data = load_master_rules()
    defaults = rules_data.get("defaults", {})
    tiers_to_generate = rules_data.get("tiers", [])

    if not tiers_to_generate:
        print("Warning: No tiers found in the master rules file. Nothing to generate.", file=sys.stderr)
        return

    # Clean the output directory before generation
    if OUTPUT_DIR.exists():
        print(f"Cleaning existing output directory: {OUTPUT_DIR}", file=sys.stderr)
        for root, dirs, files in os.walk(OUTPUT_DIR, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name)) 
    
    OUTPUT_DIR.mkdir(exist_ok=True)

    generated_count = 0
    for tier_config in tiers_to_generate:
        full_tier_data = merge_with_defaults(tier_config, defaults)
        
        tier_files = build_file_content(full_tier_data)
        
        for file_key, content in tier_files.items():
            tier_id = full_tier_data['tier']
            file_name = f"tier_{tier_id}_{file_key}.json5"
            output_path = OUTPUT_DIR / file_name
            write_json5_file(output_path, content)
            generated_count += 1

    print(f"\nPhase 3 Complete. Successfully generated {generated_count} files in '{OUTPUT_DIR}'.", file=sys.stderr)

if __name__ == "__main__":
    main()
