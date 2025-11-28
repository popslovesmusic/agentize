# TIER-00 — PRIMITIVES (FOUNDATION LAYER)

### Primitive Values (Irreducible Semantic Entities)

These are the atoms of MBC-4.0. They cannot be decomposed, cannot be projected, cannot be evaluated, cannot be rewritten except by identity, and anchor every operator domain.

| Symbol | Name | Meaning |
| :---- | :---- | :---- |
| 0 | Null State | Pure stillness; absence of semantic deviation or form. |
| 1 | Unit State | Identity semantic presence; minimal non-null existence. |
| ± | Primitive Polarity | Pre-Θ polarity; distinguishes semantic direction. |
| ∞ | Unbounded Extension | Open semantic extent; no boundary. |
| ⊥ | Contradiction | Impossible configuration; semantic collapse. |
| ⊤ | Tautology | Fully consistent maximal truth-state. |

---

# JSON SCHEMAS \+ FILES

Below are all six required files for Tier-00.  
---

# 1\. tier\_00\_metadata.json

Describes Tier-0 and its purpose.  
json  
Copy code  
{ "tier": "00", "name": "Primitive Layer", "purpose": "Define irreducible semantic values that form the base domain for all operators.", "primitives": \[ {"symbol": "0", "name": "Null", "description": "Pure stillness; semantic absence."}, {"symbol": "1", "name": "Unit", "description": "Identity semantic state."}, {"symbol": "±", "name": "Polarity", "description": "Primitive positive/negative orientation."}, {"symbol": "∞", "name": "Unbounded", "description": "No semantic limit or boundary."}, {"symbol": "⊥", "name": "Contradiction", "description": "Impossible or inconsistent state."}, {"symbol": "⊤", "name": "Tautology", "description": "Maximally consistent, universal truth."} \], "immutability": true, "interacts\_with": \[\], "notes": "Tier-00 values are atomic and cannot be decomposed or rewritten except by identity." }  
---

# 2\. tier\_00\_operator\_pack.json

Tier-0 technically has no operators, but must expose a canonical null-operator environment.  
json  
Copy code  
{ "tier": "00", "operator\_pack": { "identity": { "name": "ID", "action": "Return primitive unchanged.", "domain": "Primitive", "codomain": "Primitive" }, "undefined\_operators": \[ "δ", "Φ", "Π", "μ", "ψ", "λ", "Σ", "Θ", "χ", "Ω", "ρ" \] }, "rules": { "ID(x)": "x", "Op(x)": "undefined for all non-identity operators" } }  
---

# 3\. tier\_00\_interaction\_table.json

A primitive table of how each primitive value interacts with others.  
json  
Copy code  
{ "tier": "00", "interaction\_table": { "0": { "1": "0", "±": "0", "∞": "0", "⊥": "⊥", "⊤": "0" }, "1": { "0": "0", "±": "±", "∞": "∞", "⊥": "⊥", "⊤": "1" }, "±": { "0": "0", "1": "±", "±": "⊤", "∞": "∞", "⊥": "⊥", "⊤": "±" }, "∞": { "0": "0", "1": "∞", "±": "∞", "∞": "∞", "⊥": "⊥", "⊤": "∞" }, "⊥": { "x": "⊥" }, "⊤": { "x": "x" } } }  
Notes:

* ⊥ is absorbing.  
* ⊤ is identity-propagating.  
* ∞ is idempotent.

---

# 4\. tier\_00\_axiom\_box.json

Canonical Tier-0 sealed axiom box.  
json  
Copy code  
{ "axiom\_box": { "name": "Primitive Irreducibility Axiom", "intent": "Establish the irreducible semantic atoms of IGSOA.", "domain": "Primitive Values", "constraints": \[ "Primitives cannot be rewritten by Tier-1 or higher operators.", "Primitives are closed under identity mapping.", "⊥ is absorbing under all interactions.", "⊤ is neutral under all interactions.", "∞ is idempotent: ∞ ⊗ ∞ \= ∞." \], "cross\_links": { "upstream": \[\], "downstream": \[ "Tier-1 δ Axiom Box", "Tier-2 Φ Axiom Box", "Tier-3 Π Axiom Box" \] } } }  
---

# 5\. tier\_00\_rewrite\_system.json

