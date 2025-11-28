##  Primitive Evolution Entities (conceptual)

1\. χ-step — atomic semantic time increment

* Meaning: The smallest admissible positive increment of semantic time χ.  
* Role: Tags any evolution as having occurred; used as the unit of χ-measure.  
* Constraint: Indivisible; you may count multiples of χ-step, but χ-step itself is not factorized.

2\. Semantic Path Element — minimal evolution arrow

* Meaning: A single directed arrow  
* e:Sin→ χ-step Sout  
* e:S  
* in  
* ​  
* χ-step  
* ​  
* S  
* out  
* ​  
* Role: Minimal edge in the χ-evolution graph; all longer histories are concatenations of these.  
* Constraint: Must record exactly one χ-step (no zero-χ edges).

3\. Rewrite Rule Atom — indivisible rewrite

* Meaning: A primitive rewrite of the form  
* r:patternin⇒patternout  
* r:pattern  
* in  
* ​  
* ⇒pattern  
* out  
* ​  
* that fires in one χ-step.  
* Role: Basic dynamical law for symbolic state.  
* Constraint: Not decomposed into smaller rules; either fires as-is or not at all.

---

## 1\. tier\_00\_evolution\_metadata.json

json  
Copy code  
{ "tier\_id": "tier\_00\_evolution", "family": "Primitive Evolution Entities", "version": "0.1.0", "status": "draft", "description": "Tier-00 pack for primitive evolution entities: χ-step, Semantic Path Element, Rewrite Rule Atom.", "primitives": \[ { "id": "Evolution.Primitive.ChiStep", "name": "χ-step", "kind": "primitive\_evolution\_entity", "summary": "Atomic semantic time increment.", "properties": { "delta\_chi": "R+ (strictly positive minimal unit)", "label": "string (optional human-readable name)", "atomic": true } }, { "id": "Evolution.Primitive.SemanticPathElement", "name": "Semantic Path Element", "kind": "primitive\_evolution\_entity", "summary": "Minimal evolution arrow between two states in one χ-step.", "properties": { "state\_in\_ref": "BoxID or StateID", "state\_out\_ref": "BoxID or StateID", "chi\_step\_ref": "Evolution.Primitive.ChiStep", "metadata": { "tag": "string", "layer": "rho-layer index (optional)" } } }, { "id": "Evolution.Primitive.RewriteRuleAtom", "name": "Rewrite Rule Atom", "kind": "primitive\_evolution\_entity", "summary": "Indivisible rewrite (pattern\_in ⇒ pattern\_out) that fires in a single χ-step.", "properties": { "pattern\_in": "Term or PatternID", "pattern\_out": "Term or PatternID", "guard": "logical condition (Θ/Π expression)", "chi\_cost": "Evolution.Primitive.ChiStep" } } \], "depends\_on\_tiers": \[ "tier\_00\_primitive\_values", "tier\_00\_geometric", "tier\_00\_domain", "tier\_00\_logic", "tier\_00\_operators" \], "semantic\_links": { "core\_operator": "χ (Tier-9 Evolution / Semantic Time)", "tri\_unity\_axes": \["δ", "Φ", "Π"\], "augmentation\_operators": \["Σ", "Θ", "μ", "λ", "ψ", "ρ", "Ω"\] } }  
---

## 2\. tier\_00\_evolution\_operator\_pack.json

