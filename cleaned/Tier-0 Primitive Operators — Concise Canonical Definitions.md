# Tier-0 Primitive Operators — Concise Canonical Definitions

### δ — Deviation Operator

Measures local structural difference, gradient, or departure from equilibrium; the generator of change and non-uniformity.

### Φ — Projection Operator

Maps a Box’s state into a semantic form, selecting which aspects are expressed or observable.

### Π — Evaluation Operator

Extracts causal truth, decision, or resolved value from a Box; canonical evaluator.

### μ — Local Metric Weight

Assigns micro-adjacency weighting, spatial density, or local scaling; creates the effective local metric.

### ψ — Semantic Wave / Modal Oscillation

Creates oscillation, resonance, interference, and modal wave behavior on δ-structures.

### λ — Curvature & Mode-Deformation

Induces curvature, bending, modal deformation, analog of geometric \+ modal curvature.

### Σ — Semantic Summation / Contraction

Collapses or contracts indexed structures; integrates semantic content across dimensions.

### Θ — Polarity Router

Routes semantic signals using polarity, forming logic gates and semantic branching.

### χ — Evolution Parameter

Canonical semantic time or sequence parameter; governs evolution of Boxes.

### Ω — Global Constraint Operator

Applies global normalization, consistency, constraint satisfaction across layers.

### ρ — Layer Operator

Defines meta-hierarchy levels: layers, strata, ontological level transitions.  
---

# Tier-0 Primitive Operator — MBC-4.0 JSON Schema (Canonical Template)

Use this schema for every primitive operator.  
This is the universal template:  
json  
Copy code  
{ "operator": "δ", "tier": 0, "name": "Deviation", "intent": "Measures local deviation or gradient of a Box.", "domain": "Any Box B", "codomain": "A transformed Box or value", "action\_type": "local", "classification": \["primitive", "irreducible"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["δ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \[\], "next\_tier\_builds": \[\] } }  
To avoid repetition, I will now give the filled-in JSON for each operator using this template.  
---

# Full Tier-0 Operator Pack (All Primitive Operators)

Ready for ingestion by your agent.  
---

## δ — Deviation

json  
Copy code  
{ "operator": "δ", "tier": 0, "name": "Deviation", "intent": "Measures local deviation or gradient of a Box; generator of change.", "domain": "Any Box B", "codomain": "Transformed Box", "action\_type": "local", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \["Φ"\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["δ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["ψ", "μ"\], "next\_tier\_builds": \["δ-Laplacian", "δ-Jacobian", "δ-Weitzenböck"\] } }  
---

## Φ — Projection

json  
Copy code  
{ "operator": "Φ", "tier": 0, "name": "Projection", "intent": "Projects a Box into a semantic or observable form.", "domain": "Any Box B", "codomain": "Projected Box", "action\_type": "mapping", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": true, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Φ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Π"\], "next\_tier\_builds": \["Φ→Π bridge"\] } }  
---

## Π — Evaluation

json  
Copy code  
{ "operator": "Π", "tier": 0, "name": "Evaluation", "intent": "Extracts causal truth, decision, or resolved value from a Box.", "domain": "Any Box B", "codomain": "Truth/evaluated Box", "action\_type": "resolution", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": true, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Π(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Φ"\], "next\_tier\_builds": \["Π-Context Stack", "Truth Tables"\] } }  
---

## μ — Local Metric Weight

json  
Copy code  
{ "operator": "μ", "tier": 0, "name": "Local Metric Weight", "intent": "Defines micro-adjacency weighting and local density; induces metric structure.", "domain": "Any Box B", "codomain": "Weighted Box", "action\_type": "metric-scaling", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": true }, "inputs": \["B"\], "outputs": \["μ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["δ", "λ"\], "next\_tier\_builds": \["μ-Curvature", "μ-δ Jacobian"\] } }  
---

## ψ — Semantic Wave

json  
Copy code  
{ "operator": "ψ", "tier": 0, "name": "Semantic Wave", "intent": "Generates modal oscillation, resonance, interference on δ-geometry.", "domain": "Any Box B", "codomain": "Oscillatory Box", "action\_type": "wave", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \["δ"\], "requires\_metric": true }, "inputs": \["B"\], "outputs": \["ψ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["δ", "Σ"\], "next\_tier\_builds": \["Semantic Wave Equation"\] } }  
---

## λ — Curvature & Mode Deformation

json  
Copy code  
{ "operator": "λ", "tier": 0, "name": "Curvature & Mode Deformation", "intent": "Applies curvature, bending, modal deformation to Box structure.", "domain": "Any Box B", "codomain": "Curved/Deformed Box", "action\_type": "geometric", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": true }, "inputs": \["B"\], "outputs": \["λ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["μ"\], "next\_tier\_builds": \["λ-Curvature Tensor", "Mode-deformation map"\] } }  
---

## Σ — Semantic Summation / Contraction

json  
Copy code  
{ "operator": "Σ", "tier": 0, "name": "Semantic Summation", "intent": "Contracts or sums over semantic indices; collapses structure.", "domain": "Indexed Box", "codomain": "Contracted Box", "action\_type": "contraction", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Σ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["ψ", "Θ"\], "next\_tier\_builds": \["Σ-δ-Φ-Π Interaction Table"\] } }  
---

