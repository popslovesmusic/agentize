import os
import json
import shutil
import json5  # pip install json5
from typing import Any, Dict, List

# ==========================================================
# CONFIG
# ==========================================================
ROOT_DIR = r"D:\intake\cleaned"  # <-- SET THIS TO YOUR ROOT
VALID_JSON_DIR = os.path.join(ROOT_DIR, "valid_json")
VALID_JSON5_DIR = os.path.join(ROOT_DIR, "valid_json5")
LOG_FILE = os.path.join(ROOT_DIR, "validation_log.txt")


# ==========================================================
# IGSOA OPERATOR PACK SCHEMA HELPERS
# ==========================================================
def is_igsoa_operator_pack(data: Any) -> bool:
    """
    Heuristic: treat as IGSOA operator pack if:
      - top-level is an object
      - has 'meta' dict AND ( 'primitives' OR 'operator_pack' OR 'ψ_extensions' OR 'fusion' )
    """
    if not isinstance(data, dict):
        return False

    meta = data.get("meta")
    if not isinstance(meta, dict):
        return False

    keys = set(data.keys())
    if {"primitives"} & keys or {"operator_pack"} & keys or {"ψ_extensions"} & keys or {"fusion"} & keys:
        return True

    # Additional heuristic: name hint
    name = str(meta.get("name", "")).lower()
    if "operator pack" in name or "operator" in name:
        return True

    return False


def validate_igsoa_operator_pack(data: Dict[str, Any]) -> List[str]:
    """
    Minimal schema check for IGSOA operator packs.
    Returns a list of schema error strings (empty if OK).
    """
    errors: List[str] = []

    # meta
    meta = data.get("meta")
    if not isinstance(meta, dict):
        errors.append("meta must be an object.")
    else:
        if "name" not in meta:
            errors.append("meta.name is missing.")
        if "version" not in meta:
            errors.append("meta.version is missing.")

    # primitives: each entry should have symbol + desc
    primitives = data.get("primitives")
    if primitives is not None:
        if not isinstance(primitives, dict):
            errors.append("primitives must be an object.")
        else:
            for key, val in primitives.items():
                if not isinstance(val, dict):
                    errors.append(f"primitives.{key} must be an object.")
                    continue
                if "symbol" not in val or "desc" not in val:
                    errors.append(f"primitives.{key} should have 'symbol' and 'desc' fields.")

    # normal_form: list of rules with pattern + reduce_to
    normal_form = data.get("normal_form")
    if normal_form is not None:
        if not isinstance(normal_form, list):
            errors.append("normal_form must be a list.")
        else:
            for i, rule in enumerate(normal_form):
                if not isinstance(rule, dict):
                    errors.append(f"normal_form[{i}] must be an object.")
                    continue
                if "pattern" not in rule:
                    errors.append(f"normal_form[{i}].pattern is missing.")
                if "reduce_to" not in rule:
                    errors.append(f"normal_form[{i}].reduce_to is missing.")

    return errors


# ==========================================================
# FS HELPERS
# ==========================================================
def ensure_parent_dir(path: str) -> None:
    parent = os.path.dirname(path)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)


def move_file(src: str, dest_root: str, rel_path: str, new_extension: str = None) -> str:
    """
    Move file preserving relative path under dest_root.
    Optionally change the extension (for auto JSON→JSON5 repair).
    Returns the destination path.
    """
    rel_dir, filename = os.path.split(rel_path)
    base, ext = os.path.splitext(filename)

    if new_extension is not None:
        filename = base + new_extension

    dest_path = os.path.join(dest_root, rel_dir, filename)
    ensure_parent_dir(dest_path)
    shutil.move(src, dest_path)
    return dest_path