json  
Copy code  
{ "tier\_id": "tier\_00\_evolution", "pack\_name": "Primitive Evolution Operator Pack", "version": "0.1.0", "operators": \[ { "id": "Op.Chi.Advance", "symbol": "STEP\_χ", "name": "χ-step advance", "arity": 1, "input\_types": \["State"\], "output\_type": "State", "parameters": { "step": "Evolution.Primitive.ChiStep" }, "summary": "Advance a state forward by one χ-step according to active Rewrite Rule Atoms.", "chi\_effect": "χ := χ \+ χ-step", "law\_sketch": "If a RewriteRuleAtom r is applicable to State S, then STEP\_χ(S) \= S' where S' is S rewritten by r in one χ-step." }, { "id": "Op.Path.Compose", "symbol": "∘\_path", "name": "Path composition", "arity": 2, "input\_types": \[ "Evolution.Primitive.SemanticPathElement", "Evolution.Primitive.SemanticPathElement" \], "output\_type": "Evolution.Primitive.SemanticPathElement or Path", "parameters": { "compose\_mode": "enum('element','path')" }, "summary": "Compose two Semantic Path Elements when the intermediate state matches.", "constraints": \[ "path1.state\_out\_ref \= path2.state\_in\_ref", "chi\_total \= chi\_step(path1) \+ chi\_step(path2)" \], "chi\_effect": "χ := χ \+ 2·χ-step (for element-wise composition)", "law\_sketch": "Associative composition of minimal arrows; NF prefers a flat list representation of path elements." }, { "id": "Op.Rule.ApplyAtom", "symbol": "⊢ₐ", "name": "Atomic rewrite application", "arity": 2, "input\_types": \[ "Evolution.Primitive.RewriteRuleAtom", "State" \], "output\_type": "State", "parameters": { "mode": "enum('deterministic','nondeterministic')" }, "summary": "Apply one indivisible Rewrite Rule Atom to a State in a single χ-step.", "chi\_effect": "χ := χ \+ χ-step", "law\_sketch": "If guard(r,S) is Π-true and pattern\_in(r) matches S, then ⊢ₐ(r, S) \= S' with pattern\_out(r) substituted." } \] }  
---

## 3\. tier\_00\_evolution\_interaction\_table.json

Minimal interaction examples so the agent has a template.  
json  
Copy code  
{ "tier\_id": "tier\_00\_evolution", "table\_name": "Primitive Evolution Interaction Table", "version": "0.1.0", "interactions": \[ { "id": "Int.Chi.With.TriUnity", "lhs": "STEP\_χ ∘ (δ, Φ, Π)", "rhs": "(δ, Φ, Π) ∘ STEP\_χ", "interaction\_type": "commutation\_constraint", "summary": "χ-step evolution must respect Tri-Unity structure up to a controlled deformation.", "constraints": \[ "δ, Φ, Π evaluated at χ+χ-step are determined by Rewrite Rule Atoms that preserve Tri-Unity invariants", "Allowed deviation encoded as δχ-bounded curvature in λ, Ω layers." \] }, { "id": "Int.Path.Summation", "lhs": "Σ over Semantic Path Elements", "rhs": "Effective macroscopic path descriptor", "interaction\_type": "summation", "summary": "Σ contracts a collection of Semantic Path Elements into an effective path tensor.", "constraints": \[ "Σ counts χ-steps to produce total Δχ", "Σ aggregates μ-weights when present." \] }, { "id": "Int.Rule.Polarity", "lhs": "Θ ⊗ RewriteRuleAtom", "rhs": "Polarity-labeled RewriteRuleAtom", "interaction\_type": "polarity\_extension", "summary": "Polarity router Θ marks Rewrite Rule Atoms as constructive or destructive.", "constraints": \[ "Θ+ marks rule as constructive (entropy decreasing locally, if allowed by Ω).", "Θ- marks rule as dissipative / entropy increasing.", "Ω constraints can forbid certain Θ-labeled rules." \] }, { "id": "Int.Path.Wave", "lhs": "ψ ⊗ SemanticPathElement", "rhs": "Oscillatory weight on evolution arrow", "interaction\_type": "wave\_coupling", "summary": "Attach a phase / mode index to minimal evolution arrows.", "constraints": \[ "ψ encodes phase φ and frequency ω per Path Element.", "Interference defined when composing path elements with different ψ labels." \] } \] }  
---

## 4\. tier\_00\_evolution\_axiom\_box.json

