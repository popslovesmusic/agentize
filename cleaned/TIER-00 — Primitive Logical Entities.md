#  TIER-00 — Primitive Logical Entities

(Truth Atom • Polarity Atom • Semantic Class Atom • Deviation Atom)  
Each primitive receives:

### ✔ A formal definition

### ✔ A sealed axiom box (machine-readable JSON)

### ✔ A 6-file Tier-00 bundle

### ✔ A minimal interaction & rewrite system

Everything is written in MBC-4.0 canonical format.  
---

# \----------------------------------------------

# 0\. DEFINITIONS (Concise & Formal)

# \----------------------------------------------

## 1\. Truth Atom (Π-core state)

The irreducible semantic evaluation unit.  
Represents the smallest possible truth-bearing particle in Π-evaluation.  
It is primitive: cannot be decomposed into logical gates or projections.  
bash  
Copy code  
TruthAtom := atomic Π-state ∈ {⊤, ⊥, U}  
where U \= undefined / unprojected truth

---

## 2\. Polarity Atom (Θ-core state)

The irreducible polarity bit used by Θ-router.  
Encodes direction of semantic influence.  
css  
Copy code  
PolarityAtom := atomic Θ-state ∈ {+, −, 0}

---

## 3\. Semantic Class Atom (Φ-core class)

The minimal projection-class unit for Φ-projection.  
Represents the smallest distinguishable semantic form/class.  
kotlin  
Copy code  
SemanticClassAtom := atomic Φ-class label cᵢ (undecomposable)

---

## 4\. Deviation Atom (δ-core local displacement)

The smallest unit of geometric/semantic deviation.  
cpp  
Copy code  
DeviationAtom := atomic δ-vector element dᵢ

---

# \----------------------------------------------

# 1\. SEALED AXIOM BOXES (One per primitive)

# \----------------------------------------------

All sealed boxes follow your 5-field standard:  
json  
Copy code  
{  
  "name": "",  
  "intent": "",  
  "domain": "",  
  "constraints": {},  
  "cross\_links": {}  
}

---

## A. Sealed Axiom Box — Truth Atom

json  
Copy code  
{ "name": "TruthAtom\_Axiom", "intent": "Define the irreducible Π-core truth state.", "domain": "Primitive Logical Entities / Π", "constraints": { "values": \["⊤", "⊥", "U"\], "indivisible": true, "closed\_under\_Pi": \["Π(⊤)=⊤", "Π(⊥)=⊥"\], "undefined\_behavior": "Π(U)=U" }, "cross\_links": { "Theta": "Θ determines polarity-routing for truth propagation.", "Phi": "Φ can reclassify truth domains.", "Delta": "δ modifies truth by local displacement of evaluation context." } }  
---

## B. Sealed Axiom Box — Polarity Atom

json  
Copy code  
{ "name": "PolarityAtom\_Axiom", "intent": "Define the irreducible Θ-core polarity state.", "domain": "Primitive Logical Entities / Θ", "constraints": { "values": \["+", "-", "0"\], "indivisible": true, "opposite\_map": { "+": "-", "-": "+", "0": "0" }, "neutral\_behavior": "0 is polarity vacuum" }, "cross\_links": { "Pi": "Polarity modifies evaluation routing.", "Phi": "Polarity may reorient semantic class selection.", "Delta": "δ may flip polarity under local curvature." } }  
---

## C. Sealed Axiom Box — Semantic Class Atom

json  
Copy code  
{ "name": "SemanticClassAtom\_Axiom", "intent": "Define the irreducible Φ-core semantic class label.", "domain": "Primitive Logical Entities / Φ", "constraints": { "class\_set": "Finite or countably infinite {c\_i}", "indivisible": true, "projection\_rule": "Φ(c\_i)=c\_i" }, "cross\_links": { "Pi": "Π may evaluate class membership.", "Theta": "Polarity selects class orientation.", "Delta": "δ perturbs class alignment locally." } }  
---

## D. Sealed Axiom Box — Deviation Atom

