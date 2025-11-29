#  TIER 00 — PRIMITIVE STRUCTURES (FULL 6-FILE PACK)

### Covers every Tier-00 entity:

* Primitive Values (0, 1, ±, ∞, ⊥, ⊤)  
* Primitive Operators (δ Φ Π μ ψ λ Σ Θ χ ρ Ω)  
* Primitive Logical Entities (Truth Atom, Polarity Atom…)  
* Primitive Evolution Entities (χ-step, Path atom, Rewrite Atom…)  
* Primitive Geometric Entities (Point, Edge, Face, Box…)  
* Primitive Domain Structures (Tensor, Graph Node/Edge, Router Node, Layer Atom)

This is the Tier-00 foundation block on which Tier-01 begins building.  
---

# 📁 1\. tier\_00\_metadata.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 00 — PRIMITIVE STRUCTURES METADATA // \=========================================================================== tier: 0, name: "Primitive Structures", description: "Defines all irreducible semantic, logical, geometric, and algebraic primitives of IGSOA.", version: "1.0", status: "sealed", primitives: { values: \["0", "1", "±", "∞", "⊥", "⊤"\], operators: \["δ","Φ","Π","μ","ψ","λ","Σ","Θ","χ","ρ","Ω"\], logical\_entities: \[ "TruthAtom", "PolarityAtom", "SemanticClassAtom", "DeviationAtom" \], evolution\_entities: \[ "χ-step", "SemanticPathElement", "RewriteRuleAtom" \], geometric\_entities: \[ "Point", "Edge", "Face", "Box", "TensorIndex", "Mode" \], domain\_structures: \[ "DomainTensor", "SemanticGraphNode", "SemanticGraphEdge", "RouterNode", "LayerAtom" \] }, invariants: \[ "Box Integrity Invariant", "Domain Tensor Rank Invariant", "Adjacency Integrity Invariant", "Layer Consistency Invariant" \] }  
---

# 📁 2\. tier\_00\_operator\_pack.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 00 — PRIMITIVE OPERATOR PACK // \=========================================================================== operators: { δ: { role: "deviation", arity: 1, description: "Local displacement operator" }, Φ: { role: "projection", arity: 1, description: "Semantic class projection" }, Π: { role: "evaluation", arity: 1, description: "Truth/evaluation operator" }, μ: { role: "weight", arity: 1, description: "Adjacency/weight operator" }, ψ: { role: "wave", arity: 1, description: "Oscillatory semantic mode" }, λ: { role: "curvature", arity: 1, description: "Deformation/torsion operator" }, Σ: { role: "contraction", arity: 2, description: "Semantic summation" }, Θ: { role: "polarity-logic", arity: 1, description: "Polarity and logic router" }, χ: { role: "evolution", arity: 1, description: "Semantic time evolution" }, ρ: { role: "layer", arity: 1, description: "Federated layering operator" }, Ω: { role: "normalization", arity: 1, description: "Global constraint normalizer" } }, meta\_operators: { "\[A,B\]": "semantic commutator", "{A,B}": "semantic anticommutator", "A∘B": "composition", "A⊗B": "tensor product", "A⊕B": "semantic sum", "A⋆B": "semantic convolution", "A⇒B": "inference arrow", "A↦B": "rewrite arrow" }, examples: \[ { expression: "\[δ,Φ\]", meaning: "deviation-projection commutator" }, { expression: "Φ∘Π", meaning: "projection then evaluation" }, { expression: "δ⊕Φ", meaning: "semantic combination of deviation \+ projection" } \] }  
---

# 📁 3\. tier\_00\_interaction\_table.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 00 — PRIMITIVE INTERACTION TABLE // \=========================================================================== interactions: { δ: { acts\_on: \["DeviationAtom", "Point", "DomainTensor"\], preserves: \["tensor\_rank"\], forbidden: \["TruthAtom"\] }, Φ: { acts\_on: \["SemanticClassAtom", "Box"\], preserves: \["semantic\_class"\], forbidden: \["RouterNode"\] }, Π: { acts\_on: \["TruthAtom", "PolarityAtom"\], outputs: \["⊤", "⊥"\] }, Θ: { acts\_on: \["PolarityAtom"\], outputs: \["Θ+", "Θ−"\], preserves: \["polarity\_sign"\] }, χ: { acts\_on: \["SemanticPathElement", "RewriteRuleAtom"\], preserves: \["path\_length"\], constraints: \["χ-step must be atomic"\] }, μ: { acts\_on: \["SemanticGraphEdge"\], preserves: \["non-negativity"\] }, λ: { acts\_on: \["Edge","Face","Box"\], preserves: \["torsion\_rank"\] }, ψ: { acts\_on: \["Mode"\], preserves: \["frequency\_mode"\] } } }  
---

# 📁 4\. tier\_00\_axiom\_box.json5

