import os
import re
import json
from pathlib import Path

INPUT_DIR = "D:\intake\cleaned"
OUTPUT_DIR = "recovered_json_full"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------
# 1. Capture ALL code blocks: json, json5, js, javascript,
#    yaml, none, empty fences, and unknown tags.
# ------------------------------------------------------
code_block_pattern = re.compile(
    r"```(?:json5?|js|javascript|yaml|text|none)?\s*(.*?)```",
    re.DOTALL | re.IGNORECASE
)

# ------------------------------------------------------
# 2. Capture inline JSON objects not in code blocks
#    (Looks for {...} with nested braces up to depth 3–4)
# ------------------------------------------------------
inline_json_pattern = re.compile(
    r"(\{(?:[^{}]|(?:\{[^{}]*\}))*\})",
    re.DOTALL
)

file_counter = 0

def save_json_block(block, source_name):
    global file_counter
    block = block.strip()

    # Skip tiny or non-json blocks
    if len(block) < 5:
        return

    # Naming
    base = source_name.replace(".", "_").replace(" ", "_")
    out_name = f"{base}_{file_counter}.json"
    file_counter += 1

    # Save raw content
    with open(os.path.join(OUTPUT_DIR, out_name), "w", encoding="utf-8") as f:
        f.write(block)

    print("Recovered:", out_name)


# ------------------------------------------------------
# PROCESS FILES
# ------------------------------------------------------
for root, dirs, files in os.walk(INPUT_DIR):
    for fname in files:
        if not fname.lower().endswith((".txt", ".md", ".log")):
            continue

        with open(os.path.join(root, fname), "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        # 1. CODE BLOCK JSON
        for match in code_block_pattern.findall(text):
            save_json_block(match, fname)

        # 2. INLINE JSON
        for match in inline_json_pattern.findall(text):
            # lightweight filtering: requires at least one colon
            if ":" in match:
                save_json_block(match, fname)

print(f"\nRecovered TOTAL: {file_counter} JSON/JSON5-like blocks.")
