import os
import json

# -------------------------------------------------------------
# CONFIG — SET THIS TO THE DIRECTORY YOU WANT TO VALIDATE
# -------------------------------------------------------------
SCAN_DIR = r"D:\intake\cleaned\recovered_json_full"   # <-- CHANGE THIS

# -------------------------------------------------------------
# OUTPUT FILES
# -------------------------------------------------------------
VALID_OUTPUT   = "valid_json_files.txt"
INVALID_OUTPUT = "invalid_json_files.txt"
ERROR_REPORT   = "invalid_json_report.txt"

valid_files = []
invalid_files = []
error_details = []

# -------------------------------------------------------------
# RECURSIVE VALIDATION LOOP
# -------------------------------------------------------------
for root, dirs, files in os.walk(SCAN_DIR):
    for fname in files:
        if fname.lower().endswith(".json"):
            fpath = os.path.join(root, fname)

            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    json.load(f)   # strict JSON parser

                valid_files.append(fpath)
                print(f"[VALID]   {fpath}")

            except Exception as e:
                invalid_files.append(fpath)
                msg = f"[INVALID] {fpath}\n         Error: {str(e)}\n"
                error_details.append(msg)
                print(msg)

# -------------------------------------------------------------
# WRITE REPORT FILES
# -------------------------------------------------------------
with open(VALID_OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(valid_files))

with open(INVALID_OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(invalid_files))

with open(ERROR_REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(error_details))

print("\n========================================")
print(f"VALID JSON FILES:   {len(valid_files)}")
print(f"INVALID JSON FILES: {len(invalid_files)}")
print(f"Full error report written to: {ERROR_REPORT}")
print("========================================")