(Three sealed axiom boxes, one per primitive.)  
json  
Copy code  
{ "tier\_id": "tier\_00\_evolution", "version": "0.1.0", "axiom\_boxes": \[ { "Name": "AX\_χ\_step\_Atomicity", "Intent": "Declare χ-step as the atomic, indivisible unit of semantic time.", "Domain": { "objects": \["χ", "Evolution.Primitive.ChiStep"\], "relations": \["\<", "+", "·"\], "ambient\_tiers": \["tier\_00\_primitive\_values", "tier\_09\_chi\_family"\] }, "Constraints": \[ "1. Existence: ∃ χ\_step \> 0 such that χ\_step is the minimal positive increment of χ.", "2. Atomicity: If χ\_step \= a \+ b with a,b \> 0, then a \= χ\_step or b \= χ\_step (no nontrivial factorization).", "3. Counting: Any finite Δχ \> 0 can be represented as n · χ\_step for some n ∈ ℕ.", "4. Sealed: No operator in Tier-00 may refine χ\_step into smaller semantic time units." \], "Cross-links": { "operators": \["STEP\_χ", "χΔ", "d/dχ"\], "tiers": \["tier\_09\_chi\_family", "tier\_00\_primitive\_values"\], "normal\_forms": \["Evolution-NF"\] } }, { "Name": "AX\_SemanticPathElement\_Minimality", "Intent": "Define Semantic Path Elements as minimal χ-step evolution arrows.", "Domain": { "objects": \[ "Evolution.Primitive.SemanticPathElement", "State" \], "relations": \["state\_in\_ref", "state\_out\_ref"\], "ambient\_tiers": \["tier\_00\_geometric", "tier\_00\_domain"\] }, "Constraints": \[ "1. Edge form: Each Semantic Path Element e has (state\_in\_ref(e), state\_out\_ref(e), χ\_step\_ref(e)).", "2. Minimal χ: χ\_step\_ref(e) \= χ\_step (the atomic χ increment).", "3. No splitting: If e corresponds to a path with total Δχ \= χ\_step, then e cannot be decomposed into nontrivial concatenations of shorter path elements.", "4. Path foundation: Any finite χ-evolution history can be represented as a finite ordered sequence of Semantic Path Elements.", "5. Sealed: The definition of a Semantic Path Element may only be extended by adding metadata; its core triple is fixed." \], "Cross-links": { "operators": \["∘\_path", "STEP\_χ", "Σ"\], "tiers": \["tier\_00\_geometric", "tier\_00\_domain", "tier\_09\_chi\_family"\], "normal\_forms": \["Evolution-NF", "Path-NF"\] } }, { "Name": "AX\_RewriteRuleAtom\_Indivisibility", "Intent": "Declare Rewrite Rule Atoms as indivisible χ-step rewrite actions.", "Domain": { "objects": \[ "Evolution.Primitive.RewriteRuleAtom", "Term", "Pattern", "State" \], "relations": \["⇒", "matches", "guard"\], "ambient\_tiers": \["tier\_00\_logic", "tier\_00\_primitive\_values"\] }, "Constraints": \[ "1. Atomic rewrite: A Rewrite Rule Atom r specifies (pattern\_in(r), pattern\_out(r), guard(r), χ\_cost(r) \= χ\_step).", "2. Single-step: Application of r consumes exactly one χ-step in χ.", "3. Indivisibility: r cannot be expressed as a composition r2 ∘ r1 of two Rewrite Rule Atoms that each consume χ\_step.", "4. Guarded determinism: For deterministic mode, if guard(r, S) is Π-true and pattern\_in(r) matches S, then r(S) is uniquely defined.", "5. Sealed: The internal structure of Rewrite Rule Atoms is not exposed as a composite of sub-rules in Tier-00." \], "Cross-links": { "operators": \["⊢ₐ", "STEP\_χ"\], "tiers": \["tier\_00\_logic", "tier\_09\_chi\_family"\], "normal\_forms": \["Rule-NF", "Evolution-NF"\] } } \] }  
---

## 5\. tier\_00\_evolution\_rewrite\_system.json

