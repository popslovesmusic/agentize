# MBC Framework v4.0 - Pointer System

**Version:** 4.0
**Created:** 2025-11-27
**Type:** Reference/Pointer System
**Source Directory:** `../` (parent directory with markdown files)

---

## Overview

This directory structure follows the canonical MBC-4.0 architecture defined in `mbc json tree.txt`.

**Important:** This is a **pointer system**, not a duplicate of content. Each JSON file contains:
- Reference to source markdown file
- Line number ranges where content exists
- Extraction metadata
- Content type classification

**Benefits:**
- ✅ Minimal storage overhead (pointers are ~1-2KB vs 100KB+ content)
- ✅ Source files remain intact and authoritative
- ✅ Easy navigation via standard MBC structure
- ✅ Traceable back to original context
- ✅ Can regenerate extracted JSON on demand

---

## Directory Structure

```
MBC_Framework_v4/
├── README.md (this file)
├── mbc_framework_index.json         # Master index of all pointers
├── 00_Meta/                          # Framework metadata & principles
├── 01_Primitives/                    # Tier-0 primitive operators
├── 02_Tiers/                         # Tiers 1-12 (operator families)
├── 03_MetaOperators/                 # Commutators, tensor products, etc.
├── 04_InteractionTables/             # Cross-operator interaction tables
├── 05_RewriteSystems/                # Normal forms and rewrite rules
├── 06_AxiomBoxes/                    # Sealed axiom boxes per operator
├── 07_Diagrams/                      # Commutative squares, cubes, hypercubes
├── 08_ModulePacks/                   # Integrated layer packs
├── 09_CrossLinks/                    # Inter-component mappings
└── 10_Validation/                    # Schema definitions, consistency checks
```

---

## Pointer File Format

Each `.pointer.json` file follows this schema:

```json
{
  "pointer_version": "1.0",
  "type": "content_pointer",
  "target": {
    "source_file": "../Tier-0 Primitive Operators.md",
    "line_range": [64, 67],
    "section": "δ Operator Definition",
    "content_type": "operator_definition"
  },
  "metadata": {
    "operator": "δ",
    "tier": 0,
    "family": "deviation",
    "completeness": "full",
    "last_verified": "2025-11-27"
  },
  "extraction": {
    "method": "automated",
    "confidence": "high",
    "notes": "JSON block extracted from markdown code fence"
  },
  "cross_references": [
    "01_Primitives/tier0_operators.pointer.json",
    "02_Tiers/Tier_01_delta/tier_01_delta_operator_pack.pointer.json"
  ]
}
```

---

## How to Use This System

### 1. **Navigate by Concept**
Browse the directory structure to find what you need (e.g., `02_Tiers/Tier_04_mu/`)

### 2. **Read the Pointer**
Open the `.pointer.json` file to see where content lives in source files

### 3. **Extract on Demand**
Use the line ranges to extract actual JSON/content when needed

### 4. **Follow Cross-References**
Pointers include references to related content in other parts of the framework

---

## Master Index

See `mbc_framework_index.json` for:
- Complete inventory of all pointers
- Source file coverage map
- Completeness statistics
- Extraction status per component

---

## Source File Mapping

| Source Markdown File | Content Coverage |
|---------------------|------------------|
| Tier-0 Primitive Operators.md | 100% - All primitives |
| Tier-1 δ-Family — Concise Definitions.md | δ-Family operators, Tri-Unity tables |
| Tier-3 — Π-Family.md | Π-Family operators |
| Tier-4 — μ-Family.md | μ-Family operators, Tri-Unity+μ |
| Tier-5 — λ-Family.md | λ-Family (concise) |
| λ — Curvature & Mode-Deformation Operator.md | λ-Family (extended) |
| THE SEMANTIC WAVE EQUATION.md | ψ-Family, Semantic Wave Equation |
| Tier 7 — Σ-Family.md | Σ-Family operators |
| Tier 8 — Θ-Family.md | Θ-Family operators |
| Tier 9 — χ-Family.md | χ-Family operators |
| Ten Textbook Chapter Titles for the Ω-Family.md | Ω-Family (complete) |
| Tier-11 — ρ-Family.md | ρ-Family operators |
| Tier-12 — Ξ-Family.md | Ξ-Family operators |
| A fully diagrammatic commutative square.md | All diagram schemas |
| μ — Local Measure _ Micro-Adjacency.md | μ extended treatment |
| Σ — Semantic Summation _ Contraction Rules.md | Σ extended treatment |
| δ — Full Deviation Operator Family.md | δ extended treatment |

---

## Completeness Status

Based on gap analysis (see `../reports/MBC_Framework_Gap_Analysis.md`):

- **00_Meta:** 25% complete
- **01_Primitives:** 100% complete ✅
- **02_Tiers:** 45% average (varies by tier)
- **03_MetaOperators:** 0% (needs creation)
- **04_InteractionTables:** 60% complete
- **05_RewriteSystems:** 0% (mentioned in text, needs formalization)
- **06_AxiomBoxes:** 42% complete
- **07_Diagrams:** 78% complete
- **08_ModulePacks:** 38% complete
- **09_CrossLinks:** 0% (needs generation)
- **10_Validation:** 0% (needs generation)

**Overall: ~42% of ideal structure has source content**

---

## Maintenance

### Updating Pointers
When source files change:
1. Update `line_range` in affected pointers
2. Update `last_verified` timestamp
3. Regenerate `mbc_framework_index.json`

### Adding New Content
When new JSON is found in source files:
1. Create new `.pointer.json` in appropriate directory
2. Add entry to `mbc_framework_index.json`
3. Update cross-references

### Extracting Content
To generate actual JSON files from pointers:
```bash
# Script would read pointer, extract lines from source, write to .json
./extract_from_pointers.sh 01_Primitives/delta_primitive.pointer.json
```

---

## Related Documentation

- `../reports/Textbook_Organization_Analysis_CORRECTED.md` - Full textbook organization
- `../reports/MBC_Framework_Gap_Analysis.md` - Detailed gap analysis
- `../reports/Consolidated_JSON_Index.md` - All extracted JSON (125+ blocks)
- `../mbc json tree.txt` - Ideal directory structure specification

---

## License & Attribution

MBC-4.0 / IGSOA Framework
Monistic Box Calculus

All content extracted from source markdown files in parent directory.
