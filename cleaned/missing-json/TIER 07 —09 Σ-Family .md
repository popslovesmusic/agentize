#  TIER 07 — Σ-Family (Summation / Contraction)

### Complete 6-File Package (JSON5)

All files are ready to drop directly into your IGSOA textbook library.  
---

# 1\. tier\_07\_metadata.json5

json5  
Copy code  
{ // \============================================================ // TIER 07 — Σ-FAMILY METADATA // Summation / Contraction / Aggregation Layer // \============================================================ "tier": 7, "name": "Σ-Family", "role": "Semantic Summation / Tensor Contraction / Aggregation", "description": \` Σ is the universal contraction operator of IGSOA. It reduces dimensionality, aggregates semantic fields, collapses ψ-mode superpositions, and forms evaluable Π-states. Σ acts as the counterpart to δ (expansion) and ψ (oscillation). \`, "core\_principles": \[ "Σ reduces degrees of freedom while preserving semantic class boundaries (Φ).", "Σ contracts ψ-modes into stable Π-evaluable forms.", "Σ interacts with μ-weights as weighted summation.", "Σ preserves Ω-consistency and never creates contradictions.", "Σ is associative but not necessarily commutative in semantic space." \], "invariants": { "Rank-Reduction Invariant": "Σ must strictly decrease tensor rank unless special case Σ⁰.", "Weighted-Integrity Invariant": "Σ(μ-weighted domain) must keep μ normalization.", "Modal-Contraction Invariant": "ψ superpositions must collapse to stable Σ-states.", "Semantic-Class Preservation": "Φ-classes must remain well-defined after contraction." } }  
---

# 2\. tier\_07\_operator\_pack.json5

json5  
Copy code  
{ // \============================================================ // Σ OPERATOR PACK — Tier 07 // \============================================================ "operators": { "Σ": { "type": "semantic\_contraction", "arity": "n→1", "rank\_effect": "-1 per contraction (unless Σ⁰)", "commutativity": "conditional", "associativity": true, "description": "Primary tensor/semantic contraction operator." }, "Σ\_w": { "type": "weighted\_summation", "inputs": \["values", "weights"\], "description": "μ-weight–aware contraction." }, "Σ\_ψ": { "type": "mode\_contraction", "domain": "ψ-modes", "description": "Collapses mode superpositions into Σ-summary state." }, "Σ\_λ": { "type": "curvature\_aware\_contraction", "description": "Contraction respecting λ-deformation geometry." }, "Σ\_Φ": { "type": "class\_preserving\_contraction", "description": "Contracts only within Φ-semantic class boundaries." } } }  
---

# 3\. tier\_07\_interaction\_table.json5

### (Σ × all earlier tiers)

json5  
Copy code  
{ // \============================================================ // Σ INTERACTION TABLE // \============================================================ "interactions": { "Σ × δ": "Σ contracts fields produced by δ expansion; δΣ ≠ Σδ in general.", "Σ × Φ": "Σ may only contract within Φ-classes unless override flag set.", "Σ × Π": "Σ produces Π-ready semantic aggregates.", "Σ × μ": "Σ\_w performs μ-weighted contraction.", "Σ × λ": "Σ\_λ respects geometric curvature deformation.", "Σ × ψ": "Σ\_ψ collapses oscillatory ψ-modes into contracted stable state.", "Σ × Θ": "Polarity must be conserved under Σ unless explicitly antisymmetric.", "Σ × χ": "χ-evolution steps may schedule Σ contractions as semantic events.", "Σ × Ω": "Σ must preserve global consistency.", "Σ × ρ": "Σ participates in layer-fusion during hierarchy reductions." } }  
---

# 4\. tier\_07\_axiom\_box.json5

### Σ-Family Sealed Axiom Box (Canonical)

json5  
Copy code  
{ // \============================================================ // Σ-FAMILY AXIOM BOX (SEALED) // \============================================================ "axioms": { "Axiom Σ1 — Rank Reduction": "Σ(T\_{i j k...}) → T\_{i j...} // strictly reduces rank (unless Σ⁰).", "Axiom Σ2 — Weighted Integrity": "Σ\_w(x\_i, μ\_i) \= Σ(μ\_i \* x\_i) // μ-structure preserved.", "Axiom Σ3 — Mode Contraction": "Σ\_ψ(ψ\_1 \+ ψ\_2 \+ ... \+ ψ\_n) \= stable\_mode\_state.", "Axiom Σ4 — Φ-Class Preservation": "Σ\_Φ(x\_i∈C) ∈ C // contraction stays inside Φ-class.", "Axiom Σ5 — Consistency Preservation": "Σ never maps a consistent set to ⊥ unless input contains ⊥." }, "theorems": { "Σ-Theorem 1 — Associative Contraction": "Σ(Σ(A,B),C) \= Σ(A,B,C).", "Σ-Theorem 2 — Mixed Contraction Stability": "Σ\_ψ ∘ Σ\_w \= Σ\_w ∘ Σ\_ψ under μ-normalized mode sets.", "Σ-Theorem 3 — Π-Ready Normal Form": "Π(Σ(X)) \= Π(NF\_Σ(X))." } }  
---

# 5\. tier\_07\_rewrite\_system.json5

### NF rules for contraction, weighted reduction, and ψ-collapse

json5  
Copy code  
{ // \============================================================ // Σ-FAMILY REWRITE SYSTEM // \============================================================ "rewrite\_rules": \[ { "rule": "Σ(x, y) → x \+ y", "note": "Linear contraction of two terms." }, { "rule": "Σ(x\_1, x\_2, ..., x\_n) → Σ(Σ(x\_1, x\_2), ..., x\_n)", "note": "Associative unfolding." }, { "rule": "Σ\_w(x\_i, μ\_i) → Σ(μ\_i \* x\_i)", "note": "Weighted summation via μ-weights." }, { "rule": "Σ\_ψ(ψ\_1 \+ ψ\_2) → ψ\_stable", "note": "Mode contraction / collapse." }, { "rule": "Σ ∘ Φ → Φ ∘ Σ", "constraint": "Allowed only inside class-consistent domains." }, { "rule": "Σ ∘ δ → NonCommutative(δ ∘ Σ)", "note": "Reduction after expansion is noncommutative." }, { "rule": "Σ ∘ Π → Π", "note": "Once contracted, Π evaluation is direct." } \], "normal\_forms": { "NF\_Σ\_tensor": "minimal tensor rank representation", "NF\_Σ\_ψ": "single-mode stable state", "NF\_Σ\_weighted": "μ-normalized contraction" } }  
---

# 6\. tier\_07\_module\_pack.json5

### Reference implementation modules for Σ-operations

json5  
Copy code  
{ // \============================================================ // Σ MODULE PACK — Tier 07 // \============================================================ "modules": { "Σ.contract": { "input": "tensor/list/vector", "output": "lower-rank contracted form", "pseudocode": \` function Σ\_contract(items): if items.length \== 1: return items\[0\] return Σ\_contract(\[items\[0\] \+ items\[1\]\] \+ items\[2:\]) \` }, "Σ.weighted": { "input": "values \+ μ-weights", "output": "μ-weighted contraction", "pseudocode": \` function Σ\_weighted(values, weights): return Σ\_contract(weights\[i\] \* values\[i\] for all i) \` }, "Σ.mode\_collapse": { "input": "ψ-superposition", "output": "stable contracted ψ-state", "pseudocode": \` function Σψ(modes): return stabilized\_mode(modes) \` }, "Σ.curvature\_aware": { "input": "tensor \+ λ-geometry", "output": "λ-covariant contraction", "pseudocode": \` function Σλ(tensor, lambda\_field): return contract\_with\_metric(tensor, lambda\_field.metric) \` } } }  
---

---

# ✅ TIER 08 — Θ-FAMILY (POLARITY / LOGIC ROUTING)

## Complete Six-File Package in Proper IGSOA Format

---

# 1\. tier\_08\_metadata.json5

json5  
Copy code  
{ // \============================================================ // TIER 08 — Θ-FAMILY METADATA // Polarity / Logic Routing Layer // \============================================================ "tier": 8, "name": "Θ-Family", "role": "Polarity, logical routing, sign-structure, and semantic direction.", "description": \` Θ defines the polarity structure of IGSOA. It governs semantic \+ / − charge, logical switches, routing decisions, and the sign-tensor infrastructure that underlies Π-evaluation. Θ is the bridge between Σ-aggregation and Π-truth logic. \`, "core\_principles": \[ "Θ governs polarity and directed semantic flow.", "Θ-routing determines which branch Π will evaluate.", "Θ-sign cannot be spontaneously created/destroyed (Conservation Invariant).", "Θ-tensors contract under Σ while preserving sign structure.", "Θ interacts non-trivially with ψ (phase) and μ (local weight)." \], "invariants": { "Polarity Conservation Invariant": "Operators may route polarity, but cannot create or destroy it.", "Polarity Tensor-Sign Invariant": "Θ-tensor contraction must preserve net sign unless explicitly antisymmetric.", "Truth-Polarity Bridge Invariant": "Π evaluation must not violate Θ-sign structure.", "Routing Determinism Invariant": "Given (Θ, inputs), routing choice must be deterministic and normalized." } }  
---

# 2\. tier\_08\_operator\_pack.json5

### Θ-operators: polarity logic, routing, sign flow, and semantic logic gates.

json5  
Copy code  
{ // \============================================================ // Θ OPERATOR PACK — Tier 08 // \============================================================ "operators": { "Θ": { "type": "polarity\_operator", "description": "Primary polarity/sign operator (+ / −)." }, "Θ\_route": { "type": "polarity\_router", "description": "Directs semantic flow based on polarity patterns." }, "Θ\_flip": { "type": "inversion", "description": "Inverts polarity: \+ ↦ −, − ↦ \+." }, "Θ\_tensor": { "type": "polarity\_tensor\_constructor", "description": "Builds Θ-tensors for sign propagation." }, "Θ\_gate": { "type": "logic\_gate\_framework", "description": "Logical gates defined in terms of Θ \+ Σ \+ Π." }, // \----------------------------------------------------------- // Θ-defined Logic Gates // \----------------------------------------------------------- "AND": { "definition": "Θ\_gate(x,y, op='AND')" }, "OR": { "definition": "Θ\_gate(x,y, op='OR')" }, "XOR": { "definition": "Θ\_gate(x,y, op='XOR')" }, "NOT": { "definition": "Θ\_gate(x, op='NOT')" }, "IMPLIES": { "definition": "Θ\_gate(x,y, op='IMPLIES')"}, "NAND": { "definition": "Θ\_gate(x,y, op='NAND')" }, "NOR": { "definition": "Θ\_gate(x,y, op='NOR')" }, "XNOR": { "definition": "Θ\_gate(x,y, op='XNOR')" }, "FORALL": { "definition": "Θ\_gate(domain, op='FORALL')" }, "EXISTS": { "definition": "Θ\_gate(domain, op='EXISTS')" }, "NECESSITY": { "definition": "Θ\_gate(x, op='NECESSITY')" }, "POSSIBILITY": { "definition": "Θ\_gate(x, op='POSSIBILITY')" } } }  
---

# 3\. tier\_08\_interaction\_table.json5

### All Θ interactions across tiers (0–7 and forward into χ, Ω, ρ)

json  
Copy code  
{ // \============================================================ // Θ INTERACTION TABLE — Tier 08 // \============================================================ "interactions": { "Θ × δ": "δ-geometry may induce polarity routing boundaries.", "Θ × Φ": "Φ-classes determine allowable polarity branches.", "Θ × Π": "Θ supplies truth-polairty structure for Π logic.", "Θ × μ": "μ-weights scale polarity, but cannot flip sign.", "Θ × λ": "Curvature can bend polarity flow but preserves sign count.", "Θ × ψ": "Phase interacts with sign: Θ-phase coupling.", "Θ × Σ": "Σ contracts polarity tensors while preserving net sign.", "Θ × χ": "χ-evolution steps can trigger polarity-routing shifts.", "Θ × Ω": "Ω enforces global polarity consistency.", "Θ × ρ": "Θ-structure determines which layer a route flows into." } }  
---

# 4\. tier\_08\_axiom\_box.json5

### Canonical Θ-Family Sealed Axiom Box

js  
Copy code  
{ // \============================================================ // Θ-FAMILY AXIOM BOX (SEALED) // \============================================================ "axioms": { "Axiom Θ1 — Polarity Conservation": "Θ-routing preserves net polarity unless an explicit Θ\_flip is invoked.", "Axiom Θ2 — Sign-Tensor Integrity": "Contraction of Θ-tensors must preserve net sign (unless antisymmetric).", "Axiom Θ3 — Truth-Polarity Compatibility": "Π evaluation must respect Θ-structure: Π(Θ(x)) is well-defined.", "Axiom Θ4 — Routing Determinism": "Given inputs and Θ-state, the routing decision is unique.", "Axiom Θ5 — No Spontaneous Polarity Creation": "No operator except Θ\_flip may change sign orientation." }, "theorems": { "Θ-Theorem 1 — Logical Gate Completeness": "All classical Boolean gates can be generated from Θ \+ Π \+ Σ.", "Θ-Theorem 2 — Monotonicity under Σ": "Σ(Θ\_tensor) preserves polarity orientation.", "Θ-Theorem 3 — Π-Θ Commutation (Restricted)": "Π ∘ Θ \= Θ ∘ Π on truth-stable domains." } }  
---

# 5\. tier\_08\_rewrite\_system.json5

### Θ-aware Logic Normal Form \+ Routing Rules

js  
Copy code  
{ // \============================================================ // Θ REWRITE SYSTEM — Tier 08 // \============================================================ "rewrite\_rules": \[ // \----------------------------------------------------------- // Basic Polarity Rules // \----------------------------------------------------------- { "rule": "Θ\_flip(+1) → \-1", "note": "Invert polarity." }, { "rule": "Θ\_flip(-1) → \+1", "note": "Inverse operation." }, { "rule": "Θ(x) → sign(x) \* |x|", "note": "Extract polarity." }, // \----------------------------------------------------------- // Polarity Tensor Rules // \----------------------------------------------------------- { "rule": "Σ(Θ\_tensor(x,y)) → Θ\_tensor(Σ(x,y))", "constraint": "Allowed only if signs are class-consistent." }, { "rule": "Θ\_tensor(x,y) → (Θ(x), Θ(y))", "note": "Tensor decomposition." }, // \----------------------------------------------------------- // Logic Gate Rewrite Rules // \----------------------------------------------------------- { "rule": "NOT(+) → \-", "note": "Logical NOT via polarity flip." }, { "rule": "NOT(-) → \+", "note": "Inverse polarity." }, { "rule": "AND(+,+) → \+", "note": "Both positive." }, { "rule": "AND(+,-) → \-", "note": "Mixed polarity yields negative." }, { "rule": "AND(-,+) → \-", "note": "" }, { "rule": "AND(-,-) → \-", "note": "Negative dominates." }, { "rule": "OR(+,+) → \+" }, { "rule": "OR(+,-) → \+" }, { "rule": "OR(-,+) → \+" }, { "rule": "OR(-,-) → \-" }, { "rule": "XOR(+,+) → \-" }, { "rule": "XOR(-,-) → \-" }, { "rule": "XOR(+,-) → \+" }, { "rule": "XOR(-,+) → \+" }, // \----------------------------------------------------------- // Truth Evaluation Compatibility // \----------------------------------------------------------- { "rule": "Π(Θ(x)) → Θ(Π(x))", "constraint": "Truth-polairty compatibility domain only." } \], "normal\_forms": { "NF\_Θ\_logic": "simplest polarity-based logical form", "NF\_Θ\_tensor": "sign-preserving contracted tensor", "NF\_Θ\_route": "unique polarity-normalized routing decision" } }  
---

# 6\. tier\_08\_module\_pack.json5

json5  
Copy code  
{ // \============================================================ // Θ MODULE PACK — Tier 08 // \============================================================ "modules": { "Θ.extract": { "input": "semantic item", "output": "polarity (+/-)", "pseudocode": \` function Θ\_extract(x): return sign(x) \` }, "Θ.route": { "input": "inputs \+ polarity state", "output": "selected branch", "pseudocode": \` function Θ\_route(options, polarity): if polarity \== \+: return options.positive\_branch else: return options.negative\_branch \` }, "Θ.flip": { "input": "+/-", "output": "flipped sign", "pseudocode": \` function Θ\_flip(s): return \-s \` }, "Θ.gate": { "input": "values \+ operator", "output": "logical polarity output", "pseudocode": \` function Θ\_gate(values, op): // reduce domain to polarity-only logic return apply\_polarity\_logic(values, op) \` }, "Θ.tensor\_build": { "input": "values", "output": "Θ-tensor", "pseudocode": \` function Θ\_tensor(values): return tuple(Θ\_extract(v) for v in values) \` } } }  
---

---

# ✅ TIER 09 — χ-Family (Semantic Evolution / Time)

## Complete Six-File Package (JSON5)

All files are ready for your repository as-is.  
---

# 1\. tier\_09\_metadata.json5

json5  
Copy code  
{ // \============================================================ // TIER 09 — χ-FAMILY METADATA // Semantic Evolution / Temporal Flow Layer // \============================================================ "tier": 9, "name": "χ-Family", "role": "Semantic evolution, temporal flow, causal progression.", "description": \` χ defines the semantic evolution operator of IGSOA. It is the time-like engine that pushes δ-Φ-Π-μ-λ-ψ-Σ-Θ states forward along an ordered semantic path. χ enforces the arrow of semantic time and governs how states evolve into their normal forms. \`, "core\_principles": \[ "χ defines ordered semantic flow.", "χ-step is the atomic unit of semantic time.", "Evolution must follow monotonic forward progression (no reversal).", "χ integrates all prior tiers into causal-semantic sequences.", "χ defines temporal adjacency and causal accessibility." \], // \------------------------------------------------------------ // χ-Invariants // \------------------------------------------------------------ "invariants": { "Forward-Flow Invariant": "χ must never reverse semantic time. χ⁻¹ is forbidden except in sealed proofs.", "Continuity Invariant": "χ evolution must be continuous unless explicitly flagged as discrete.", "Monotonic Evolution Invariant": "Each χ-step must reduce or preserve semantic entropy but never create contradictions.", "Path Coherence Invariant": "Semantic paths formed by successive χ-steps must remain causally coherent.", "Evolution-NF Invariant": "Every χ chain converges to a unique χ-normal form (χ-NF)." } }  
---

# 2\. tier\_09\_operator\_pack.json5

json5  
Copy code  
{ // \============================================================ // χ OPERATOR PACK — Tier 09 // \============================================================ "operators": { "χ": { "type": "semantic\_time\_operator", "description": "Drives semantic evolution forward one χ-step." }, "χ\_step": { "type": "atomic\_evolution\_step", "description": "Minimal increment of semantic time." }, "χ\_flow": { "type": "continuous\_evolution\_flow", "description": "Smooth forward evolution unless discrete flag is applied." }, "χ\_discrete": { "type": "explicit\_discrete\_jump", "description": "Allowed discontinuity; bypasses continuity invariant with flag." }, "χ\_path": { "type": "semantic\_path\_constructor", "description": "Builds paths of temporal evolution." }, "χ\_integrate": { "type": "multi-tier\_evolution\_scheduler", "description": "Integrates δ-Φ-Π-μ-λ-ψ-Σ-Θ into χ-sequences." }, "χ\_apply": { "type": "evolution\_application", "description": "Apply χ to any IGSOA object; produce evolved state." } } }  
---

# 3\. tier\_09\_interaction\_table.json5

json5  
Copy code  
{ // \============================================================ // χ INTERACTION TABLE — Tier 09 // \============================================================ "interactions": { "χ × δ": "δ-deviation fields evolve under χ into stabilized curvature patterns.", "χ × Φ": "Semantic classes evolve; χ preserves class boundaries unless Φ-break flag.", "χ × Π": "Truth evaluation may be scheduled in χ-evolution cycles.", "χ × μ": "Local weights may drift or stabilize under χ-flow.", "χ × λ": "Curvature fields deform continuously across χ-time.", "χ × ψ": "Oscillatory modes propagate, decay, or stabilize under χ-flow.", "χ × Σ": "Contractions may occur during χ evolution events.", "χ × Θ": "Polarity-routing decisions may update as χ progresses.", "χ × Ω": "Global constraints regulate admissible χ-trajectories.", "χ × ρ": "Layer transitions may occur at defined χ thresholds." } }  
---

# 4\. tier\_09\_axiom\_box.json5

### Sealed χ-Axiom Box

json5  
Copy code  
{ // \============================================================ // χ-FAMILY AXIOM BOX (SEALED) // \============================================================ "axioms": { "Axiom χ1 — Forward Flow": "χ(x\_t) \= x\_{t+1} // χ always moves forward; no χ⁻¹.", "Axiom χ2 — Temporal Continuity": "χ\_flow(x\_t) is continuous unless χ\_discrete is explicitly invoked.", "Axiom χ3 — Semantic Path Coherence": "χ\_path(x\_0, x\_1, ..., x\_n) must be causally coherent.", "Axiom χ4 — Evolution Monotonicity": "χ must not generate contradictions or increase semantic entropy.", "Axiom χ5 — Evolution Normal Form": "For any x, repeated χ-steps converge to χ-NF(x)." }, "theorems": { "χ-Theorem 1 — Convergence": "∀x, ∃\! y such that χ^k(x) → y \= χ-NF(x).", "χ-Theorem 2 — Causal Accessibility": "If y is reachable from x under χ, then y ∈ CausalSphere(x).", "χ-Theorem 3 — Multi-Tier Stability": "χ-integrated chains stabilize δ-Φ-Π-μ-λ-ψ-Σ-Θ states." } }  
---

# 5\. tier\_09\_rewrite\_system.json5

### χ Evolution Rewrite System / Temporal Normal Forms

json5  
Copy code  
{ // \============================================================ // χ REWRITE SYSTEM — Tier 09 // \============================================================ "rewrite\_rules": \[ // \----------------------------------------------------------- // Forward Flow // \----------------------------------------------------------- { "rule": "χ(x\_t) → x\_{t+1}", "note": "Advance semantic state one step." }, { "rule": "χ(x\_{t+1}) → x\_{t+2}", "note": "χ cannot reverse (no χ(x\_{t+1}) → x\_t)." }, // \----------------------------------------------------------- // Path Construction // \----------------------------------------------------------- { "rule": "χ\_path(x0) → \[x0\]", "note": "Start new evolution path." }, { "rule": "χ\_path(\[..., x\_t\], x\_{t+1}) → \[..., x\_t, x\_{t+1}\]", "note": "Append next forward state." }, // \----------------------------------------------------------- // Continuity / Discrete Jumps // \----------------------------------------------------------- { "rule": "χ\_flow(x) → smooth(x)", "note": "Continuous update." }, { "rule": "χ\_discrete(x) → x\_jump", "constraint": "Must not violate causal coherence or Ω-consistency." }, // \----------------------------------------------------------- // Multi-tier Integration // \----------------------------------------------------------- { "rule": "χ(δ(x)) → δ(χ(x))", "note": "δ-evolution commutes with χ (local geometry evolves)." }, { "rule": "χ(ψ(x)) → ψ\_evolved", "note": "Oscillatory state decays/propagates under χ." }, { "rule": "χ(Σ(x)) → Σ(χ(x))", "note": "Contracted forms evolve uniformly." }, { "rule": "χ(Θ(x)) → Θ(x')", "note": "Routing decisions update with time." }, { "rule": "χ(Π(x)) → Π(x')", "note": "Truth evaluations occur at new semantic time." } \], // \------------------------------------------------------------- // χ Normal Forms // \------------------------------------------------------------- "normal\_forms": { "NF\_χ": "unique convergent state under repeated χ application", "NF\_χ\_path": "fully-evolved, causally-coherent path", "NF\_χ\_multi": "δ–Φ–Π–μ–λ–ψ–Σ–Θ stabilized under χ" } }  
---

# 6\. tier\_09\_module\_pack.json5

### χ Evolution Engine Modules (Reference Implementation)

json5  
Copy code  
{ // \============================================================ // χ MODULE PACK — Tier 09 // \============================================================ "modules": { "χ.step": { "input": "state x\_t", "output": "state x\_{t+1}", "pseudocode": \` function χ\_step(x): return evolve\_forward(x) \` }, "χ.flow": { "input": "state", "output": "continuously evolved state", "pseudocode": \` function χ\_flow(x): return smooth\_update(x) \` }, "χ.discrete": { "input": "state", "output": "discrete jump outcome", "pseudocode": \` function χ\_discrete(x): assert continuity\_flag\_disabled return discrete\_jump(x) \` }, "χ.path": { "input": "initial\_state \+ steps", "output": "full evolution path", "pseudocode": \` function χ\_path(x0, steps): path \= \[x0\] for i in range(steps): x0 \= χ\_step(x0) path.append(x0) return path \` }, "χ.integrate": { "input": "object with δ-Φ-Π-μ-λ-ψ-Σ-Θ structure", "output": "integrated evolved state", "pseudocode": \` function χ\_integrate(obj): return apply\_all\_tiers\_forward(obj) \` }, "χ.to\_NF": { "input": "state", "output": "χ-normal form", "pseudocode": \` function χ\_to\_NF(x): while not is\_χ\_normal(x): x \= χ\_step(x) return x \` } } }  
---

