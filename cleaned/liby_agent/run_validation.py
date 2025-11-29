import os
import json5

# -------------------------------------------------------------
# CONFIGURATION — SET THIS TO THE FOLDER WITH YOUR JSON FILES
# -------------------------------------------------------------
SCAN_DIR = r"D:\intake\cleaned\recovered_json_full"   # <-- CHANGE THIS

# -------------------------------------------------------------
# OUTPUT REPORT FILES
# -------------------------------------------------------------
VALID_OUTPUT  = "valid_json5_files.txt"
INVALID_OUTPUT = "invalid_json5_files.txt"
INVALID_REPORT = "invalid_json5_report.txt"

valid_files = []
invalid_files = []
error_details = []

# -------------------------------------------------------------
# VALIDATION LOOP (Recursively scans folders)
# -------------------------------------------------------------
for root, dirs, files in os.walk(SCAN_DIR):
    for fname in files:
        if fname.lower().endswith((".json", ".json5")):
            fpath = os.path.join(root, fname)

            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    json5.load(f)   # try to parse using JSON5
                
                valid_files.append(fpath)
                print(f"[VALID]   {fpath}")

            except Exception as e:
                invalid_files.append(fpath)
                error_details.append(f"[ERROR] {fpath}\n       {str(e)}\n")
                print(f"[INVALID] {fpath}   -> {str(e)}")

# -------------------------------------------------------------
# WRITE OUTPUT LOGS
# -------------------------------------------------------------
with open(VALID_OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(valid_files))

with open(INVALID_OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(invalid_files))

with open(INVALID_REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(error_details))

print("\n----------------------------------------")
print(f"VALID JSON5 FILES:   {len(valid_files)}")
print(f"INVALID JSON5 FILES: {len(invalid_files)}")
print(f"Full report saved to: {INVALID_REPORT}")
print("----------------------------------------")
