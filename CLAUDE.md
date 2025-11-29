# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **IGSOA/MBC-4.0 Framework** (Integrated Geometric-Semantic Operator Algebra / Monistic Box Calculus v4) - a comprehensive mathematical-semantic framework implementing a 13-tier operator algebra system for AI agents. The repository contains:

- **Structured operator definitions** across 13 tiers (Tier 0-12)
- **Pooled variant system** for context-aware operator selection
- **JSON5-based canonical format** for machine-readable operator packs
- **Validation and testing infrastructure** in Python
- **Extensive documentation** in Markdown

The framework is designed to be both human-readable (textbook-quality documentation) and machine-parseable (JSON5 operator packs).

## Key Architecture Concepts

### Tri-Unity Foundation
The framework is built on three primitive operators:
- **δ** (delta): Deviation/geometry operator
- **Φ** (phi): Projection/semantic classification operator
- **Π** (pi): Evaluation/truth extraction operator

**Critical**: Base-level non-commutativity `[δ,Φ]≠0` is **foundational**, not a bug. This signals semantic richness.

### 13-Tier Operator Hierarchy
```
Tier 0:  Primitive Structures/Operators (δ, Φ, Π, μ, ψ, λ, Σ, Θ, χ, Ω, ρ)
Tier 1:  δ-Family (Deviation Geometry)
Tier 2:  Φ-Family (Semantic Projection)
Tier 3:  Π-Family (Evaluation/Truth/Causality)
Tier 4:  μ-Family (Local Weight/Adjacency)
Tier 5:  λ-Family (Curvature/Deformation)
Tier 6:  ψ-Family (Wave/Modes)
Tier 7:  Σ-Family (Summation/Contraction)
Tier 8:  Θ-Family (Polarity/Logic Routing)
Tier 9:  χ-Family (Semantic Evolution/Time)
Tier 10: Ω-Family (Global Constraints/Normalization)
Tier 11: ρ-Family (Layer/Meta-Hierarchy)
Tier 12: Ξ-Family (Top-Meta/Universal Schema)
```

### Pooled Variant System
The framework uses **context-aware variant pooling** to resolve apparent conflicts. Different formulations of the same operator are valid in different contexts:
- **Context-dependent**: λ-δ composition has 4 variants (canonical, flat geometry, symmetric approximation, perturbative expansion)
- **Level-dependent**: ψ-layer commutativity vs base-level non-commutativity
- **Selective**: Θ commutes with δ,Σ but not Φ,Π

Implemented in `cleaned/operators/variant_aware_router.py`.

### Universal Commutativity of Ω
**Important**: Ω commutes with ALL operators by axiom: `[Ω, O] = 0`. This is the defining property of Ω (global constraint operator). Ω does NOT need pooled variants.

## Directory Structure

### Core Directories
- `cleaned/` - Main working directory with all canonical content
- `cleaned/valid_json/` - Validated JSON files
- `cleaned/MBC_Framework_v4/` - Structured framework hierarchy
  - `00_Meta/` - Framework metadata
  - `01_Primitives/` - Primitive operator definitions
  - `02_Tiers/Tier_XX_<name>/` - Tier-specific files (13 tiers)
  - `03_MetaOperators/` - Meta-operator packs
  - `04_InteractionTables/` - Operator interaction matrices
  - `05_RewriteSystems/` - Normal form rewrite rules
  - `06_AxiomBoxes/` - Sealed axiom definitions
  - `07_Diagrams/` - Commutative diagrams
  - `08_ModulePacks/` - Bundled operator modules
- `cleaned/operators/` - Python implementation
  - `canonical/` - Canonical operator definitions (JSON)
  - `validation/` - Test suites
  - `examples/` - Usage examples
  - `variant_aware_router.py` - Router implementation
- `cleaned/reports/` - Analysis and completeness reports
- `cleaned/deliverables/` - Output artifacts