Rewrite rules for primitive normal forms.  
json  
Copy code  
{ "tier": "00", "rewrite\_system": { "rules": \[ {"rule": "x → x", "condition": "x is primitive"}, {"rule": "⊥ ⊗ x → ⊥"}, {"rule": "⊤ ⊗ x → x"}, {"rule": "∞ ⊗ ∞ → ∞"}, {"rule": "0 ⊗ x → 0", "except": \["⊥"\]}, {"rule": "1 ⊗ x → x"}, {"rule": "± ⊗ ± → ⊤"} \], "normal\_form": "Primitive symbols are already in irreducible form." } }  
---

# 6\. tier\_00\_module\_pack.json

The fully bundled module for Tier-0.  
json  
Copy code  
{ "tier": "00", "module\_pack": { "metadata": "tier\_00\_metadata.json", "operator\_pack": "tier\_00\_operator\_pack.json", "interaction\_table": "tier\_00\_interaction\_table.json", "axiom\_box": "tier\_00\_axiom\_box.json", "rewrite\_system": "tier\_00\_rewrite\_system.json", "exports": { "primitive\_set": \["0", "1", "±", "∞", "⊥", "⊤"\], "identity\_operator": "ID", "normal\_form": "Primitive values only", "protected": true } } }  
---

---

# ALL SIX SEALED AXIOM BOXES (Tier-00)

## 1\. 00\_\_Primitive\_0\_Box.json

json  
Copy code  
{ "axiom\_box": { "name": "Primitive 0 — Null State", "intent": "Define 0 as the irreducible semantic-null element.", "domain": "Primitive", "constraints": \[ "0 has no internal structure.", "0 is annihilating under all multiplicative-like interactions: 0 ⊗ x \= 0.", "0 is neutral under contradiction: 0 ⊗ ⊥ \= ⊥.", "No operator may reduce or expand 0.", "0 is the unique minimal semantic amplitude." \], "cross\_links": { "upstream": \[\], "downstream": \["δ Null-Action Rule", "Σ Null Contraction Rule"\] } } }  
---

## 2\. 00\_\_Primitive\_1\_Box.json

json  
Copy code  
{ "axiom\_box": { "name": "Primitive 1 — Unit State", "intent": "Define 1 as the irreducible semantic-identity element.", "domain": "Primitive", "constraints": \[ "1 is the identity: 1 ⊗ x \= x.", "1 cannot be decomposed or rewritten.", "1 preserves polarity and amplitude.", "1 interacts neutrally with ⊤: 1 ⊗ ⊤ \= 1.", "1 cannot produce ∞ or ⊥ without external operators." \], "cross\_links": { "upstream": \[\], "downstream": \["Π Identity Evaluation Rule", "Φ Identity-Preservation Projection"\] } } }  
---

## 3\. 00\_\_Primitive\_Polarity\_Box.json (for ±)

json  
Copy code  
{ "axiom\_box": { "name": "Primitive ± — Polarity Seed", "intent": "Define ± as the irreducible semantic-polarity primitive.", "domain": "Primitive", "constraints": \[ "± encodes primitive orientation before Θ-layer logic.", "± ⊗ 1 \= ±.", "± ⊗ ± \= ⊤ (primitive polarity closure).", "Polarity cannot generate contradiction unless paired with ⊥.", "± forms the base for Θ+ and Θ− channels." \], "cross\_links": { "upstream": \[\], "downstream": \["Θ Layer — Polarity Router", "Θ Logic Gate Generator"\] } } }  
---

## 4\. 00\_\_Primitive\_Infinite\_Box.json (for ∞)

json  
Copy code  
{ "axiom\_box": { "name": "Primitive ∞ — Unbounded Semantic Extent", "intent": "Define ∞ as the irreducible unlimited semantic amplitude.", "domain": "Primitive", "constraints": \[ "∞ has no upper bound: ∞ ⊗ x \= ∞ for all x except ⊥.", "∞ is idempotent: ∞ ⊗ ∞ \= ∞.", "∞ cannot be normalized without Ω-layer action.", "∞ interacts trivially with 0: 0 ⊗ ∞ \= 0.", "∞ cannot be decomposed or projected." \], "cross\_links": { "upstream": \[\], "downstream": \["Ω Constraint Layer", "λ Curvature Amplitude Limit Theorem"\] } } }  
---

## 5\. 00\_\_Primitive\_Contradiction\_Box.json (for ⊥)

