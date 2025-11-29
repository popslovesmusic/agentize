import os
import json
from collections import defaultdict

# -------------------------------------------
# CONFIG
# -------------------------------------------
ROOT_DIR = r"D:\intake\cleaned\recovered_json_full"     # change if needed
OUTPUT_FILE = "library_inventory.json"

# -------------------------------------------
# METRIC STRUCTURES
# -------------------------------------------
inventory = []
stats = {
    "total_files": 0,
    "json_files": 0,
    "json5_files": 0,
    "directories": 0,
    "by_directory": defaultdict(int),
    "by_tier_detected": defaultdict(int),
    "sizes": []
}

# tier detection regex (Tier_XX or tier_XX)
import re
tier_pattern = re.compile(r"[Tt]ier[_-]?(\d+)")


# -------------------------------------------
# SCAN FUNCTION
# -------------------------------------------
for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    stats["directories"] += 1
    
    for filename in filenames:
        stats["total_files"] += 1
        
        full_path = os.path.join(dirpath, filename)
        rel_path = os.path.relpath(full_path, ROOT_DIR)
        file_ext = os.path.splitext(filename)[1].lower()

        # Check JSON vs JSON5
        if file_ext == ".json":
            stats["json_files"] += 1
        if file_ext == ".json5":
            stats["json5_files"] += 1

        # Directory-level metrics
        stats["by_directory"][dirpath] += 1

        # Tier detection
        match = tier_pattern.search(full_path)
        if match:
            tier_id = match.group(1)
            stats["by_tier_detected"][tier_id] += 1

        # File size
        try:
            size = os.path.getsize(full_path)
        except:
            size = None
        
        stats["sizes"].append(size)

        # Inventory append
        inventory.append({
            "path": rel_path,
            "directory": dirpath,
            "filename": filename,
            "extension": file_ext,
            "size_bytes": size
        })


# -------------------------------------------
# OUTPUT
# -------------------------------------------
output = {
    "root_directory": ROOT_DIR,
    "stats": stats,
    "inventory": inventory
}

with open(OUTPUT_FILE, "w") as f:
    json.dump(output, f, indent=2)

print(f"Inventory written to {OUTPUT_FILE}")
print("JSON:", stats["json_files"], " JSON5:", stats["json5_files"])
print("Total files:", stats["total_files"], " directories:", stats["directories"])