### Important Files
- `cleaned/claude.md` - Librarian agent configuration (JSON5 format)
- `cleaned/TEST_SUITE_MASTER_INDEX.md` - Central test registry
- `cleaned/valid_json/reports/AGENT_FAMILIARIZATION_GUIDE.json` - Comprehensive framework guide

## File Formats

### JSON5 vs JSON
**Use JSON5** for all semantic/operator files that humans edit:
- Operator packs
- Axiom boxes
- Rewrite systems
- Test suites
- Tier definitions

JSON5 allows:
- Comments (`//` and `/* */`)
- Trailing commas
- Mathematical symbols (δ, Φ, Π) as keys
- Human annotations inline with machine data

**Use standard JSON** only for:
- API communication
- Database storage
- Performance-critical pipelines

### Standard File Extensions
- `.json5` - Canonical operator/axiom definitions
- `.md` - Human documentation
- `.py` - Validation/router implementations
- `.pointer.json` - Reference pointers in MBC_Framework_v4

## Common Development Tasks

### Running Validation Tests
```bash
# Run the complete variant consistency test suite (11 tests)
python cleaned/operators/validation/variant_consistency_tests.py

# Expected: All tests pass (100% pass rate)
```

### Working with Operator Definitions
Operator packs follow this structure (JSON5):
```json5
{
  meta: {
    pack_id: "OPERATOR-PACK-ID",
    tier: N,
    family: "X-Family",
    version: "1.0.0",
    schema: "mbc4.operator_pack.vN"
  },
  operators: {
    δ: {
      definition: "...",
      type: "operator-type",
      domain: "semantic-domain",
      properties: { ... },
      examples: { ... }
    }
  },
  invariants: { ... },
  rewrite_system: { ... }
}
```

### Adding a New Operator Variant
1. Add JSON5 definition to `cleaned/operators/canonical/<operator>.json`
2. Include all 4 context dimensions:
   - `geometry_type`: flat, curved, unknown
   - `abstraction_level`: base_operator, psi_layer, mixed
   - `numerical_mode`: high_precision, stability_critical, analytical, normal
   - `safety_mode`: conservative, exploratory, normal
3. Update `variant_aware_router.py` with selection logic
4. Add tests to `cleaned/operators/validation/variant_consistency_tests.py`
5. Document in `cleaned/operators/POOLED_VARIANT_SYSTEM_README.md`

### Extracting JSON from Markdown Files
Many tier files contain embedded JSON blocks:
```bash
python cleaned/extract_json_from_transcripts.py
```

This extracts JSON blocks from markdown documentation into separate files.

### Finding Tier Definitions
Tier definitions are in both locations:
- Markdown: `cleaned/Tier-N — X-Family.md` or `cleaned/TIER N — X-FAMILY.md`
- JSON: `cleaned/valid_json/MBC_Framework_v4/02_Tiers/Tier_XX_<name>/`

For canonical mathematical proofs, see the markdown files (e.g., Tier-5 Canonical λ-Theorem at lines 191-501).

## Critical Implementation Details

### Normal Form (NF) System
Every operator expression reduces to a unique Normal Form (NF_*). Rewrite rules are defined per tier:
- Closure: δ-Φ-Π chains stay within Tri-Unity
- Commutativity: Cube paths commute at NF level
- Uniqueness: Each expression has exactly one NF

### Librarian Agent Mode
The `cleaned/claude.md` file defines a "Librarian" agent persona:
- Conservative (low creativity bias)
- High caution (Π + Ω prioritized)
- Never mutates theory without authorization
- Proposes repairs as diffs, not silent edits

When working as a Librarian, follow these constraints strictly.

### Test Suite Organization
Tests are organized by tier and invariant type. The master index is at:
`cleaned/TEST_SUITE_MASTER_INDEX.md`

Each test suite includes:
- Test ID and description
- Input patterns (symbolic, e.g., `[δ, Φ]`)
- Expected NF outputs
- Invariant tags (closure, commutativity, normal_form)