json  
Copy code  
{ "axiom\_box": { "name": "Primitive ⊥ — Contradiction", "intent": "Define ⊥ as the irreducible impossible state.", "domain": "Primitive", "constraints": \[ "⊥ is absorbing: x ⊗ ⊥ \= ⊥ for all x.", "⊥ cannot be undone by any Tier-1…Tier-9 operator.", "⊥ serves as the semantic boundary of consistency.", "⊥ is fixed under projection: Φ(⊥) \= ⊥.", "⊥ induces operator collapse in χ-evolution." \], "cross\_links": { "upstream": \[\], "downstream": \["Ω Consistency Invariant", "Θ Paraconsistent Logic Rules"\] } } }  
---

## 6\. 00\_\_Primitive\_Tautology\_Box.json (for ⊤)

json  
Copy code  
{ "axiom\_box": { "name": "Primitive ⊤ — Tautology", "intent": "Define ⊤ as the irreducible maximally consistent truth-state.", "domain": "Primitive", "constraints": \[ "⊤ is neutral: ⊤ ⊗ x \= x.", "⊤ subsumes polarity: ⊤ ⊗ ± \= ±.", "⊤ cannot collapse to ⊥ under any finite operator sequence.", "⊤ forms the upper bound of semantic consistency.", "⊤ serves as normalization attractor in Ω-layer action." \], "cross\_links": { "upstream": \[\], "downstream": \["Ω Normal Form Rule", "Π Truth Evaluation Bridge"\] } } }  
---

# ✔ All primitive boxes complete

You now have:

* 6 atomic sealed boxes  
* All independent and irreducible  
* Each with unique constraints  
* Each properly cross-linked to future tiers  
* Fully MBC-4.0 compliant and machine-readable

---

###### 

---

# ✅ tier\_00\_axiom\_box.json (Master Index)

json  
Copy code  
{ "tier": "00", "layer\_name": "Primitive Layer", "type": "AxiomBox::MasterIndex", "version": "1.0.0", "intent": "Bundle all primitive sealed boxes into a single canonical Tier-00 axiom index.", "description": "This master index aggregates the six irreducible primitive entities of MBC-4.0: 0, 1, ±, ∞, ⊥, ⊤. Each primitive has its own sealed box defining its constraints, domain boundaries, and downstream operator linkages.", "primitives": \[ { "symbol": "0", "name": "Null State", "file": "00\_\_Primitive\_0\_Box.json", "sha256": "\<to-be-filled\>", "properties": { "role": "semantic-null", "absorbing": true, "decomposable": false } }, { "symbol": "1", "name": "Unit State", "file": "00\_\_Primitive\_1\_Box.json", "sha256": "\<to-be-filled\>", "properties": { "role": "semantic-identity", "decomposable": false, "preserves\_forms": true } }, { "symbol": "±", "name": "Polarity Seed", "file": "00\_\_Primitive\_Polarity\_Box.json", "sha256": "\<to-be-filled\>", "properties": { "role": "primitive-orientation", "feeds\_layer": "Θ", "decomposable": false } }, { "symbol": "∞", "name": "Unbounded Semantic Extent", "file": "00\_\_Primitive\_Infinite\_Box.json", "sha256": "\<to-be-filled\>", "properties": { "role": "semantic-unbounded", "idempotent": true, "requires\_Omega": true } }, { "symbol": "⊥", "name": "Contradiction", "file": "00\_\_Primitive\_Contradiction\_Box.json", "sha256": "\<to-be-filled\>", "properties": { "absorbing": true, "inconsistency\_boundary": true, "paraconsistent": true } }, { "symbol": "⊤", "name": "Tautology", "file": "00\_\_Primitive\_Tautology\_Box.json", "sha256": "\<to-be-filled\>", "properties": { "max\_consistency": true, "normalization\_attractor": true, "neutral": true } } \], "constraints": \[ "Tier-00 primitives must remain irreducible under all rewrite systems.", "Primitive boxes cannot be rewritten or merged.", "All operator packs from Tier-01 upward must treat primitives as atomic domain elements.", "⊥ must remain globally absorbing unless overridden by explicit paraconsistent rules.", "⊤ must remain globally neutral and consistency-maximal." \], "cross\_links": { "upstream": \[\], "downstream": \[ "tier\_01\_axiom\_box.json", "tier\_02\_axiom\_box.json", "tier\_03\_axiom\_box.json", "Tri-Unity Operator Grid", "Ω Normalization Layer" \] }, "validation": { "requires\_all\_files\_present": true, "requires\_unique\_primitives": true, "requires\_sha256\_verification": true, "notes": "Agent should regenerate SHA256 hashes on any change." } }  
---

# ✔ Master Index Complete

This file now serves as:

* the root of the entire MBC-4.0 axiom hierarchy  
* the canonical upstream dependency for δ, Φ, Π  
* the structural anchor for all rewrite systems