Core Evolution-NF rules for the primitives.  
json  
Copy code  
{ "tier\_id": "tier\_00\_evolution", "system\_name": "Evolution-NF", "version": "0.1.0", "normal\_form\_intent": "Reduce expressions involving χ-step, Semantic Path Elements, and Rewrite Rule Atoms to a canonical evolution normal form.", "rules": \[ { "name": "Rχ-CanonicalStepCounting", "kind": "normalization", "lhs\_pattern": "χ\_step \+ χ\_step \+ ... \+ χ\_step (n times)", "rhs\_pattern": "χ\_step^{(n)}", "conditions": \[ "n ∈ ℕ, n ≥ 1" \], "update\_pseudocode": \[ "input: n (integer ≥ 1)", "output: chi\_multiplied \= n \* chi\_step", "representation: encode as χ\_step^{(n)} (do NOT split χ\_step into smaller units)" \], "effects": { "chi\_representation": "compressed multiplicity form", "tri\_unity\_state": "unchanged except for χ increment" } }, { "name": "RPath-AssocFlatten", "kind": "structural", "lhs\_pattern": "(e1 ∘\_path e2) ∘\_path e3", "rhs\_pattern": "e1 ∘\_path (e2 ∘\_path e3)", "conditions": \[ "e1.state\_out\_ref \= e2.state\_in\_ref", "e2.state\_out\_ref \= e3.state\_in\_ref" \], "update\_pseudocode": \[ "input: list of Semantic Path Elements \[e1, e2, e3, ...\]", "output: flatten nested composition into a single ordered list", "NF: represent paths only as flat lists, never as nested compositions" \], "effects": { "chi\_total": "sum of chi\_step\_ref(ei)", "path\_representation": "associative, flattened" } }, { "name": "RRule-GuardedApply", "kind": "evolution\_step", "lhs\_pattern": "⊢ₐ(r, S)", "rhs\_pattern": "S'", "conditions": \[ "r is Evolution.Primitive.RewriteRuleAtom", "guard(r, S) evaluates to Π-true", "pattern\_in(r) matches S" \], "update\_pseudocode": \[ "if guard(r, S) \== TRUE and match(pattern\_in(r), S):", " S\_prime \= substitute(pattern\_out(r), S)", " χ := χ \+ χ\_step", " return S\_prime", "else:", " return S (no evolution)" \], "effects": { "state": "S' is S rewritten by r", "chi": "incremented by χ-step", "tri\_unity": "δ, Φ, Π updated according to new state S'" } }, { "name": "RPath-NF", "kind": "normalization", "lhs\_pattern": "nested or branching path expression", "rhs\_pattern": "flat ordered list of Semantic Path Elements with χ\_step^{(n)} counted", "conditions": \[ "χ\_total finite", "all edges are Semantic Path Elements" \], "update\_pseudocode": \[ "1. Expand all compositions into a multiset of Semantic Path Elements.", "2. Order them by χ (or by an explicit index).", "3. Represent repeated consecutive χ-steps as χ\_step^{(n)}.", "4. Output canonical Path NF." \], "effects": { "representation": "canonical Path NF", "chi": "unchanged total Δχ" } } \] }  
---

## 6\. tier\_00\_evolution\_module\_pack.json

Top-level bundle tying everything together for the agent.  
json  
Copy code  
{ "tier\_id": "tier\_00\_evolution", "module\_name": "PrimitiveEvolutionModulePack", "version": "0.1.0", "exports": { "primitive\_entities": \[ "Evolution.Primitive.ChiStep", "Evolution.Primitive.SemanticPathElement", "Evolution.Primitive.RewriteRuleAtom" \], "operators\_file": "tier\_00\_evolution\_operator\_pack.json", "interaction\_table\_file": "tier\_00\_evolution\_interaction\_table.json", "axiom\_box\_file": "tier\_00\_evolution\_axiom\_box.json", "rewrite\_system\_file": "tier\_00\_evolution\_rewrite\_system.json", "metadata\_file": "tier\_00\_evolution\_metadata.json" }, "ingestion\_hints": { "primitive\_tag": "primitive\_evolution\_entity", "preferred\_normal\_form": "Evolution-NF", "axiom\_box\_field\_set": \["Name", "Intent", "Domain", "Constraints", "Cross-links"\], "sealed\_axioms": \[ "AX\_χ\_step\_Atomicity", "AX\_SemanticPathElement\_Minimality", "AX\_RewriteRuleAtom\_Indivisibility" \] }, "dependencies": \[ "tier\_00\_primitive\_values", "tier\_00\_geometric", "tier\_00\_domain", "tier\_00\_logic" \], "notes": \[ "This module should be loaded before Tier-9 χ-Family to provide primitive χ semantics.", "Rewrite engines must respect Evolution-NF when scheduling χ-step updates." \] }  
---

---

# ✅ tiny\_worked\_example\_evolution.json