json  
Copy code  
{ "name": "DeviationAtom\_Axiom", "intent": "Define the irreducible δ-core displacement unit.", "domain": "Primitive Logical Entities / δ", "constraints": { "basis": "d\_i is element of δ-basis", "indivisible": true, "linearity": "δ(a d\_i \+ b d\_j) \= a δ(d\_i) \+ b δ(d\_j)" }, "cross\_links": { "Pi": "Propagation of truth depends on δ-displacement.", "Theta": "δ may flip polarity under curvature.", "Phi": "δ shifts semantic projection domains." } }  
---

# \----------------------------------------------

# 2\. TIER-00 — 6 FILES (FULL PACKAGE)

# \----------------------------------------------

Below is the exact Tier-00 folder with all 6 items.  
---

# 1\. tier\_00\_metadata.json

json  
Copy code  
{ "tier": "00", "name": "Primitive Logical Entities", "entities": \[ "TruthAtom", "PolarityAtom", "SemanticClassAtom", "DeviationAtom" \], "description": "Tier-00 defines the irreducible logical-semantic atoms for MBC-4.0.", "version": "1.0" }  
---

# 2\. tier\_00\_operator\_pack.json

Only primitive operators appear:  
json  
Copy code  
{ "TruthAtom": { "Pi": "identity evaluation", "Theta": "polarity-conditioned routing", "Phi": "semantic domain projection", "Delta": "local context displacement" }, "PolarityAtom": { "Theta": "identity", "flip": "Θ(+)=−, Θ(−)=+, Θ(0)=0" }, "SemanticClassAtom": { "Phi": "identity projection", "Delta": "class deformation under displacement" }, "DeviationAtom": { "Delta": "atomic displacement generator", "Phi": "projection domain shift" } }  
---

# 3\. tier\_00\_interaction\_table.json

(Minimal atomic interactions)  
json  
Copy code  
{ "TruthAtom": { "Theta": "Polarity gates truth", "Phi": "Truth projected into class domain", "Delta": "Truth shifted by deviation context" }, "PolarityAtom": { "Pi": "Evaluation is polarity-routed", "Delta": "Deviation may flip polarity" }, "SemanticClassAtom": { "Pi": "Evaluation of class membership", "Theta": "Polarity selects class orientation" }, "DeviationAtom": { "Theta": "Polarity changes under δ-curvature", "Phi": "Class shifts under displacement" } }  
---

# 4\. tier\_00\_axiom\_box.json (Master Bundle)

json  
Copy code  
{ "TruthAtom": { "$ref": "TruthAtom\_Axiom" }, "PolarityAtom": { "$ref": "PolarityAtom\_Axiom" }, "SemanticClassAtom": { "$ref": "SemanticClassAtom\_Axiom" }, "DeviationAtom": { "$ref": "DeviationAtom\_Axiom" } }  
---

# 5\. tier\_00\_rewrite\_system.json

json  
Copy code  
{ "rules": \[ { "pattern": "Pi(TruthAtom\[x\])", "rewrite": "x" }, { "pattern": "Theta(PolarityAtom\[x\])", "rewrite": "x" }, { "pattern": "Phi(SemanticClassAtom\[c\])", "rewrite": "c" }, { "pattern": "Delta(DeviationAtom\[d\])", "rewrite": "d" }, { "pattern": "Delta(TruthAtom\[x\])", "rewrite": "TruthAtom\[x\]' // context-shifted truth" }, { "pattern": "Delta(PolarityAtom\[x\])", "rewrite": "Theta\_flip(x)" }, { "pattern": "Delta(SemanticClassAtom\[c\])", "rewrite": "c' // shifted semantic class" } \] }  
---

# 6\. tier\_00\_module\_pack.json

json  
Copy code  
{ "module": "Tier-00 Primitive Logical Entities", "includes": \[ "tier\_00\_metadata.json", "tier\_00\_operator\_pack.json", "tier\_00\_interaction\_table.json", "tier\_00\_axiom\_box.json", "tier\_00\_rewrite\_system.json" \], "usage": { "purpose": "Foundation for all higher-tier logic, geometry, evaluation, and routing.", "dependencies": \[\], "export": \[ "TruthAtom", "PolarityAtom", "SemanticClassAtom", "DeviationAtom" \] } }  
---

# \----------------------------------------------