---

---

## Conceptual Rules (δ on primitives)

* δ(0) → 0  
  No deviation from pure stillness.  
* δ(1) → 0  
  Unit state has zero internal gradient: no deviation.  
* δ(±) → ±  
  Polarity is the first non-null deviation; δ preserves this primitive orientation.  
* δ(∞) → 0 (under Ω-regularized uniform extension)  
  Infinite but uniform extent has zero local deviation; all “points” see the same state.  
* δ(⊥) → ⊥  
  Contradiction is absorbing; deviation cannot repair or alter ⊥.  
* δ(⊤) → 0  
  Tautology is maximally consistent and uniform; no internal deviation.

---

## tier\_01\_delta\_on\_primitives.json

json  
Copy code  
{ "tier": "01", "bridge\_type": "Tier00\_to\_Tier01", "source\_layer": "Tier-00\_Primitives", "target\_layer": "Tier-01\_δ-Family", "version": "1.0.0", "intent": "Define the action of the deviation operator δ on the irreducible primitive values (0, 1, ±, ∞, ⊥, ⊤) to bridge Tier-00 primitives into the Tier-01 δ-layer.", "description": "These rules specify how the δ deviation operator acts on semantic primitives. They form the canonical bridge between Tier-00 primitive values and the Tier-01 δ-family, and are to be included as a base case in any δ-based rewrite system.", "rules": \[ { "id": "delta\_on\_null", "pattern": "δ(0)", "rewrite": "0", "semantic\_intent": "No deviation from pure stillness.", "constraints": \[ "0 has no internal structure.", "δ cannot create structure out of pure null." \], "pseudocode": "if x \== 0: return 0" }, { "id": "delta\_on\_unit", "pattern": "δ(1)", "rewrite": "0", "semantic\_intent": "Unit state has zero internal gradient.", "constraints": \[ "1 is identity for primitive interactions.", "δ measures change; identity has no internal change." \], "pseudocode": "if x \== 1: return 0" }, { "id": "delta\_on\_polarity", "pattern": "δ(±)", "rewrite": "±", "semantic\_intent": "Primitive polarity is the first non-null deviation; δ preserves this orientation.", "constraints": \[ "± encodes primitive directional difference from 0.", "δ acts as identity on pure polarity seeds." \], "pseudocode": "if x \== '±': return '±'" }, { "id": "delta\_on\_infinity", "pattern": "δ(∞)", "rewrite": "0", "semantic\_intent": "Uniform infinite extent has no local deviation; all points see the same state.", "constraints": \[ "Interpretation assumes Ω-regularized uniform infinity.", "Non-uniform infinities must be represented at higher tiers, not as primitive ∞." \], "requires\_layers": \["Ω"\], "pseudocode": "if x \== '∞': return 0 \# under Ω-regularized uniformity" }, { "id": "delta\_on\_contradiction", "pattern": "δ(⊥)", "rewrite": "⊥", "semantic\_intent": "Contradiction is absorbing; deviation cannot resolve or alter it.", "constraints": \[ "⊥ is the boundary of semantic consistency.", "No δ action can escape ⊥ without explicit paraconsistent rules at Θ/Ω tiers." \], "pseudocode": "if x \== '⊥': return '⊥'" }, { "id": "delta\_on\_tautology", "pattern": "δ(⊤)", "rewrite": "0", "semantic\_intent": "Tautology is maximally consistent and uniform; no internal deviation remains.", "constraints": \[ "⊤ is globally uniform truth.", "δ measures local change; tautology is invariant under such change." \], "pseudocode": "if x \== '⊤': return 0" } \], "normal\_form\_notes": \[ "For primitive arguments, δ always rewrites to a primitive value.", "No higher δ-structure (e.g. δᵢ, δ², δᴶ) is introduced at the primitive level.", "These rules must be applied before any Tier-01+ composite δ rules." \], "cross\_links": { "uses\_axiom\_boxes": \[ "00\_\_Primitive\_0\_Box.json", "00\_\_Primitive\_1\_Box.json", "00\_\_Primitive\_Polarity\_Box.json", "00\_\_Primitive\_Infinite\_Box.json", "00\_\_Primitive\_Contradiction\_Box.json", "00\_\_Primitive\_Tautology\_Box.json" \], "integrate\_into": \[ "tier\_01\_rewrite\_system.json", "Tri-Unity\_δ-Φ-Π\_Base\_Rewrites.json" \] } }  
---