json  
Copy code  
{ "example\_id": "tiny\_evolution\_demo\_v1", "description": "Minimal executable example: one state, one rewrite rule atom, one χ-step, and a 3-element Semantic Path reduced to Evolution-NF.", "primitives": { "chi\_step": { "id": "chi\_step", "value": 1, "atomic": true } }, "states": { "S0": { "id": "S0", "term": "A" }, "S1": { "id": "S1", "term": "B" }, "S2": { "id": "S2", "term": "C" }, "S3": { "id": "S3", "term": "D" } }, "rewrite\_rule\_atoms": { "r1": { "id": "r1", "pattern\_in": "A", "pattern\_out": "B", "guard": "TRUE", "chi\_cost": "chi\_step" } }, "path\_elements": \[ { "id": "e1", "state\_in": "S0", "state\_out": "S1", "chi\_step": "chi\_step", "description": "Apply r1: A ⇒ B" }, { "id": "e2", "state\_in": "S1", "state\_out": "S2", "chi\_step": "chi\_step", "description": "Manual transition B ⇒ C" }, { "id": "e3", "id\_alias": "final\_step", "state\_in": "S2", "state\_out": "S3", "chi\_step": "chi\_step", "description": "Manual transition C ⇒ D" } \], "semantic\_path": { "raw\_composed": "((e1 ∘\_path e2) ∘\_path e3)", "elements": \["e1", "e2", "e3"\], "total\_steps": 3, "total\_delta\_chi": "3 \* chi\_step" }, "execution\_trace": \[ { "step\_index": 1, "path\_element": "e1", "input\_state": "S0", "action": "RewriteRule r1 applied", "result\_state": "S1", "chi\_increment": 1, "chi\_total": 1 }, { "step\_index": 2, "path\_element": "e2", "input\_state": "S1", "action": "Manual transition", "result\_state": "S2", "chi\_increment": 1, "chi\_total": 2 }, { "step\_index": 3, "path\_element": "e3", "input\_state": "S2", "action": "Manual transition", "result\_state": "S3", "chi\_increment": 1, "chi\_total": 3 } \], "normal\_form\_reduction": { "before": { "representation": "((e1 ∘\_path e2) ∘\_path e3)" }, "rewrite\_rules\_applied": \[ "RPath-AssocFlatten : nested \-\> flat list", "Rχ-CanonicalStepCounting : χ\_step \+ χ\_step \+ χ\_step \-\> χ\_step^{(3)}" \], "after": { "canonical\_path\_nf": { "elements": \["e1", "e2", "e3"\], "chi\_total": "χ\_step^{(3)}", "state\_start": "S0", "state\_end": "S3" } } } }  
---

# ✅ Explanation of the tiny example

### 1\. Initial state

yaml  
Copy code  
S0 : A

### 2\. Rewrite Rule Atom

r₁ rewrites:  
css  
Copy code  
A  ⇒  B    in one χ-step

### 3\. Path Elements

Three consecutive χ-step transitions:  
makefile  
Copy code  
e1: S0 → S1   (A → B)  
e2: S1 → S2   (B → C)  
e3: S2 → S3   (C → D)

### 4\. Execution

* After e1: χ \= 1  
* After e2: χ \= 2  
* After e3: χ \= 3

### 5\. Normal Form

The raw nested path:  
scss  
Copy code  
((e1 ∘ e2) ∘ e3)

reduces to the Evolution-NF:  
csharp  
Copy code  
\[e1, e2, e3\]   with total χ \= χ\_step³

---

---

# tiny\_worked\_example\_evolution\_plus\_labels.json