# ==========================================================
# MAIN
# ==========================================================
def main():
    os.makedirs(VALID_JSON_DIR, exist_ok=True)
    os.makedirs(VALID_JSON5_DIR, exist_ok=True)

    valid_json_count = 0
    valid_json5_count = 0
    invalid_count = 0
    igsoa_checked = 0
    igsoa_schema_errors_total = 0

    with open(LOG_FILE, "w", encoding="utf-8") as log:
        log.write("IGSOA JSON / JSON5 Validation Log\n")
        log.write(f"ROOT_DIR = {ROOT_DIR}\n\n")

        for root, dirs, files in os.walk(ROOT_DIR):
            # Skip our own output dirs to avoid infinite moving
            dirs[:] = [
                d for d in dirs
                if os.path.join(root, d) not in (VALID_JSON_DIR, VALID_JSON5_DIR)
                and d not in ("valid_json", "valid_json5")
            ]

            for filename in files:
                full_path = os.path.join(root, filename)
                # Skip the log itself
                if os.path.abspath(full_path) == os.path.abspath(LOG_FILE):
                    continue

                # If file is already inside output dirs, skip
                if full_path.startswith(os.path.abspath(VALID_JSON_DIR)) or full_path.startswith(
                    os.path.abspath(VALID_JSON5_DIR)
                ):
                    continue

                rel_path = os.path.relpath(full_path, ROOT_DIR)

                # Read file
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        text = f.read()
                except Exception as e:
                    invalid_count += 1
                    log.write(f"[IO_ERROR] {rel_path} | error={type(e).__name__}: {e}\n")
                    continue

                json_error = None
                json5_error = None
                parsed_data = None
                parsed_kind = None  # "json" or "json5"

                # Try strict JSON
                try:
                    parsed_data = json.loads(text)
                    parsed_kind = "json"
                except Exception as e:
                    json_error = f"{type(e).__name__}: {e}"

                    # Try JSON5
                    try:
                        parsed_data = json5.loads(text)
                        parsed_kind = "json5"
                    except Exception as e2:
                        json5_error = f"{type(e2).__name__}: {e2}"

                # Classification
                if parsed_kind is None:
                    # Completely invalid (neither JSON nor JSON5)
                    invalid_count += 1
                    log.write(
                        f"[INVALID] {rel_path} | json_error={json_error} | json5_error={json5_error}\n"
                    )
                    continue

                # Optional: IGSOA operator pack schema validation
                schema_errors: List[str] = []
                if is_igsoa_operator_pack(parsed_data):
                    igsoa_checked += 1
                    schema_errors = validate_igsoa_operator_pack(parsed_data)
                    igsoa_schema_errors_total += len(schema_errors)

                # === VALID JSON ===
                if parsed_kind == "json":
                    dest_path = move_file(full_path, VALID_JSON_DIR, rel_path)
                    valid_json_count += 1

                    if schema_errors:
                        log.write(
                            f"[VALID_JSON][IGSOA_SCHEMA_ERRORS] {rel_path} -> {os.path.relpath(dest_path, ROOT_DIR)}\n"
                        )
                        for err in schema_errors:
                            log.write(f"    - {err}\n")
                    else:
                        log.write(
                            f"[VALID_JSON] {rel_path} -> {os.path.relpath(dest_path, ROOT_DIR)}\n"
                        )

                # === VALID JSON5 (auto-repaired JSON→JSON5 naming) ===
                else:  # parsed_kind == "json5"
                    # Auto "repair" JSON-ish to JSON5 by ensuring extension is .json5
                    dest_path = move_file(full_path, VALID_JSON5_DIR, rel_path, new_extension=".json5")
                    valid_json5_count += 1

                    # Distinguish files that were ONLY JSON5-valid
                    if json_error is not None:
                        status = "[VALID_JSON5][JSON5_PARSE_ONLY][AUTO_RENAMED_TO_.json5]"
                    else:
                        status = "[VALID_JSON5]"

                    if schema_errors:
                        log.write(
                            f"{status}[IGSOA_SCHEMA_ERRORS] {rel_path} -> {os.path.relpath(dest_path, ROOT_DIR)}\n"
                        )
                        for err in schema_errors:
                            log.write(f"    - {err}\n")
                    else:
                        log.write(
                            f"{status} {rel_path} -> {os.path.relpath(dest_path, ROOT_DIR)}\n"
                        )

        # Summary
        log.write("\n=== SUMMARY ===\n")
        log.write(f"Valid JSON   : {valid_json_count}\n")
        log.write(f"Valid JSON5  : {valid_json5_count}\n")
        log.write(f"Invalid      : {invalid_count}\n")
        log.write(f"IGSOA packs checked      : {igsoa_checked}\n")
        log.write(f"IGSOA schema errors total: {igsoa_schema_errors_total}\n")

    print("✔ Recursive separation complete.")
    print(f"Valid JSON   : {valid_json_count}")
    print(f"Valid JSON5  : {valid_json5_count}")
    print(f"Invalid left : {invalid_count}")
    print(f"Log file     : {LOG_FILE}")
    print(f"JSON dir     : {VALID_JSON_DIR}")
    print(f"JSON5 dir    : {VALID_JSON5_DIR}")


if __name__ == "__main__":
    main()