## Important Warnings

1. **Do NOT rename mathematical symbols**: δ stays as δ, not "delta"
2. **Do NOT treat Ω as needing variants**: Ω commutes with everything by axiom
3. **Do NOT assume non-commutativity is a bug**: It's foundational to MBC
4. **Do NOT create Tier-10 from scratch**: It already exists (3,569 lines with 10 textbook chapters)
5. **Do NOT use strict JSON**: Use JSON5 for all semantic/operator files
6. **Always read source tier files**: Summaries miss critical proofs and theorems

## High-Priority Items

### Implemented (100% complete)
- λ-δ composition pooled variant (4 contexts)
- ψ-commutativity pooled variant (level separation)
- Variant-aware router (712 lines, production-ready)
- Test suite (11/11 tests passing)

### High-Priority Next Steps
1. Implement Θ selective commutativity pooled variant
2. Implement δ-Φ level separation pooled variant
3. Implement μ-λ coupling pooled variant
4. Extract Tier-10 Ω-Family JSON modules (10 modules in markdown)
5. Extract Tier-6 ψ-Family complete JSON (40+ interaction rules)

## Key Mathematical Results

### Canonical λ-Theorem
Location: `cleaned/Tier-5 — λ-Family (Curvature _ Deformation).md`, lines 191-501

**Statement**: `λ(B) = λ_curv(B) + λ_mode(B) + λ_×(B)`

This provides mathematical proof that pooled variants are correct decomposition.

### Ω-Coherence Theorem
Location: `cleaned/Ten Textbook Chapter Titles for the Ω-Family.md`, Chapter 5

**Statement**: `[Ω, O] = 0` for ALL lawful operators

Ω is a meta-functor that commutes with everything by design.

### ψ-Layer Commutativity
Location: `cleaned/Tier-6 — ψ-Family (Semantic Oscillation _ Waves).md`, line 100

**Statement**: "All faces commute under ψ-action when weighted by μ and shaped by λ"

This validates level separation approach for apparent conflicts.

## Agent Familiarization Checklist

When starting work, ensure you understand:
- [ ] Tri-Unity (δ, Φ, Π) and why non-commutativity is foundational
- [ ] Difference between context-dependent and level-dependent pooling
- [ ] Why Ω doesn't need pooled variants (universal commutativity)
- [ ] Location of Canonical λ-Theorem and its significance
- [ ] Which 3 operators are high-priority for pooling next
- [ ] How to run validation tests and interpret results
- [ ] Difference between summary reports and detailed tier files
- [ ] That Tier-10 is exceptionally complete (needs extraction, not creation)

## Reference Documentation

### Essential Reading (in order)
1. `cleaned/reports/POOLED_VARIANT_REPORTS_INDEX.md` - Navigation index
2. `cleaned/reports/Completeness_Summary.md` - Quick status overview
3. `cleaned/reports/COMPREHENSIVE_LIBRARY_ANALYSIS.md` - Complete operator coverage (13 tiers)
4. `cleaned/reports/Pooled_Variant_System_Completeness_Report.md` - Quality assessment
5. `cleaned/valid_json/reports/AGENT_FAMILIARIZATION_GUIDE.json` - Detailed guide

### Key Reports
- Completeness: `cleaned/reports/Completeness_Summary.md`
- Library analysis: `cleaned/reports/COMPREHENSIVE_LIBRARY_ANALYSIS.md`
- Gap analysis: `cleaned/reports/MBC_Framework_Gap_Analysis.md`
- Logic gates: `cleaned/reports/Logic_Gates_Implementation_Analysis.md`

## Version Control Notes

- Repository uses Git
- Current branch: `main`
- Avoid large binary files
- JSON5 files are diff-friendly (trailing commas help)
- Use semantic commit messages

## Contact/Support

For questions about the framework:
- Read agent familiarization guide first
- Check tier files for canonical proofs
- Consult pooled variant system documentation
- Run validation tests to verify assumptions