json  
Copy code  
{ "example\_id": "tiny\_evolution\_demo\_v2", "description": "Expanded tiny example with polarity Θ± on r1 and ψ/μ/λ labels added to each Semantic Path Element.", "primitives": { "chi\_step": { "id": "chi\_step", "value": 1, "atomic": true } }, "states": { "S0": { "id": "S0", "term": "A" }, "S1": { "id": "S1", "term": "B" }, "S2": { "id": "S2", "term": "C" }, "S3": { "id": "S3", "term": "D" } }, "rewrite\_rule\_atoms": { "r1": { "id": "r1", "pattern\_in": "A", "pattern\_out": "B", "guard": "TRUE", "chi\_cost": "chi\_step", "polarity": { "Theta": "Θ+", "intent": "constructive evolution step (entropy-lowering or structure-building)" } } }, "path\_elements": \[ { "id": "e1", "state\_in": "S0", "state\_out": "S1", "chi\_step": "chi\_step", "description": "Apply r1: A ⇒ B", "psi": { "phase": 0.0, "frequency": 1.0, "mode\_label": "ψ₁" }, "mu": { "weight": 1.0, "adjacency\_factor": 0.95 }, "lambda": { "curvature": 0.01, "deformation\_mode": "λᶜᵘʳᵛ" } }, { "id": "e2", "state\_in": "S1", "state\_out": "S2", "chi\_step": "chi\_step", "description": "Manual transition B ⇒ C", "psi": { "phase": 0.5, "frequency": 1.0, "mode\_label": "ψ₁" }, "mu": { "weight": 0.9, "adjacency\_factor": 0.90 }, "lambda": { "curvature": 0.03, "deformation\_mode": "λˣ" } }, { "id": "e3", "id\_alias": "final\_step", "state\_in": "S2", "state\_out": "S3", "chi\_step": "chi\_step", "description": "Manual transition C ⇒ D", "psi": { "phase": 1.0, "frequency": 1.0, "mode\_label": "ψ₁" }, "mu": { "weight": 0.85, "adjacency\_factor": 0.88 }, "lambda": { "curvature": 0.05, "deformation\_mode": "λᵐᵒᵈᵉ" } } \], "semantic\_path": { "raw\_composed": "((e1 ∘\_path e2) ∘\_path e3)", "elements": \["e1", "e2", "e3"\], "total\_steps": 3, "total\_delta\_chi": "3 \* chi\_step", "aggregated\_labels": { "psi\_combined": { "net\_phase": 1.5, "dominant\_frequency": 1.0 }, "mu\_combined": { "effective\_weight": 0.9, "effective\_adjacency": 0.91 }, "lambda\_combined": { "total\_curvature": 0.09 } } }, "execution\_trace": \[ { "step\_index": 1, "path\_element": "e1", "input\_state": "S0", "action": "RewriteRule r1 (Θ+ constructive polarity)", "result\_state": "S1", "psi": { "phase": 0.0, "frequency": 1.0 }, "mu": { "weight": 1.0 }, "lambda": { "curvature": 0.01 }, "chi\_increment": 1, "chi\_total": 1 }, { "step\_index": 2, "path\_element": "e2", "input\_state": "S1", "action": "Manual transition B ⇒ C", "psi": { "phase": 0.5, "frequency": 1.0 }, "mu": { "weight": 0.9 }, "lambda": { "curvature": 0.03 }, "result\_state": "S2", "chi\_increment": 1, "chi\_total": 2 }, { "step\_index": 3, "path\_element": "e3", "input\_state": "S2", "action": "Manual transition C ⇒ D", "psi": { "phase": 1.0, "frequency": 1.0 }, "mu": { "weight": 0.85 }, "lambda": { "curvature": 0.05 }, "result\_state": "S3", "chi\_increment": 1, "chi\_total": 3 } \], "normal\_form\_reduction": { "before": { "representation": "((e1 ∘\_path e2) ∘\_path e3)" }, "rewrite\_rules\_applied": \[ "RPath-AssocFlatten", "Rχ-CanonicalStepCounting" \], "after": { "canonical\_path\_nf": { "elements": \["e1", "e2", "e3"\], "chi\_total": "χ\_step^{(3)}", "state\_start": "S0", "state\_end": "S3", "combined\_labels": { "psi": { "net\_phase": 1.5, "dominant\_frequency": 1.0 }, "mu": { "effective\_weight": 0.9, "effective\_adjacency": 0.91 }, "lambda": { "total\_curvature": 0.09 } } } } } }  
---

# 🔍 What was added?

## 1\. Polarity Θ on the Rewrite Rule Atom

json  
Copy code  
"polarity": { "Theta": "Θ+", "intent": "constructive evolution step" }  
This tags r₁ as structure-building.

## 2\. ψ-labels per path element

Each has:

* phase  
* frequency  
* mode label

Used for wave interference in evolution.

## 3\. μ-labels per path element

Each has:

* local weight  
* adjacency factor

Used for local geometry / metric density.

## 4\. λ-labels per path element

Each has:

* curvature  
* deformation mode

Used for δ/λ-coupled curvature dynamics.  
---