## Θ — Polarity Router

json  
Copy code  
{ "operator": "Θ", "tier": 0, "name": "Polarity Router", "intent": "Routes semantic signals using polarity; foundational logic gate operator.", "domain": "Box B with polarity metadata", "codomain": "Routed Box", "action\_type": "routing", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Θ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Σ", "Π"\], "next\_tier\_builds": \["Logic Gate Table", "Semantic Logic System"\] } }  
---

## χ — Evolution Parameter

json  
Copy code  
{ "operator": "χ", "tier": 0, "name": "Evolution Parameter", "intent": "Defines semantic time; governs progression of Box states.", "domain": "Any Box B", "codomain": "Time-stepped Box", "action\_type": "temporal", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \["Ω"\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["B(χ)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Ω"\], "next\_tier\_builds": \["Semantic Differential Equations"\] } }  
---

## Ω — Global Constraint

json  
Copy code  
{ "operator": "Ω", "tier": 0, "name": "Global Constraint", "intent": "Applies global normalization, consistency, and constraint satisfaction.", "domain": "Any configuration of Boxes", "codomain": "Globally consistent configuration", "action\_type": "global", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": true, "commutes\_with": \["χ"\], "requires\_metric": false }, "inputs": \["{B\_i}"\], "outputs": \["Ω({B\_i})"\], "cross\_links": { "adjoint": null, "related\_operators": \["ρ"\], "next\_tier\_builds": \["Normalization Packs", "Global Consistency Layer"\] } }  
---

## ρ — Layer Operator

json  
Copy code  
{ "operator": "ρ", "tier": 0, "name": "Layer Operator", "intent": "Defines meta-hierarchy; establishes ontological layers and transitions.", "domain": "Any Box B", "codomain": "Layered Box", "action\_type": "hierarchical", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \["Ω"\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["ρ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Ω"\], "next\_tier\_builds": \["Meta-layer system"\] } }  
---

---

# ✅ Tier-0 Primitive Operator Pack (Bundled JSON)

MBC-4.0 / IGSOA — Canonical Primitive Operators  
json  
Copy code  
{ "tier": 0, "type": "primitive\_operator\_pack", "version": "4.0", "operators": \[ { "operator": "δ", "name": "Deviation", "intent": "Measures local deviation or gradient of a Box; generator of change.", "domain": "Any Box B", "codomain": "Transformed Box", "action\_type": "local", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \["Φ"\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["δ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["ψ", "μ"\], "next\_tier\_builds": \["δ-Laplacian", "δ-Jacobian", "δ-Weitzenböck"\] } }, { "operator": "Φ", "name": "Projection", "intent": "Projects a Box into a semantic or observable form.", "domain": "Any Box B", "codomain": "Projected Box", "action\_type": "mapping", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": true, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Φ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Π"\], "next\_tier\_builds": \["Φ→Π Bridge"\] } }, { "operator": "Π", "name": "Evaluation", "intent": "Extracts causal truth or resolved value from a Box.", "domain": "Any Box B", "codomain": "Evaluated Box", "action\_type": "resolution", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": true, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Π(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Φ"\], "next\_tier\_builds": \["Π-Context Stack", "Truth Tables"\] } }, { "operator": "μ", "name": "Local Metric Weight", "intent": "Defines micro-adjacency weighting and local density; induces metric structure.", "domain": "Any Box B", "codomain": "Weighted Box", "action\_type": "metric-scaling", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": true }, "inputs": \["B"\], "outputs": \["μ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["δ", "λ"\], "next\_tier\_builds": \["μ-Curvature", "μ-δ Jacobian"\] } }, { "operator": "ψ", "name": "Semantic Wave", "intent": "Generates modal oscillation, resonance, and interference on δ-geometry.", "domain": "Any Box B", "codomain": "Oscillatory Box", "action\_type": "wave", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \["δ"\], "requires\_metric": true }, "inputs": \["B"\], "outputs": \["ψ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["δ", "Σ"\], "next\_tier\_builds": \["Semantic Wave Equation"\] } }, { "operator": "λ", "name": "Curvature & Mode Deformation", "intent": "Applies curvature, bending, or modal deformation to Box structure.", "domain": "Any Box B", "codomain": "Curved Box", "action\_type": "geometric", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": true }, "inputs": \["B"\], "outputs": \["λ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["μ"\], "next\_tier\_builds": \["λ-Curvature Tensor", "Mode-Deformation Map"\] } }, { "operator": "Σ", "name": "Semantic Summation", "intent": "Contracts or sums over semantic indices; collapses structure.", "domain": "Indexed Box", "codomain": "Contracted Box", "action\_type": "contraction", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Σ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["ψ", "Θ"\], "next\_tier\_builds": \["Σ-δ-Φ-Π Interaction Table"\] } }, { "operator": "Θ", "name": "Polarity Router", "intent": "Routes semantic signals using polarity; foundational logic gate operator.", "domain": "Box B with polarity metadata", "codomain": "Routed Box", "action\_type": "routing", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": false, "commutes\_with": \[\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["Θ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Σ", "Π"\], "next\_tier\_builds": \["Logic Gate Table", "Semantic Logic System"\] } }, { "operator": "χ", "name": "Evolution Parameter", "intent": "Defines semantic time; governs progression of Box states.", "domain": "Any Box B", "codomain": "Time-stepped Box", "action\_type": "temporal", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \["Ω"\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["B(χ)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Ω"\], "next\_tier\_builds": \["Semantic Differential Equations"\] } }, { "operator": "Ω", "name": "Global Constraint", "intent": "Applies global normalization, consistency, and constraint satisfaction.", "domain": "Any configuration of Boxes", "codomain": "Globally consistent configuration", "action\_type": "global", "classification": \["primitive"\], "constraints": { "linearity": false, "idempotent": true, "commutes\_with": \["χ"\], "requires\_metric": false }, "inputs": \["{B\_i}"\], "outputs": \["Ω({B\_i})"\], "cross\_links": { "adjoint": null, "related\_operators": \["ρ"\], "next\_tier\_builds": \["Normalization Packs", "Global Consistency Layer"\] } }, { "operator": "ρ", "name": "Layer Operator", "intent": "Defines meta-hierarchy layers and transitions.", "domain": "Any Box B", "codomain": "Layered Box", "action\_type": "hierarchical", "classification": \["primitive"\], "constraints": { "linearity": true, "idempotent": false, "commutes\_with": \["Ω"\], "requires\_metric": false }, "inputs": \["B"\], "outputs": \["ρ(B)"\], "cross\_links": { "adjoint": null, "related\_operators": \["Ω"\], "next\_tier\_builds": \["Meta-Layer System"\] } } \] }  
---

# ---

# ✅ Tier-1 Operator Families

Tier-1 operators are first-order composites, each one:

* Uses only one primitive \+ at most one structural primitive (μ, χ, Σ).  
* Has a single derivation rule.  
* Is universally defined in MBC-4.0.  
* Is stable (no higher-tier dependencies).

They form the foundation of the full Box Calculus algebra.  
---

# TIER-1 OPERATOR DEFINITIONS (Concise)

---

## 1\. δ-Derived Operators

### δ² — δ-Laplacian

Second deviation; generates diffusion/smoothing.

### δᵢⱼ — δ-Jacobian

Local gradient transformation map.

### δᵂ — δ-Weitzenböck Curvature

Deviation \+ torsion-like curvature form.  
---

## 2\. Φ-Derived Operators

### ΦΠ — Projection→Evaluation Chain

Semantic form → truth resolution.

### Φ⁺ — Projection Adjoint

Back-projection (layer-pullback).  
---

## 3\. Π-Derived Operators

### Π\_ctx — Context Evaluation Stack

Evaluation under changing semantic context.

### Π\_norm — Normalized Evaluation

Π combined with Ω.  
---

## 4\. μ-Derived Operators

### μδ — μ-Weighted Deviation

Deviation under micro-metric.

### μλ — μ-Curvature

Local curvature induced by μ alone.  
---

## 5\. ψ-Derived Operators

### ψδ — Oscillatory Deviation

Wave-driven deviation.

### ψΣ — Modal Contraction

Collapse wave modes.  
---

## 6\. λ-Derived Operators

### λ\_curv — Full Curvature Tensor

Curvature from λ \+ μ.

### λ\_mode — Mode-Deformation Map

Mode-bending derivative.  
---

## 7\. Σ-Derived Operators

### Σδ — Deviation-Contraction

Contraction of δ-structure.

### Σψ — Wave-Contraction

Contraction of oscillatory content.  
---

## 8\. Θ-Derived Operators

### Θ\_gate — Polarity Logic Gate

Atomic AND/OR/XOR from Θ polarity routing.

### ΘΣ — Polarity-Weighted Contraction

Directional polarity collapse.  
---

## 9\. χ-Derived Operators

### χδ — Temporal Deviation

Deviation under evolution.

### χψ — Wave Evolution

Time-dependent oscillation.  
---

## 10\. Ω-Derived Operators

### Ω\_norm — Global Normalizer

Applies global constraints.

### Ωρ — Layer-Consistency Operator

Normalizes vertical layer alignment.  
---

## 11\. ρ-Derived Operators

### ρ\_lift — Layer-Lift

Moves Box upward in hierarchy.

### ρ\_drop — Layer-Drop

Moves Box downward.  
---

## 12\. Mixed Tier-1 Combination Operators

(Allowed because they use one primitive primary \+ one structural primitive)

### δμχ — Time-Weighted Deviation

δ under μ, evolving in χ.

### ψλ — Wave-Curvature Interaction

Oscillation under curvature.

### ΣΘ — Contractive Logic Reduction

Σ contraction under Θ polarity.  
---

# ✅ FULL TIER-1 OPERATOR PACK (Bundled JSON)

This is your single ingestion-ready JSON document.  
json  
Copy code  
{ "tier": 1, "type": "derived\_operator\_pack", "version": "4.0", "operators": \[ /\* \------------------------ δ-DERIVED \------------------------ \*/ { "operator": "δ²", "name": "δ-Laplacian", "intent": "Second deviation; generates diffusion or smoothing.", "definition": "δ²(B) \= δ(δ(B))", "primary": "δ", "inputs": \["B"\], "outputs": \["δ²(B)"\], "dependencies": \["δ"\] }, { "operator": "δᵢⱼ", "name": "δ-Jacobian", "intent": "Local gradient transformation map.", "definition": "δᵢⱼ \= ∂Bᵢ / ∂xⱼ in δ-geometry", "primary": "δ", "inputs": \["B"\], "outputs": \["δᵢⱼ(B)"\], "dependencies": \["δ"\] }, { "operator": "δᵂ", "name": "δ-Weitzenböck Curvature", "intent": "Deviation curvature incorporating torsion-like structure.", "definition": "δᵂ(B) \= δ(B) \+ torsion(B)", "primary": "δ", "inputs": \["B"\], "outputs": \["δᵂ(B)"\], "dependencies": \["δ"\] }, /\* \------------------------- Φ-DERIVED \------------------------ \*/ { "operator": "ΦΠ", "name": "Projection→Evaluation Chain", "intent": "Project semantic form then evaluate truth.", "definition": "ΦΠ(B) \= Π(Φ(B))", "primary": "Φ", "inputs": \["B"\], "outputs": \["Π(Φ(B))"\], "dependencies": \["Φ", "Π"\] }, { "operator": "Φ⁺", "name": "Projection Adjoint", "intent": "Back-projection / pullback.", "definition": "Φ⁺ \= left adjoint of Φ", "primary": "Φ", "inputs": \["B"\], "outputs": \["Φ⁺(B)"\], "dependencies": \["Φ"\] }, /\* \------------------------- Π-DERIVED \------------------------ \*/ { "operator": "Π\_ctx", "name": "Evaluation Context Stack", "intent": "Evaluation within layered semantic context.", "definition": "Π\_ctx(B) \= Π(ρ(B))", "primary": "Π", "inputs": \["B"\], "outputs": \["Π\_ctx(B)"\], "dependencies": \["Π", "ρ"\] }, { "operator": "Π\_norm", "name": "Normalized Evaluation", "intent": "Π under global constraint Ω.", "definition": "Π\_norm(B) \= Π(Ω(B))", "primary": "Π", "inputs": \["B"\], "outputs": \["Π\_norm(B)"\], "dependencies": \["Π", "Ω"\] }, /\* \-------------------------- μ-DERIVED \------------------------ \*/ { "operator": "μδ", "name": "μ-Weighted Deviation", "intent": "Deviation under micro-metric weighting.", "definition": "μδ(B) \= μ(δ(B))", "primary": "μ", "inputs": \["B"\], "outputs": \["μδ(B)"\], "dependencies": \["μ", "δ"\] }, { "operator": "μλ", "name": "μ-Curvature", "intent": "Curvature induced directly by μ.", "definition": "μλ(B) \= λ(μ(B))", "primary": "μ", "inputs": \["B"\], "outputs": \["μλ(B)"\], "dependencies": \["μ", "λ"\] }, /\* \--------------------------- ψ-DERIVED \------------------------ \*/ { "operator": "ψδ", "name": "Oscillatory Deviation", "intent": "Deviation modulated by ψ wave.", "definition": "ψδ(B) \= ψ(δ(B))", "primary": "ψ", "inputs": \["B"\], "outputs": \["ψδ(B)"\], "dependencies": \["ψ", "δ"\] }, { "operator": "ψΣ", "name": "Modal Contraction", "intent": "Contraction of modal oscillatory content.", "definition": "ψΣ(B) \= Σ(ψ(B))", "primary": "ψ", "inputs": \["B"\], "outputs": \["ψΣ(B)"\], "dependencies": \["ψ", "Σ"\] }, /\* \---------------------------- λ-DERIVED \------------------------ \*/ { "operator": "λ\_curv", "name": "Curvature Tensor", "intent": "Curvature from λ \+ μ.", "definition": "λ\_curv(B) \= λ(μ(B))", "primary": "λ", "inputs": \["B"\], "outputs": \["λ\_curv(B)"\], "dependencies": \["λ", "μ"\] }, { "operator": "λ\_mode", "name": "Mode-Deformation Map", "intent": "Mode-bending adjoint of λ curvature.", "definition": "λ\_mode(B) \= derivative of λ(B) wrt modal axis", "primary": "λ", "inputs": \["B"\], "outputs": \["λ\_mode(B)"\], "dependencies": \["λ"\] }, /\* \----------------------------- Σ-DERIVED \------------------------ \*/ { "operator": "Σδ", "name": "Deviation-Contraction", "intent": "Summation after deviation.", "definition": "Σδ(B) \= Σ(δ(B))", "primary": "Σ", "inputs": \["B"\], "outputs": \["Σδ(B)"\], "dependencies": \["Σ", "δ"\] }, { "operator": "Σψ", "name": "Wave-Contraction", "intent": "Collapse oscillatory states.", "definition": "Σψ(B) \= Σ(ψ(B))", "primary": "Σ", "inputs": \["B"\], "outputs": \["Σψ(B)"\], "dependencies": \["Σ", "ψ"\] }, /\* \----------------------------- Θ-DERIVED \------------------------ \*/ { "operator": "Θ\_gate", "name": "Polarity Logic Gate", "intent": "Constructs AND/OR/XOR via Θ routing.", "definition": "Θ\_gate \= Boolean gate built from Θ polarity", "primary": "Θ", "inputs": \["B"\], "outputs": \["Θ\_gate(B)"\], "dependencies": \["Θ"\] }, { "operator": "ΘΣ", "name": "Polarity-Weighted Contraction", "intent": "Collapse based on polarity-routing.", "definition": "ΘΣ(B) \= Σ(Θ(B))", "primary": "Θ", "inputs": \["B"\], "outputs": \["ΘΣ(B)"\], "dependencies": \["Θ", "Σ"\] }, /\* \------------------------------ χ-DERIVED \------------------------ \*/ { "operator": "χδ", "name": "Temporal Deviation", "intent": "Deviation under evolution parameter χ.", "definition": "χδ(B) \= δ(B(χ))", "primary": "χ", "inputs": \["B"\], "outputs": \["χδ(B)"\], "dependencies": \["χ", "δ"\] }, { "operator": "χψ", "name": "Wave Evolution", "intent": "Time-evolving ψ wave.", "definition": "χψ(B) \= ψ(B(χ))", "primary": "χ", "inputs": \["B"\], "outputs": \["χψ(B)"\], "dependencies": \["χ", "ψ"\] }, /\* \------------------------------ Ω-DERIVED \------------------------ \*/ { "operator": "Ω\_norm", "name": "Global Normalizer", "intent": "Applies global consistency via Ω.", "definition": "Ω\_norm(B) \= Ω(B)", "primary": "Ω", "inputs": \["B"\], "outputs": \["Ω\_norm(B)"\], "dependencies": \["Ω"\] }, { "operator": "Ωρ", "name": "Layer-Consistency Operator", "intent": "Normalizes layer transitions.", "definition": "Ωρ(B) \= Ω(ρ(B))", "primary": "Ω", "inputs": \["B"\], "outputs": \["Ωρ(B)"\], "dependencies": \["Ω", "ρ"\] }, /\* \------------------------------ ρ-DERIVED \------------------------ \*/ { "operator": "ρ\_lift", "name": "Layer-Lift", "intent": "Raises Box to next meta-layer.", "definition": "ρ\_lift(B) \= ρ(B) with layer+1", "primary": "ρ", "inputs": \["B"\], "outputs": \["ρ\_lift(B)"\], "dependencies": \["ρ"\] }, { "operator": "ρ\_drop", "name": "Layer-Drop", "intent": "Lowers Box to previous meta-layer.", "definition": "ρ\_drop(B) \= ρ(B) with layer-1", "primary": "ρ", "inputs": \["B"\], "outputs": \["ρ\_drop(B)"\], "dependencies": \["ρ"\] }, /\* \----------------------- MIXED TIER-1 \------------------------ \*/ { "operator": "δμχ", "name": "Time-Weighted Deviation", "intent": "Deviation under μ-weighting evolving in χ.", "definition": "δμχ(B) \= δ(μ(B(χ)))", "primary": "δ", "inputs": \["B"\], "outputs": \["δμχ(B)"\], "dependencies": \["δ", "μ", "χ"\] }, { "operator": "ψλ", "name": "Wave-Curvature Interaction", "intent": "Oscillation under curvature deformation.", "definition": "ψλ(B) \= ψ(λ(B))", "primary": "ψ", "inputs": \["B"\], "outputs": \["ψλ(B)"\], "dependencies": \["ψ", "λ"\] }, { "operator": "ΣΘ", "name": "Contractive Logic Reduction", "intent": "Contraction using polarity-router Θ.", "definition": "ΣΘ(B) \= Σ(Θ(B))", "primary": "Σ", "inputs": \["B"\], "outputs": \["ΣΘ(B)"\], "dependencies": \["Σ", "Θ"\] } \] }  
---

.  