This is the Sealed Axiom Box for Tier-00.  
json5  
Copy code  
{ // \=========================================================================== // TIER 00 — SEALED AXIOM BOX // \=========================================================================== sealed: true, axioms: { A0\_PrimitiveIrreducibility: "Primitive entities cannot be rewritten, decomposed, or factored by any operator.", A1\_OperatorDomainAxiom: "Each primitive operator has a fixed domain of action that cannot be expanded in Tier-00.", A2\_TensorRankAxiom: "No Tier-00 operator may change the order of a Domain Tensor.", A3\_BoxIntegrityAxiom: "A primitive Box must retain all δ–Φ–Π fields during any Tier-00 rewrite.", A4\_PolaritySignAxiom: "Θ operators preserve net polarity sign across all primitive entities.", A5\_AdjacencyIntegrityAxiom: "Graph adjacency structure cannot be altered by any Tier-00 operator.", A6\_LayerAtomicityAxiom: "Layer atoms (ρ₀) cannot federate, merge, or split in Tier-00.", A7\_TruthEvaluationAxiom: "Π applied to any TruthAtom must return exactly ⊤ or ⊥." } }  
---

# 📁 5\. tier\_00\_rewrite\_system.json5

This includes the requested invalid → NF repaired example.  
json5  
Copy code  
{ // \=========================================================================== // TIER 00 — REWRITE SYSTEM // \=========================================================================== rewrite\_rules: \[ { id: "r0", pattern: "invalid\_tensor\_rank\_change", action: "REPAIR → restore original rank", invariant: "Domain Tensor Rank Invariant", example: { before: { tensor: "Dᵢⱼ", applied: "δ", illegal\_change\_to: "Dᵢⱼₖ" }, after: { tensor: "Dᵢⱼ (restored)" } } }, { id: "r1", pattern: "Φ applied to router node", action: "BLOCK → return ⊥", invariant: "Operator Domain Axiom" }, { id: "r2", pattern: "Θ flips polarity", action: "REPAIR → restore original polarity sign", invariant: "Polarity Sign Axiom" }, { id: "r3", pattern: "δ removes Φ-field from a Box", action: "REPAIR → reattach Φ-field", invariant: "Box Integrity Axiom", example: { before: { box: "{δ,Π}", missing: "Φ" }, after: { box: "{δ,Φ,Π}" } } } \], // Multi-step δ–Φ–Π–ψ chain (requested) example\_chain: { initial\_state: "{Box: {δ, Φ, Π}}", steps: \[ "apply δ → valid", "apply Φ → valid", "apply Π → valid", "apply ψ → invalid removal of δ-field", "rewrite via r3 → restore δ-field" \], final\_state: "{Box: {δ, Φ, Π}} // INVARIANT-SAFE NORMAL FORM" } }  
---

# 📁 6\. tier\_00\_module\_pack.json5

This is the Tier-00 federated pack that links all files.  
json5  
Copy code  
{ // \=========================================================================== // TIER 00 — MODULE PACK (MASTER INDEX) // \=========================================================================== tier: 0, name: "Primitive Structures Module Pack", includes: { metadata: "tier\_00\_metadata.json5", operator\_pack: "tier\_00\_operator\_pack.json5", interaction\_table: "tier\_00\_interaction\_table.json5", axiom\_box: "tier\_00\_axiom\_box.json5", rewrite\_system: "tier\_00\_rewrite\_system.json5" }, exports: { primitives: { values: \["0","1","±","∞","⊥","⊤"\], operators: \["δ","Φ","Π","μ","ψ","λ","Σ","Θ","χ","ρ","Ω"\], domain\_structures: \[ "DomainTensor", "SemanticGraphNode", "SemanticGraphEdge", "RouterNode", "LayerAtom" \] } }, test\_suite: "T0-SI-TESTS.json5", notes: "Tier-00 feeds directly into Tier-01 via δ-action on primitives." }  
---

---

# ✅ TIER 01 — δ-Family (Deviation Geometry)

### Includes:

* Deviation Geometry Operators  
* δ-Curvature  
* δ-Norm  
* Weitzenböck Torsion Rank  
* Deviation Flow \+ Local δ-Frames  
* Full axiom box  
* Rewrite system with NF rules  
* Interaction table  
* Module pack

---

# 📁 1\. tier\_01\_metadata.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 01 — Deviation Geometry Metadata // \=========================================================================== tier: 1, family: "δ-Family", name: "Deviation Geometry", description: "Introduces deviation curvature, δ-norm, torsion rank, and deviation-frame geometry.", version: "1.0", status: "sealed", primitives\_used: \["Point", "Edge", "Face", "Box", "TensorIndex", "Mode"\], operators\_extended: \["δ", "λ", "ψ", "Σ"\], invariants\_extended: \[ "δ-Curvature Sign Invariant", "δ-Norm Invariant", "Weitzenböck Torsion Rank Invariant", "Deviation-Flow Continuity Invariant" \], // Bridge rule reference extends\_from\_tier\_00: true, bridge\_files: \["tier\_00\_operator\_pack.json5", "tier\_00\_axiom\_box.json5"\] }  
---

# 📁 2\. tier\_01\_operator\_pack.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 01 — δ OPERATOR PACK // \=========================================================================== operators: { δ: { role: "deviation", description: "Computes local geometric deviation from flat δ=0 baseline.", outputs: \["δ-curvature", "δ-frame", "δ-norm"\], arity: 1 }, δ²: { role: "second deviation", description: "Computes second-order deviation; used for δ-curvature sign.", arity: 1 }, ∇δ: { role: "δ-gradient", description: "Spatial gradient of deviation field.", arity: 1 }, λδ: { role: "torsion curvature coupling", description: "Couples deviation to torsion rank via λ.", arity: 2 } }, derived\_quantities: { δ\_curvature: "κ\_δ \= δ²(x) \- λ(x)", δ\_norm: "||δ|| \= sqrt( δ\_i δ^i )", torsion\_rank: "τ \= rank(Tⁱⱼₖ)" }, examples: \[ { op: "δ(Point)", out: "local deviation vector" }, { op: "δ(Edge)", out: "edge curvature shift" }, { op: "∇δ(Box)", out: "δ-gradient frame" }, { op: "λδ(δ, λ)", out: "torsion adjusted deviation" } \] }  
---

# 📁 3\. tier\_01\_interaction\_table.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 01 — INTERACTION TABLE (δ × geometry) // \=========================================================================== interactions: { δ: { acts\_on: \["Point", "Edge", "Face", "Box"\], outputs: \["δ-vector", "δ-curvature", "δ-frame"\], preserves: \["dimension"\], forbidden: \["TruthAtom", "PolarityAtom"\] }, δ²: { acts\_on: \["Point", "Edge"\], outputs: \["second-order curvature"\], preserves: \["sign of curvature"\] }, ∇δ: { acts\_on: \["Box", "Face"\], outputs: \["δ-gradient frame"\] }, λδ: { acts\_on: \["Edge", "Face", "Box"\], depends\_on: \["torsion\_rank"\], preserves: \["torsion\_rank"\], constraints: \["λδ cannot modify torsion sign"\] } }, // Interaction with Tier-00 cross\_tier: { δ: { Box: "extends Tier-00 DEVIATE(B)", DomainTensor: "allowed only if tensor order preserved" }, λ: { inherits: "λ curvature rules from Tier-00" } } }  
---

# 📁 4\. tier\_01\_axiom\_box.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 01 — SEALED AXIOM BOX (Deviation Geometry) // \=========================================================================== sealed: true, axioms: { A1\_δCurvatureSignInvariant: "δ-curvature cannot spontaneously flip sign under any Tier-01 operator.", A2\_δNormInvariant: "The δ-norm must remain invariant under δ-frame reparameterizations.", A3\_TorsionRankInvariant: "Weitzenböck torsion rank τ must remain constant under δ, δ², ∇δ, or λδ.", A4\_DeviationFlowContinuity: "Deviation evolution must be C¹-continuous unless explicitly discretized.", A5\_TensorOrderPreservation: "δ and δ² cannot change the index order of domain tensors.", A6\_FrameAttachmentAxiom: "Every δ-frame must remain attached to its base Box unless rewritten by a legal rule.", A7\_δλCouplingAxiom: "Torsion curvature coupling λδ must not violate curvature sign or torsion rank invariants." } }  
---

# 📁 5\. tier\_01\_rewrite\_system.json5

Includes:

* δ-curvature repair  
* δ-norm preservation  
* torsion-rank repair  
* illegal δ-flows → NF  
* example chain

json5  
Copy code  
{ // \=========================================================================== // TIER 01 — REWRITE SYSTEM (Deviation Geometry) // \=========================================================================== rewrite\_rules: \[ // \--------------------------------------------------------- // δ-curvature sign protection // \--------------------------------------------------------- { id: "r1\_δ\_sign", pattern: "δ-curvature flips sign illegally", action: "REPAIR → restore original curvature sign", invariant: "δ-Curvature Sign Invariant", example: { before: { κ\_δ: "+1", op: "illegal δ²" }, after: { κ\_δ: "+1" } } }, // \--------------------------------------------------------- // δ-norm preservation // \--------------------------------------------------------- { id: "r2\_norm", pattern: "δ-norm changes under frame reparameterization", action: "REPAIR → normalize ||δ||", invariant: "δ-Norm Invariant" }, // \--------------------------------------------------------- // torsion rank preservation // \--------------------------------------------------------- { id: "r3\_torsion", pattern: "λδ modifies torsion rank", action: "BLOCK → return ⊥", invariant: "Torsion Rank Invariant" }, // \--------------------------------------------------------- // illegal δ-flow (discontinuity) // \--------------------------------------------------------- { id: "r4\_flow", pattern: "discontinuous δ-flow", action: "SMOOTH → enforce C¹ continuity", invariant: "Deviation Flow Continuity" }, // \--------------------------------------------------------- // δ-gradient frame stabilization // \--------------------------------------------------------- { id: "r5\_frame", pattern: "δ-gradient detaches from Box", action: "REATTACH", invariant: "Frame Attachment Axiom" } \], // \----------------------------------------------------------- // Multi-step example δ → δ² → ∇δ → λδ → NF // \----------------------------------------------------------- example\_chain: { initial\_state: "{Point: p}", steps: \[ "apply δ(p) → δ₁", "apply δ²(p) → κ\_δ", "apply ∇δ(Box(p)) → δ-frame", "apply λδ(δ-frame) → illegal torsion shift", "rewrite via r3\_torsion → restore τ", "NF check → curvature sign preserved → δ-geometry NORMAL FORM" \], final\_state: "{Box(p): {δ, κ\_δ, δ-frame}}" } }  
---

# 📁 6\. tier\_01\_module\_pack.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 01 — δ-FAMILY MODULE PACK // \=========================================================================== tier: 1, name: "Deviation Geometry Module Pack", family: "δ-Family", includes: { metadata: "tier\_01\_metadata.json5", operator\_pack: "tier\_01\_operator\_pack.json5", interaction\_table: "tier\_01\_interaction\_table.json5", axiom\_box: "tier\_01\_axiom\_box.json5", rewrite\_system: "tier\_01\_rewrite\_system.json5" }, exports: { geometric\_primitives: \["Point","Edge","Face","Box","TensorIndex"\], deviation\_constructs: \[ "δ-vector", "δ-curvature", "δ-norm", "δ-frame", "torsion\_rank" \] }, bridge\_from\_tier\_00: "Tier-01 extends δ-action over Tier-00 geometric primitives.", test\_suite: "T1-δ-TESTS.json5" }  
---

---

## 📁 1\. tier\_02\_metadata.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 02 — Φ-Family (Semantic Projection) — METADATA // \=========================================================================== tier: 2, family: "Φ-Family", name: "Semantic Projection", description: "Introduces Φ-based semantic class projection, class lattices, and Φ–Π commutative chains over Tier-00/01 structures.", version: "1.0", status: "sealed", primitives\_used: \[ "SemanticClassAtom", // from Primitive Logical Entities "TruthAtom", "PolarityAtom", "DomainTensor", "Box", "SemanticGraphNode", "SemanticGraphEdge" \], operators\_extended: \[ "Φ", // base projection "Φ\_class", // classification "Φ\_lift", // lifting to higher class "Φ\_restrict"// restricting to sub-class \], invariants\_extended: \[ "Class Preservation Invariant", "Projection–Evaluation Consistency Invariant", "Φ-Idempotence Invariant", "Semantic Separation Invariant" \], extends\_from\_tiers: \[0, 1\], bridge\_files: \[ "tier\_00\_operator\_pack.json5", "tier\_01\_operator\_pack.json5", "tier\_00\_axiom\_box.json5", "tier\_01\_axiom\_box.json5" \] }  
---

## 📁 2\. tier\_02\_operator\_pack.json5

json  
Copy code  
{ // \=========================================================================== // TIER 02 — Φ OPERATOR PACK (Semantic Projection) // \=========================================================================== operators: { Φ: { role: "semantic\_projection", description: "Projects any admissible entity into its semantic class representation.", arity: 1, outputs: \["SemanticClassAtom", "ClassLabel"\], laws: \[ "Idempotent: Φ(Φ(x)) \= Φ(x)", "Class-preserving: Φ(x) ∈ C(x)" \] }, Φ\_class: { role: "classifier", description: "Returns a canonical semantic class label for a given entity.", arity: 1, outputs: \["ClassLabel"\] }, Φ\_lift: { role: "class\_lift", description: "Lifts an element from a lower-level semantic class to a higher / more abstract class in the class lattice.", arity: 1, outputs: \["SemanticClassAtom"\] }, Φ\_restrict: { role: "class\_restriction", description: "Restricts an element to a sub-class or sub-typing of its semantic class.", arity: 1, outputs: \["SemanticClassAtom"\] } }, // \--------------------------------------------------------------------------- // Derived quantities and helper constructs // \--------------------------------------------------------------------------- derived\_quantities: { semantic\_class\_id: "A unique identifier for a semantic class (e.g. Φ\_class(x) \= 'Box/Geometric').", class\_distance: "A metric d(C1, C2) on the lattice of semantic classes; used to measure semantic separation.", class\_lattice: "A partial order (C, ≤) where C are semantic classes and ≤ is the refinement / abstraction relation." }, examples: \[ { op: "Φ(Box)", out: "SemanticClassAtom: 'Box/Geometric'", comment: "Projects a concrete Box into its semantic class." }, { op: "Φ(SemanticGraphNode)", out: "SemanticClassAtom: 'Graph/Node'", comment: "Node → Graph/Node class." }, { op: "Φ\_class(TruthAtom)", out: "'Logic/Truth'", comment: "Classification of logical truth entities." }, { op: "Φ\_lift('Graph/Node')", out: "SemanticClassAtom: 'Graph/Structure'", comment: "Lifts node to its graph-level abstraction." }, { op: "Φ\_restrict('Box/Geometric')", out: "SemanticClassAtom: 'Box/Geometric/δ-Frame'", comment: "Restricts to δ-geometry flavoured Box." } \] }  
---

## 📁 3\. tier\_02\_interaction\_table.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 02 — INTERACTION TABLE (Φ × structures × Π) // \=========================================================================== interactions: { Φ: { acts\_on: \[ "Box", "DomainTensor", "SemanticGraphNode", "SemanticGraphEdge", "TruthAtom", "PolarityAtom" \], outputs: \[ "SemanticClassAtom", "ClassLabel" \], preserves: \[ "semantic\_class\_validity" \], forbidden: \[ "undefined\_domain\_entities" // any entity with no class definition \] }, Φ\_class: { acts\_on: \["any\_admissible\_entity"\], outputs: \["ClassLabel"\], preserves: \["equivalence\_class"\], // equal entities share same class label constraints: \[ "If x ≡ y then Φ\_class(x) \= Φ\_class(y)." \] }, Φ\_lift: { acts\_on: \["SemanticClassAtom"\], outputs: \["SemanticClassAtom"\], constraints: \[ "Φ\_lift(C) ≥ C in the class lattice." \] }, Φ\_restrict: { acts\_on: \["SemanticClassAtom"\], outputs: \["SemanticClassAtom"\], constraints: \[ "Φ\_restrict(C) ≤ C in the class lattice." \] } }, // \--------------------------------------------------------------------------- // Cross-operator interactions (Φ with Π and δ) // \--------------------------------------------------------------------------- cross\_operator: { "Π∘Φ": { description: "Evaluate the truth of a projected semantic class.", law: "Projection–Evaluation Consistency: Π(Φ(x)) \= Π(x) when x is semantically well-typed." }, "Φ∘Π": { description: "Project truth-evaluated object into its truth class.", law: "Projection–Evaluation Consistency: Φ(Π(x)) \= Φ(x) as a class of truth-bearing entities." }, "δ∘Φ": { description: "Deviation of a projected geometric entity (approximate).", law: "In general δ∘Φ may differ from Φ∘δ, but both must preserve class validity." }, "Φ∘δ": { description: "Projection of a deviation-perturbed entity into semantic class.", law: "Class Preservation: δ-perturbations must not produce undefined classes." } } }  
---

## 📁 4\. tier\_02\_axiom\_box.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 02 — SEALED AXIOM BOX (Semantic Projection) // \=========================================================================== sealed: true, axioms: { // \------------------------------------------------------------------------- // Core Φ invariants from your spec // \------------------------------------------------------------------------- A1\_ClassPreservationInvariant: "Φ-projection may not produce undefined or invalid semantic classes; every admissible entity has a well-defined Φ-image.", A2\_ProjectionEvaluationConsistency: "For any semantically well-typed x, Π(Φ(x)) \= Π(x) and Φ(Π(x)) \= Φ(x) up to canonical identification in the semantic class lattice.", // \------------------------------------------------------------------------- // Additional Φ-structure axioms // \------------------------------------------------------------------------- A3\_ΦIdempotence: "For all admissible x, Φ(Φ(x)) \= Φ(x). Φ is a projection operator onto semantic class space.", A4\_SemanticSeparationInvariant: "If Φ(x) ≠ Φ(y), then x and y belong to disjoint semantic classes with strictly positive class\_distance.", A5\_ClassLatticeAxiom: "The set of all semantic classes with the refinement / abstraction relation forms a partial order (class\_lattice).", A6\_ClassLiftRestrictionAxiom: "Φ\_lift and Φ\_restrict must move only along the class\_lattice: Φ\_lift(C) ≥ C, Φ\_restrict(C) ≤ C, and neither may produce undefined classes.", A7\_BoxFieldCompleteness: "For any Box with fields {δ,Φ,Π} at Tier-02, the Φ-field must be consistent with both the δ-geometry class and the Π-truth class (no mixed or contradictory classification)." } }  
---

## 📁 5\. tier\_02\_rewrite\_system.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 02 — REWRITE SYSTEM (Semantic Projection) // \=========================================================================== rewrite\_rules: \[ // \------------------------------------------------------------------------- // r1 — Undefined or invalid semantic class → repair or reject // \------------------------------------------------------------------------- { id: "r2\_1\_class\_repair", pattern: "Φ(x) \= undefined", action: "REPAIR → map x to a canonical fallback semantic class or signal ⊥", invariant: "Class Preservation Invariant", example: { before: { x: "UnknownEntity", Φ\_of\_x: "undefined" }, after: { x: "UnknownEntity", Φ\_of\_x: "SemanticClassAtom: 'Unknown/Other'" } } }, // \------------------------------------------------------------------------- // r2 — Enforce Φ idempotence (Φ(Φ(x)) → Φ(x)) // \------------------------------------------------------------------------- { id: "r2\_2\_idempotence", pattern: "Φ(Φ(x))", action: "REWRITE → Φ(x)", invariant: "Φ-Idempotence Invariant" }, // \------------------------------------------------------------------------- // r3 — Projection–Evaluation commutativity normalization // \------------------------------------------------------------------------- { id: "r2\_3\_PiPhi\_commute", pattern: "Π(Φ(x)) and Φ(Π(x)) disagree", action: "NORMALIZE → enforce Π(Φ(x)) \= Π(x) and Φ(Π(x)) \= Φ(x) when x is well-typed", invariant: "Projection–Evaluation Consistency Invariant", example: { before: { expr1: "Π(Φ(Box)) \= ⊤", expr2: "Π(Box) \= ⊥" }, after: { expr1: "Π(Φ(Box)) \= Π(Box)", expr2: "Π(Box) \= Π(Φ(Box))" } } }, // \------------------------------------------------------------------------- // r4 — Illegal class merge (violates separation) // \------------------------------------------------------------------------- { id: "r2\_4\_class\_merge\_block", pattern: "Φ(x) and Φ(y) merged into a single class when class\_distance \> 0", action: "BLOCK → return ⊥ or split into distinct classes", invariant: "Semantic Separation Invariant" }, // \------------------------------------------------------------------------- // r5 — Inconsistent Box Φ-field with δ/Π fields // \------------------------------------------------------------------------- { id: "r2\_5\_box\_consistency", pattern: "Box({δ, Φ, Π}) where Φ(Box) is inconsistent with δ-geometry or Π-truth class", action: "REPAIR → adjust Φ(Box) to the nearest consistent semantic class or signal ⊥", invariant: "Box Field Completeness Axiom" } \], // \--------------------------------------------------------------------------- // Multi-step example chain: // Box with δ-geometry and Π-evaluation flows through Φ, with repairs // \--------------------------------------------------------------------------- example\_chain: { initial\_state: { box: "{δ, Π}", comment: "Box has geometry and truth but no explicit Φ-class yet." }, steps: \[ "Apply Φ(Box) → tentative class 'Box/Geometric/?'.", "Apply Π(Φ(Box)) and Π(Box) → detect inconsistency.", "Rewrite via r2\_3\_PiPhi\_commute → normalize Π∘Φ vs Π.", "Detect that Φ(Box) conflicts with δ-geometry label.", "Rewrite via r2\_5\_box\_consistency → adjust Φ(Box) to 'Box/Geometric/δ-Frame'.", "Apply idempotence: Φ(Φ(Box)) → Φ(Box) via r2\_2\_idempotence." \], final\_state: { box: "{δ, Φ, Π}", Φ\_box: "SemanticClassAtom: 'Box/Geometric/δ-Frame'", comment: "All invariants satisfied, expression in Φ-NORMAL FORM." } } }  
---

## 📁 6\. tier\_02\_module\_pack.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 02 — Φ-FAMILY MODULE PACK // \=========================================================================== tier: 2, name: "Semantic Projection Module Pack", family: "Φ-Family", includes: { metadata: "tier\_02\_metadata.json5", operator\_pack: "tier\_02\_operator\_pack.json5", interaction\_table: "tier\_02\_interaction\_table.json5", axiom\_box: "tier\_02\_axiom\_box.json5", rewrite\_system: "tier\_02\_rewrite\_system.json5" }, exports: { semantic\_classes: \[ "SemanticClassAtom", "ClassLabel", "class\_lattice" \], operators: \[ "Φ", "Φ\_class", "Φ\_lift", "Φ\_restrict" \], invariants: \[ "Class Preservation Invariant", "Projection–Evaluation Consistency Invariant", "Φ-Idempotence Invariant", "Semantic Separation Invariant" \] }, bridge\_from\_tiers: { "0": "Φ projects Primitive Logical / Geometric entities into semantic classes.", "1": "Φ aligns δ-geometry objects with their semantic class labels (δ-Frames, torsion structures, etc.)." }, test\_suite: "T2-Φ-TESTS.json5", notes: "Tier-02 formalizes semantic projection and its commutative relationship with evaluation Π over the growing IGSOA structure." }  
---

---

# ✅ TIER 03 — Π-Family (Evaluation / Truth / Causality)

### Included:

1. tier\_03\_metadata.json5  
2. tier\_03\_operator\_pack.json5  
3. tier\_03\_interaction\_table.json5  
4. tier\_03\_axiom\_box.json5  
5. tier\_03\_rewrite\_system.json5  
6. tier\_03\_module\_pack.json5

---

# 📁 1\. tier\_03\_metadata.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 03 — Π-Family Metadata // \=========================================================================== tier: 3, family: "Π-Family", name: "Evaluation / Truth / Causality", description: "Introduces Π-evaluation, truth measurement, semantic causality, evaluation lattices, and Π-normal forms. Completes the Tri-Unity δ–Φ–Π core.", version: "1.0", status: "sealed", primitives\_used: \[ "TruthAtom", "PolarityAtom", "SemanticClassAtom", "Box", "DomainTensor", "δ-vector", "SemanticGraphNode" \], operators\_extended: \[ "Π", "Π\_truth", "Π\_cause", "Π\_chain", "Π\_measure" \], invariants\_extended: \[ "Truth-Preservation Invariant", "Causality Monotonicity Invariant", "Evaluation Consistency Invariant", "Tri-Unity Commutativity (δ–Φ–Π)", "Π-Normal Form Invariant" \], extends\_from\_tiers: \[0, 1, 2\], bridge\_files: \[ "tier\_00\_axiom\_box.json5", "tier\_01\_axiom\_box.json5", "tier\_02\_axiom\_box.json5" \] }  
---

# 📁 2\. tier\_03\_operator\_pack.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 03 — Π OPERATOR PACK (Truth / Evaluation / Causality) // \=========================================================================== operators: { Π: { role: "evaluation", description: "Evaluates an entity's truth-state, causal validity, or semantic consistency.", arity: 1, outputs: \["⊤", "⊥", "Π-value"\], laws: \[ "Π is total on all well-typed entities.", "Π(x) \= Π(Φ(x)) via Projection–Evaluation Consistency.", "Π(x) is invariant under δ unless δ violates class/type invariants." \] }, Π\_truth: { role: "truth\_evaluation", description: "Evaluates logical truth: maps TruthAtoms to ⊤ or ⊥.", outputs: \["⊤", "⊥"\] }, Π\_cause: { role: "causal\_evaluation", description: "Evaluates whether x causally follows from y in the semantic/causal graph.", arity: 2, outputs: \["causal", "non-causal", "indeterminate"\] }, Π\_chain: { role: "causal\_chain", description: "Evaluates an entire causal chain for monotonicity, validity, and DAG-consistency.", arity: "n", outputs: \["valid\_chain", "invalid\_chain"\] }, Π\_measure: { role: "evaluation\_metric", description: "Returns real-valued evaluation measures (semantic energy, causal weight, etc.).", outputs: \["ℝ"\] } }, derived\_quantities: { truth\_value: "Π\_truth(x) ∈ {⊤, ⊥}", causal\_relation: "Π\_cause(x, y) \= causal if x → y in the causal graph", chain\_validity: "Π\_chain(x1,...,xn) ensures no backward causal edges", evaluation\_norm: "||Π(x)|| \= numeric measure of evaluation strength" }, examples: \[ { op: "Π(Box)", out: "Π-value reflecting Box consistency" }, { op: "Π\_truth(TruthAtom)", out: "⊤ or ⊥" }, { op: "Π\_cause(A,B)", out: "causal" }, { op: "Π\_chain(\[A,B,C\])", out: "valid\_chain" }, { op: "Π\_measure(Box)", out: "real semantic score" } \] }  
---

# 📁 3\. tier\_03\_interaction\_table.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 03 — INTERACTION TABLE (Π × δ × Φ × logic × causality) // \=========================================================================== interactions: { Π: { acts\_on: \[ "TruthAtom", "Box", "SemanticClassAtom", "δ-frame", "DomainTensor" \], outputs: \["⊤", "⊥", "Π-value"\], preserves: \["typing", "evaluation\_consistency"\], forbidden: \["undefined\_entities"\] }, Π\_truth: { acts\_on: \["TruthAtom", "PolarityAtom"\], outputs: \["⊤", "⊥"\], preserves: \["truth\_axioms"\] }, Π\_cause: { acts\_on: \["SemanticGraphNode", "SemanticGraphEdge"\], outputs: \["causal", "non-causal", "indeterminate"\], constraints: \[ "Must not create cycles.", "Must not violate DAG structure." \] }, Π\_chain: { acts\_on: \["List\<SemanticGraphNode\>"\], outputs: \["valid\_chain", "invalid\_chain"\], preserves: \["causal\_monotonicity"\] }, Π\_measure: { acts\_on: \["any\_semantic\_entity"\], outputs: \["ℝ"\], preserves: \["class\_compatibility"\] } }, cross\_operator: { "Π∘Φ": { law: "Π(Φ(x)) \= Π(x) for all well-typed x." }, "Π∘δ": { law: "Π(δ(x)) \= Π(x) unless δ breaks Φ-class consistency." }, "Π∘Θ": { law: "Truth-Preserving: polarity must not alter Π-value." }, "Π∘Σ": { law: "Evaluation of sums is monotonic: Π(Σ(x,y)) ≥ min(Π(x), Π(y))." } } }  
---

# 📁 4\. tier\_03\_axiom\_box.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 03 — SEALED AXIOM BOX (Evaluation / Truth / Causality) // \=========================================================================== sealed: true, axioms: { // \------------------------------------------------------------------------- // Truth invariants // \------------------------------------------------------------------------- A1\_TruthPreservationInvariant: "Π(x) \= Π\_truth(x) for any TruthAtom. Truth evaluation cannot be modified by polarity, geometry, or projection.", A2\_LogicConsistencyAxiom: "If x entails y in logic, then Π(x) \= ⊤ implies Π(y) \= ⊤.", // \------------------------------------------------------------------------- // Causality invariants // \------------------------------------------------------------------------- A3\_CausalityMonotonicityInvariant: "If Π\_cause(x, y) \= causal, and Π(y) \= ⊤, then Π(x) must be ⊤.", A4\_CausalChainAxiom: "Π\_chain(x₁,...,xₙ) \= valid\_chain iff all edges point forward; cycles invalidate the chain.", // \------------------------------------------------------------------------- // Evaluation structure // \------------------------------------------------------------------------- A5\_EvaluationConsistencyInvariant: "Π(x) \= Π(Φ(x)) unless Φ(x) is undefined or inconsistent.", A6\_TriUnityCommutativity: "For admissible x: Π(Φ(δ(x))) \= Π(δ(Φ(x))).", // \------------------------------------------------------------------------- // Π-Normal Form definition // \------------------------------------------------------------------------- A7\_PiNormalFormInvariant: "A Π-expression is in Π-NF when: (1) Φ and δ actions do not change Π-value; (2) Truth is evaluated; (3) all causal chains are validated.", A8\_EvaluationTotalityAxiom: "Π must return a value (⊤, ⊥, or Π-value) for all well-typed semantic objects." } }  
---

# 📁 5\. tier\_03\_rewrite\_system.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 03 — REWRITE SYSTEM (Evaluation / Truth / Causality) // \=========================================================================== rewrite\_rules: \[ // \------------------------------------------------------------------------- // Truth rules // \------------------------------------------------------------------------- { id: "r3\_truth\_eval", pattern: "Π\_truth(x) produces no value", action: "REPAIR → enforce Π\_truth(x) ∈ {⊤, ⊥}", invariant: "Truth-Preservation Invariant" }, { id: "r3\_truth\_polarity", pattern: "Π(Θ(x)) ≠ Π(x)", action: "REPAIR → Π(Θ(x)) := Π(x)", invariant: "Truth-Preservation Invariant" }, // \------------------------------------------------------------------------- // Causality rules // \------------------------------------------------------------------------- { id: "r3\_cause\_cycle", pattern: "Π\_cause(x, x) or cycle in Π\_chain", action: "REWRITE → invalid\_chain", invariant: "CausalChainAxiom" }, { id: "r3\_causal\_backward", pattern: "Π\_cause(x, y) \= causal but x occurs after y", action: "BLOCK → non-causal", invariant: "Causality Monotonicity Invariant" }, // \------------------------------------------------------------------------- // Projection–Evaluation consistency // \------------------------------------------------------------------------- { id: "r3\_PiPhi\_commute", pattern: "Π(Φ(x)) ≠ Π(x)", action: "NORMALIZE → enforce Π(Φ(x)) \= Π(x) if Φ(x) is well-typed; otherwise signal ⊥", invariant: "EvaluationConsistencyInvariant" }, // \------------------------------------------------------------------------- // Π-Normal Form // \------------------------------------------------------------------------- { id: "r3\_normal\_form", pattern: "Complex Π-expression with unresolved δ or Φ", action: "REDUCE → Π-NF by evaluating truth and validating causality", invariant: "Π-Normal Form Invariant" } \], // \--------------------------------------------------------------------------- // Example multi-step δ–Φ–Π chain (as requested in Tier-00 pattern) // \--------------------------------------------------------------------------- example\_chain: { initial\_state: "Π(Φ(δ(Box)))", steps: \[ "Apply δ(Box) → δ-frame", "Apply Φ(δ-frame) → 'Box/Geometric/δ-Frame'", "Apply Π → tentative evaluation", "Check Π(Φ(..)) \= Π(..) using r3\_PiPhi\_commute", "Detect causal dependency in Box structure", "Apply Π\_cause(Box\_subcomponents)", "Validate causal chain with Π\_chain", "Reduce to Π-NF with r3\_normal\_form" \], final\_state: { PiNF: "⊤ or Π-value", comment: "All truth, causality, and projection invariants satisfied." } } }  
---

# 📁 6\. tier\_03\_module\_pack.json5

json5  
Copy code  
{ // \=========================================================================== // TIER 03 — Π-FAMILY MODULE PACK // \=========================================================================== tier: 3, name: "Evaluation / Truth / Causality Module Pack", family: "Π-Family", includes: { metadata: "tier\_03\_metadata.json5", operator\_pack: "tier\_03\_operator\_pack.json5", interaction\_table: "tier\_03\_interaction\_table.json5", axiom\_box: "tier\_03\_axiom\_box.json5", rewrite\_system: "tier\_03\_rewrite\_system.json5" }, exports: { evaluation\_entities: \[ "Π-value", "truth\_value", "causal\_relation", "chain\_validity", "evaluation\_norm" \], operators: \[ "Π", "Π\_truth", "Π\_cause", "Π\_chain", "Π\_measure" \], invariants: \[ "Truth-Preservation Invariant", "Causality Monotonicity Invariant", "Evaluation Consistency Invariant", "Tri-Unity Commutativity", "Π-Normal Form Invariant" \] }, bridge\_from\_tiers: { "0": "TruthAtoms, PolarityAtoms, Semantic primitives → evaluated by Π.", "1": "δ-geometry entities → evaluation must respect curvature/torsion consistency.", "2": "Φ-projection → Π∘Φ consistency enforced." }, test\_suite: "T3-Π-TESTS.json5", notes: "Tier-03 closes the Tri-Unity core (δ–Φ–Π) and defines the full evaluation/causality structure for higher tiers." }  
---

