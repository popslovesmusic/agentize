##  Semantic Form Invariants (Φ) — Conceptual

We lock in that Φ never “lies” about class, and that once you go Φ then Π, you get the same answer as if Π “looks through” Φ.

### Core Invariants

1. Class Preservation Invariant

Φ-projection may not produce undefined or inconsistent semantic classes.  
Informal: if an object lives in a well-defined semantic class, Φ must send it into a valid, declared class; it cannot generate “class noise” or contradictions.

2. Projection–Evaluation Consistency Invariant

For any object where both exist, Φ followed by Π gives the same truth/evaluation as Π acting directly (up to NF).  
Formally: for any admissible state   
x  
x,  
Π(Φ(x))=Π(x)  
Π(Φ(x))=Π(x)  
in normal form, whenever both sides are defined.  
---

### Dual-Column Snapshot (for the textbook)

| IGSOA / MBC-4.0 Side | Standard Math / CS Analogy |
| :---- | :---- |
| Semantic Carrier: A Box state  B B has a semantic class tag class\_id in Φ-layer metadata. | A typed term t : C in a typed λ-calculus or a value with a schema tag in a type system. |
| Φ-Projection:  Φ(B) Φ(B) extracts/aligns the semantic shape of  B B into a canonical class representative. | A projection proj\_C(t) that forgets implementation details and keeps only interface/type-level structure. |
| Class Preservation Invariant: If class\_id was valid before Φ, the post-Φ class\_id' must be in the same declared class lattice and not undefined or ⊥. | Type preservation theorem: if Γ ⊢ t : C and t → t', then Γ ⊢ t' : C (no “falling out” of the type system). |
| Projection–Evaluation Consistency:  Π(Φ(B))=Π(B) Π(Φ(B))=Π(B) in NF. | Evaluation commutes with type-projection: interpreting a value’s semantics does not depend on whether you first normalize its type/shape. |

---

## 2\. tier\_02\_metadata.json5

json5  
Copy code  
{ // \======================================================================== // TIER 02 — SEMANTIC FORM INVARIANTS (Φ-FAMILY) // \======================================================================== tier: 2, name: "Semantic Form Invariants (Φ)", family: "Φ", version: "0.1.0", status: "draft", description: "Tier-02 defines invariants governing Φ-based semantic form projection, ensuring class preservation and Φ–Π consistency.", invariants: \[ { id: "PHI\_INV\_01\_CLASS\_PRESERVATION", name: "Class Preservation Invariant", summary: "Φ-projection may not produce undefined or inconsistent semantic classes.", }, { id: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", name: "Projection–Evaluation Consistency", summary: "For admissible states, Π∘Φ agrees with Π up to normal form.", }, \], // Related tiers this builds on dependencies: { // Primitive values / logic / structure tiers: \[0, 1\], // primitives \+ δ-family notes: "Assumes Tier-00 primitive values and Tier-01 δ-Family deviation operators are already defined.", }, file\_manifest: \[ "tier\_02\_metadata.json5", "tier\_02\_operator\_pack.json5", "tier\_02\_interaction\_table.json5", "tier\_02\_axiom\_box.json5", "tier\_02\_rewrite\_system.json5", "tier\_02\_module\_pack.json5", \], }  
---

## 3\. tier\_02\_operator\_pack.json5

json5  
Copy code  
{ // \======================================================================== // TIER 02 — Φ OPERATOR PACK (SEMANTIC FORM \+ INVARIANT CHECKS) // \======================================================================== meta: { tier: 2, family: "Φ", module: "tier\_02\_operator\_pack", version: "0.1.0", }, // Core Φ operators: keep consistent with your global Φ-Family definitions. operators: { "Φ": { id: "OP\_PHI\_BASE", kind: "projection", arity: 1, signature: "Box \-\> Box", description: "Canonical semantic-form projection on Boxes.", preserves: \["class\_id", "semantic\_domain"\], }, "Φ\_s": { id: "OP\_PHI\_SEMANTIC", kind: "projection", arity: 1, signature: "Box \-\> Box", description: "Projection onto pure semantic-form component (shape without evaluation).", preserves: \["semantic\_shape"\], }, "Φ\_c": { id: "OP\_PHI\_CAUSAL", kind: "projection", arity: 1, signature: "Box \-\> Box", description: "Causal-form projection (Φ-branch aligned with causal structure).", preserves: \["causal\_class"\], }, "Φ\*": { id: "OP\_PHI\_ADJOINT", kind: "adjoint\_projection", arity: 1, signature: "Box \-\> Box", description: "Adjoint to Φ; reconstructs a canonical preimage (if it exists).", }, "Φ⊕": { id: "OP\_PHI\_SUM", kind: "projection\_composite", arity: 2, signature: "Box × Box \-\> Box", description: "Semantic sum of projections; combines compatible semantic classes.", }, "Φ→Π": { id: "OP\_PHI\_TO\_PI\_BRIDGE", kind: "bridge", arity: 1, signature: "Box \-\> TruthValue", description: "Bridge composition Π∘Φ as a single operator for evaluation.", notes: "Subject to Projection–Evaluation Consistency invariant.", }, }, // Invariant checkers exposed as pseudo-operators invariant\_checks: { "checkClassPreservation": { id: "INVCHK\_PHI\_CLASS", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", input: "Box", output: "Bool", description: "Returns true iff Φ-projection leaves Box in a valid, defined semantic class.", }, "checkProjEvalConsistency": { id: "INVCHK\_PHI\_PROJ\_EVAL", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", input: "Box", output: "Bool", description: "Returns true iff Π(Φ(B)) \== Π(B) in normal form for admissible Box B.", }, }, }  
---

## 4\. tier\_02\_interaction\_table.json5

json5  
Copy code  
{ // \======================================================================== // TIER 02 — Φ INTERACTION TABLE (FOCUSED ON INVARIANTS) // \======================================================================== meta: { tier: 2, family: "Φ", module: "tier\_02\_interaction\_table", version: "0.1.0", }, // Each entry describes how Φ interacts with another family, w.r.t invariants. interactions: \[ { id: "PHI\_INT\_01\_PHI\_WITH\_DELTA", lhs: "δ ∘ Φ", rhs: "Φ ∘ δ", relation: "commutes\_on\_class\_preserving\_subspace", invariant\_guard: "PHI\_INV\_01\_CLASS\_PRESERVATION", description: "On states with invariant-preserving δ, semantic form projection commutes with deviation.", }, { id: "PHI\_INT\_02\_PHI\_WITH\_PI", lhs: "Π ∘ Φ", rhs: "Π", relation: "equal\_in\_NF", invariant\_guard: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", description: "Evaluation Π is invariant under prior Φ-projection on admissible states.", }, { id: "PHI\_INT\_03\_PHI\_CLASS\_SUM", lhs: "Φ ⊕ Φ", rhs: "Φ ∘ Σ", relation: "refinement", invariant\_guard: "PHI\_INV\_01\_CLASS\_PRESERVATION", description: "Classwise sum of projections refines to a single projection after Σ-contraction, provided classes are compatible.", }, { id: "PHI\_INT\_04\_PHI\_STAR", lhs: "Φ\* ∘ Φ", rhs: "Id\_on\_semantic\_class", relation: "partial\_identity", invariant\_guard: "PHI\_INV\_01\_CLASS\_PRESERVATION", description: "Adjoint projection reconstructs a canonical representative within the same semantic class.", }, \], }  
---

## 5\. tier\_02\_axiom\_box.json5 (Sealed Axiom Box)

json5  
Copy code  
{ // \======================================================================== // TIER 02 — Φ SEMANTIC FORM INVARIANTS (SEALED AXIOM BOX) // \======================================================================== meta: { tier: 2, family: "Φ", module: "tier\_02\_axiom\_box", version: "0.1.0", sealed: true, // This box is not to be rewritten by lower tiers. }, context: { domain: "Semantic Form / Projection Layer", carriers: \["Box", "SemanticClass", "TruthValue"\], references: \["tier\_00\_axiom\_box.json5", "tier\_01\_axiom\_box.json5"\], }, axioms: \[ { id: "AX\_PHI\_01\_CLASS\_PRESERVATION", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", name: "Class Preservation Axiom", statement: \` For every Box B with well-defined semantic class C(B), let Φ(B) be the semantic-form projection. Then C(Φ(B)) is defined and belongs to the declared semantic-class lattice. No application of Φ may yield an undefined or contradictory class (⊥). \`, formal\_schema: { // C : Box \-\> SemanticClass ∪ {⊥} for\_all: "B ∈ Box", require: "C(B) ≠ ⊥", assert: "C(Φ(B)) ≠ ⊥ ∧ C(Φ(B)) ∈ L\_semantic\_classes", }, }, { id: "AX\_PHI\_02\_PROJ\_EVAL\_CONSISTENCY", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", name: "Projection–Evaluation Consistency Axiom", statement: \` For every admissible Box B, whenever Π(B) and Π(Φ(B)) are both defined, they coincide up to normal form: NF(Π(Φ(B))) \= NF(Π(B)). \`, formal\_schema: { for\_all: "B ∈ Box\_admissible", require: "Π(B) defined ∧ Π(Φ(B)) defined", assert: "NF(Π(Φ(B))) \= NF(Π(B))", }, }, \], diagrams: { // Simple commuting square: Φ then Π vs Π directly. commuting\_square\_ascii: \` B \--Φ--\> Φ(B) | | Π| |Π v v Π(B) \== Π(Φ(B)) (in NF) \`, }, }  
---

## 6\. tier\_02\_rewrite\_system.json5

json5  
Copy code  
{ // \======================================================================== // TIER 02 — Φ REWRITE SYSTEM (ENFORCING INVARIANTS) // \======================================================================== meta: { tier: 2, family: "Φ", module: "tier\_02\_rewrite\_system", version: "0.1.0", }, // Patterns are schematic; your agent can refine them into concrete rule engines. rules: \[ // \--------------------------------------------------------- // R1: Class Preservation Repair // \--------------------------------------------------------- { id: "PHI\_RW\_01\_CLASS\_REPAIR", target\_invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", pattern: "B \-\> Φ(B)", precondition: "C(B) ≠ ⊥ ∧ C(Φ(B)) \= ⊥", action: \` SUBSTITUTE C(Φ(B)) with nearest-valid class in lattice L\_semantic\_classes or flag Box as INVALID\_CLASS\_ERROR if no such class exists. \`, ensures: "C(Φ(B')) ≠ ⊥", notes: "B' is the repaired Box after class re-alignment.", }, // \--------------------------------------------------------- // R2: Project-Then-Eval Normalization // \--------------------------------------------------------- { id: "PHI\_RW\_02\_PHI\_PI\_NF", target\_invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", pattern: "Π(Φ(B))", precondition: "Π(B) defined ∧ Π(Φ(B)) defined", action: \` REWRITE Π(Φ(B)) \=\> NF(Π(B)) // agent computes Π(B), then normalizes to canonical truth NF. \`, ensures: "NF(Π(Φ(B))) \= NF(Π(B))", }, // \--------------------------------------------------------- // R3: Illegal Φ-Projection Guard // \--------------------------------------------------------- { id: "PHI\_RW\_03\_ILLEGAL\_PHI", target\_invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", pattern: "Φ(B)", precondition: "C(B) \= ⊥", action: \` REWRITE Φ(B) \=\> ⊥\_PhiDomain // Φ is undefined on Boxes without valid semantic class. \`, ensures: "Domain error is explicit and not silently propagated.", }, // \--------------------------------------------------------- // R4: Φ–δ Commutation on Stable Classes // \--------------------------------------------------------- { id: "PHI\_RW\_04\_DELTA\_PHI\_COMMUTE", target\_invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", pattern: "δ(Φ(B))", precondition: "δ preserves C(B) and Φ is defined on B and δ(B)", action: \` REWRITE δ(Φ(B)) \=\> Φ(δ(B)) // enforce commutation where class-preserving δ makes it safe. \`, ensures: "Semantic class remains consistent along δ–Φ path.", }, \], }  
---

## 7\. tier\_02\_module\_pack.json5

json5  
Copy code  
{ // \======================================================================== // TIER 02 — SEMANTIC FORM INVARIANTS MODULE PACK (Φ) // \======================================================================== meta: { tier: 2, family: "Φ", module: "tier\_02\_module\_pack", version: "0.1.0", }, includes: \[ "tier\_02\_metadata.json5", "tier\_02\_operator\_pack.json5", "tier\_02\_interaction\_table.json5", "tier\_02\_axiom\_box.json5", "tier\_02\_rewrite\_system.json5", \], exports: { invariants: \[ "PHI\_INV\_01\_CLASS\_PRESERVATION", "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", \], operators: \[ "Φ", "Φ\_s", "Φ\_c", "Φ\*", "Φ⊕", "Φ→Π", "checkClassPreservation", "checkProjEvalConsistency", \], test\_suites: \[ { id: "T2-PHI-INV-CP-001", target\_invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", description: "Verify that Φ never produces undefined class for valid-class Boxes.", }, { id: "T2-PHI-INV-PE-001", target\_invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", description: "Verify Π∘Φ and Π agree in NF on admissible Boxes.", }, \], }, // Hook for your agent: how to run Tier-02 checks. agent\_integration: { pipeline: \[ "load tier\_02\_operator\_pack", "load tier\_02\_axiom\_box", "load tier\_02\_rewrite\_system", "run test\_suites on sample Boxes", \], notes: "This pack can be used as a Φ-layer guardrail for any higher-tier Box-processing agent.", }, }  
---

---

# ✅ TINY WORKED Φ-INVARIANT EXAMPLE

This example uses:

* One initial Box B0  
* One Φ-projection  
* One rewrite rule PHI\_RW\_01\_CLASS\_REPAIR  
* One final Invariant-Safe NF Box

---

# 1\. Initial Invalid Box (B0.json5)

B0 has a semantic class that is formally declared ("vector"),  
BUT one attribute is corrupted (dim: \-3, which violates Tier-00 primitive constraints).  
This makes it an illegal instance of class "vector".  
json5  
Copy code  
{ id: "B0", class\_id: "vector", payload: { dim: \-3, // violates primitive constraints: dimension must be \>= 1 values: \[2, 4\] // length mismatch with invalid dimension } }  
This Box has a declared class, but it fails class validation.  
So C(B0) ≠ ⊥, but B0 is not a valid representative of "vector".  
---

# 2\. Naïve Φ-Projection Output

Your Φ-operator attempts to project onto semantic class "vector":  
json5  
Copy code  
{ id: "Φ(B0)", class\_id: "undefined", // \<-- Φ produced an undefined class (violation) payload: null }  
This violates:

### PHI\_INV\_01 — Class Preservation Invariant

Φ-projection may not produce undefined semantic classes.  
---

# 3\. Tier-02 Rewrite System Repair Rule Applied

Rule (from earlier):

### PHI\_RW\_01\_CLASS\_REPAIR

json5  
Copy code  
{ id: "PHI\_RW\_01\_CLASS\_REPAIR", pattern: "B \-\> Φ(B)", precondition: "C(B) ≠ ⊥ ∧ C(Φ(B)) \= ⊥", action: " SUBSTITUTE C(Φ(B)) with nearest-valid class in L\_semantic\_classes or flag Box as INVALID\_CLASS\_ERROR if no such class exists. ", ensures: "C(Φ(B')) ≠ ⊥" }  
---

## 3A. Determining the repair target

We check possible classes in your L\_semantic\_classes:  
Example lattice (minimal):  
cpp  
Copy code  
scalar  
vector  
tensor  
form

The nearest valid class to "vector" that can accept a degenerate or malformed payload is:  
✔ "vector" (itself)  
because Tier-00 allows repair by:

* Fixing negative dimension  
* Rebuilding payload to match corrected dimension

---

# 4\. Invariant-Safe Repaired Projection

We repair Φ(B0):

* Choose class "vector"  
* Fix payload:  
  * set dim \= 2 because payload has 2 elements  
  * keep values \[2,4\] because these are consistent

### Final Repaired Box (Φ(B0)')

json5  
Copy code  
{ id: "Φ(B0)'", class\_id: "vector", payload: { dim: 2, values: \[2, 4\] }, provenance: { repaired\_from: "Φ(B0)", repair\_rule: "PHI\_RW\_01\_CLASS\_REPAIR" } }  
This Box now satisfies:

* C(Φ(B0)') \!= ⊥  
* Fits lattice definition of "vector"  
* Ready for evaluation Π  
* Ready for further δ / ψ / Σ / Θ flows

---

# 5\. Verification Step (Agent Test-Suite)

Your Tier-02 T2-PHI-INV-CP-001 test case would check:  
json5  
Copy code  
{ test\_id: "T2-PHI-INV-CP-001", input: "B0", result\_before: "class(undefined)", result\_after: "class(vector)", invariant\_satisfied: true }  
And the evaluation consistency is preserved:  
vbnet  
Copy code  
Π(Φ(B0)') \= Π(B0)  in NF

because:

* Π(B0) normalizes the malformed vector  
* Π(Φ(B0)') evaluates the corrected vector  
* Both return the same normalized truth/evaluation

---

# 6\. Fully Bundled Worked Example File

(You can drop this into your repo)  
json5  
Copy code  
{ example\_id: "T2\_PHI\_INVARIANT\_EXAMPLE\_01", initial\_box: { id: "B0", class\_id: "vector", payload: { dim: \-3, values: \[2, 4\] } }, naive\_phi\_output: { id: "Φ(B0)", class\_id: "undefined", payload: null }, applied\_rewrite\_rule: "PHI\_RW\_01\_CLASS\_REPAIR", repaired\_phi\_output: { id: "Φ(B0)'", class\_id: "vector", payload: { dim: 2, values: \[2, 4\] }, provenance: { repaired\_from: "Φ(B0)", repair\_rule: "PHI\_RW\_01\_CLASS\_REPAIR" } }, invariant\_checks: { PHI\_INV\_01\_CLASS\_PRESERVATION: true, PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY: true } }  
---

# ✔ Ready for Regression Use

This example is now:

* Minimal  
* Formal  
* Directly executable  
* Serves as the canonical demonstration of how Tier-02 Φ-Invariant logic catches and repairs semantic-class violations.

---

---

# ✅ MULTI-STEP δ–Φ–Π EVOLUTION WITH INVARIANT BREAK \+ REPAIR

### (Worked Example \+ Full JSON5)

---

# STORY OVERVIEW (Human-readable)

We start with a valid Box B0:  
perl  
Copy code  
vector (dim=3, values=\[1,2,3\])

Sequence of operations:

1. δ acts and breaks the class (dim=3 → dim=4 but payload still length 3\)  
2. Φ acts and produces an undefined class (⊥) → violates Φ-Invariant-01  
3. Tier-02 rewrite repairs Φ, producing a valid class again  
4. Π applied directly to B1  
5. Π applied after Φ(B1)'  
6. Tier-02 enforces Π∘Φ \= Π, repairing any mismatch

At the end, everything is in Invariant-Safe Normal Form.  
---

# \============================================

# ✅ MACHINE-READABLE JSON5 SIMULATION FILE

# \============================================

Save as:  
T2\_multi\_step\_phi\_delta\_pi\_example.json5  
json5  
Copy code  
{ example\_id: "T2\_MULTI\_STEP\_DELTA\_PHI\_PI\_01", //------------------------------------------------------------ // STEP 0 — INITIAL VALID BOX //------------------------------------------------------------ step0\_initial\_box: { id: "B0", class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] } }, //------------------------------------------------------------ // STEP 1 — APPLY δ (δ introduces inconsistency) //------------------------------------------------------------ step1\_apply\_delta: { operator: "δ", input: "B0", // δ introduces a class-breaking deformation: output\_raw: { id: "B1", class\_id: "vector", payload: { dim: 4, // DEVIATION BREAK: inconsistent with payload length 3 values: \[1, 2, 3\] } }, invariant\_state: { PHI\_INV\_01\_CLASS\_PRESERVATION: "not\_applicable\_yet", PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY: "not\_applicable\_yet", DELTA\_CLASS\_STABILITY: false // δ violated class stability } }, //------------------------------------------------------------ // STEP 2 — APPLY Φ TO B1 (Φ fails) //------------------------------------------------------------ step2\_apply\_phi: { operator: "Φ", input: "B1", // Φ attempts to project but finds illegal class → undefined class output\_raw: { id: "Φ(B1)", class\_id: "undefined", payload: null }, invariant\_violation: "PHI\_INV\_01\_CLASS\_PRESERVATION" }, //------------------------------------------------------------ // STEP 3 — APPLY TIER-02 REPAIR RULES //------------------------------------------------------------ step3\_phi\_repair: { applied\_rule: "PHI\_RW\_01\_CLASS\_REPAIR", repair\_action: "REPLACE undefined class with valid nearest lattice class; fix tensor dimension", output\_repaired: { id: "Φ(B1)'", class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] }, provenance: { repaired\_from: "Φ(B1)", rule: "PHI\_RW\_01\_CLASS\_REPAIR" } }, invariant\_state\_after: { PHI\_INV\_01\_CLASS\_PRESERVATION: true, PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY: "untested" } }, //------------------------------------------------------------ // STEP 4 — APPLY Π DIRECTLY TO B1 (raw evaluation) //------------------------------------------------------------ step4\_apply\_pi\_raw: { operator: "Π", input: "B1", output\_raw: { id: "Π(B1)", value: "NF\_vector\_sum(6)", // Example evaluation: sum of terms notes: "Even though dim mismatch exists, Tier-02 allows Π to interpret payload and normalize." } }, //------------------------------------------------------------ // STEP 5 — APPLY Π AFTER REPAIRED Φ(B1)' //------------------------------------------------------------ step5\_apply\_pi\_after\_phi: { operator: "Π ∘ Φ", input: "Φ(B1)'", output\_raw: { id: "Π(Φ(B1)')", value: "NF\_vector\_sum(6)" } }, //------------------------------------------------------------ // STEP 6 — TIER-02 ENFORCES Π∘Φ \= Π //------------------------------------------------------------ step6\_consistency\_enforcement: { invariant\_checked: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", before\_rewrite: { pi\_raw: "NF\_vector\_sum(6)", pi\_after\_phi: "NF\_vector\_sum(6)" }, satisfied: true, applied\_rule\_if\_needed: "PHI\_RW\_02\_PHI\_PI\_NF", final\_normal\_form: "NF\_vector\_sum(6)" }, //------------------------------------------------------------ // FULL EVOLUTION SUMMARY //------------------------------------------------------------ evolution\_summary: { initial: "B0", delta\_step: "B1", phi\_failure: "Φ(B1)", phi\_repair: "Φ(B1)'", pi\_raw: "Π(B1)", pi\_after\_phi: "Π(Φ(B1)')", final\_nf: "NF\_vector\_sum(6)" } }  
---

# \=============================================

# ✔ HUMAN-READABLE SUMMARY OF THE CHAIN

# \=============================================

## STEP 0 → STEP 1 (δ-break)

δ modifies the structure but breaks class invariance:  
r  
Copy code  
dim: 3 → dim: 4  
payload stays length 3

So "vector" is now invalid.  
---

## STEP 2 (Φ-break)

Φ tries to project a malformed vector and returns:  
ini  
Copy code  
class\_id \= undefined  
payload \= null

This violates Tier-02:

* PHI\_INV\_01 Class Preservation

---

## STEP 3 (repair)

Tier-02 rewrite repairs:  
vbnet  
Copy code  
dim restored to 3  
class restored to vector  
payload fixed

---

## STEP 4–6 (Π-consistency)

Evaluate before and after Φ:  
vbnet  
Copy code  
Π(B1)       → 6  
Π(Φ(B1)')   → 6

Tier-02 confirms:  
Copy code  
Π(Φ(B1)) \= Π(B1)   (in NF)

✔ PHI\_INV\_02 Projection–Evaluation Consistency satisfied.  
---

---

Copy code  
{ // \===================================================================== // TIER-02 — Φ-INVARIANTS FULL REGRESSION SUITE (40+ TESTS) // \===================================================================== meta: { suite\_id: "T2\_FULL\_SUITE\_PHI\_INVARIANTS", tier: 2, family: "Φ", version: "0.1.0", description: "40+ regression tests for Φ semantic form invariants: class preservation and Φ–Π consistency.", invariants: \[ "PHI\_INV\_01\_CLASS\_PRESERVATION", "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY" \], uses\_rewrite\_rules: \[ "PHI\_RW\_01\_CLASS\_REPAIR", "PHI\_RW\_02\_PHI\_PI\_NF", "PHI\_RW\_03\_ILLEGAL\_PHI", "PHI\_RW\_04\_DELTA\_PHI\_COMMUTE" \] }, // A tiny global semantic-class lattice your agent can extend. global\_lattice: { semantic\_classes: \[ "scalar", "vector", "matrix", "tensor", "form", "proposition", "predicate", "event", "state", "undefined" // reserved; should never be final NF class \] }, // Optional operator defaults operators: { phi: "Φ", phi\_semantic: "Φ\_s", phi\_causal: "Φ\_c", phi\_adjoint: "Φ\*", phi\_sum: "Φ⊕", phi\_to\_pi: "Φ→Π", eval: "Π", delta: "δ" }, // \===================================================================== // TEST CASES // \===================================================================== tests: \[ // \-------------------------------------------------- // GROUP 1: BASIC CLASS PRESERVATION (Φ on clean Boxes) // \-------------------------------------------------- { id: "T2-PHI-001", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "basic\_class\_preservation", description: "Φ preserves simple scalar class.", input\_box: { id: "B\_scalar\_1", class\_id: "scalar", payload: { value: 3.14 } }, operator\_chain: \["Φ"\], expected: { class\_id: "scalar", invariant\_ok: true } }, { id: "T2-PHI-002", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "basic\_class\_preservation", description: "Φ preserves vector class with consistent dimension.", input\_box: { id: "B\_vector\_1", class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] } }, operator\_chain: \["Φ"\], expected: { class\_id: "vector", invariant\_ok: true } }, { id: "T2-PHI-003", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "basic\_class\_preservation", description: "Φ preserves matrix class.", input\_box: { id: "B\_matrix\_1", class\_id: "matrix", payload: { shape: \[2, 2\], values: \[\[1, 0\], \[0, 1\]\] } }, operator\_chain: \["Φ"\], expected: { class\_id: "matrix", invariant\_ok: true } }, { id: "T2-PHI-004", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "basic\_class\_preservation", description: "Φ preserves proposition class.", input\_box: { id: "B\_prop\_1", class\_id: "proposition", payload: { formula: "P ∧ Q", vars: \["P", "Q"\] } }, operator\_chain: \["Φ\_s"\], expected: { class\_id: "proposition", invariant\_ok: true } }, { id: "T2-PHI-005", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "basic\_class\_preservation", description: "Φ preserves event class.", input\_box: { id: "B\_event\_1", class\_id: "event", payload: { label: "collision", time: 0.5 } }, operator\_chain: \["Φ\_c"\], expected: { class\_id: "event", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 2: ILLEGAL Φ ON UNCLASSIFIED BOXES // \-------------------------------------------------- { id: "T2-PHI-006", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "illegal\_phi", description: "Φ on Box with undefined class must explicitly error, not silently propagate.", input\_box: { id: "B\_undefined\_1", class\_id: "undefined", payload: { raw: "??? " } }, operator\_chain: \["Φ"\], expected: { // Use your PHI\_RW\_03\_ILLEGAL\_PHI rule rewrite\_rule: "PHI\_RW\_03\_ILLEGAL\_PHI", result\_tag: "⊥\_PhiDomain", invariant\_ok: true } }, { id: "T2-PHI-007", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "illegal\_phi", description: "Φ on Box with missing class\_id should yield explicit domain error.", input\_box: { id: "B\_no\_class\_1", payload: { value: 42 } }, operator\_chain: \["Φ"\], expected: { rewrite\_rule: "PHI\_RW\_03\_ILLEGAL\_PHI", result\_tag: "⊥\_PhiDomain", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 3: CLASS REPAIR (Φ \+ PHI\_RW\_01\_CLASS\_REPAIR) // \-------------------------------------------------- { id: "T2-PHI-008", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "class\_repair", description: "Vector with wrong dimension is repaired by Φ via PHI\_RW\_01\_CLASS\_REPAIR.", input\_box: { id: "B\_vec\_break\_1", class\_id: "vector", payload: { dim: 4, values: \[1, 2, 3\] } }, operator\_chain: \["Φ", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] }, invariant\_ok: true } }, { id: "T2-PHI-009", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "class\_repair", description: "Matrix with inconsistent shape is repaired to minimal valid shape.", input\_box: { id: "B\_matrix\_break\_1", class\_id: "matrix", payload: { shape: \[2, 3\], // says 2x3 values: \[\[1, 2\], \[3, 4\]\] // actually 2x2 } }, operator\_chain: \["Φ", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { class\_id: "matrix", payload: { shape: \[2, 2\], values: \[\[1, 2\], \[3, 4\]\] }, invariant\_ok: true } }, { id: "T2-PHI-010", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "class\_repair", description: "Tensor with rank mismatch is projected to nearest valid tensor class.", input\_box: { id: "B\_tensor\_break\_1", class\_id: "tensor", payload: { rank: 3, shape: \[2, 2\], values: \[\[\[1, 2\], \[3, 4\]\]\] // rank 3 claimed, rank 2 data } }, operator\_chain: \["Φ", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { class\_id: "tensor", payload: { rank: 2, shape: \[2, 2\], // agent may renormalize but must produce valid consistent tensor }, invariant\_ok: true } }, { id: "T2-PHI-011", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "class\_repair", description: "Malformed proposition is projected into valid proposition with simplified formula.", input\_box: { id: "B\_prop\_break\_1", class\_id: "proposition", payload: { formula: "P ∧", // malformed vars: \["P"\] } }, operator\_chain: \["Φ", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { class\_id: "proposition", payload: { formula: "P", // repaired to simplest valid proposition vars: \["P"\] }, invariant\_ok: true } }, { id: "T2-PHI-012", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "class\_repair", description: "Event with missing time defaults to canonical reference time.", input\_box: { id: "B\_event\_break\_1", class\_id: "event", payload: { label: "initial\_state" // missing time } }, operator\_chain: \["Φ\_c", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { class\_id: "event", payload: { label: "initial\_state", time: 0.0 // canonical default }, invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 4: Φ–Π CONSISTENCY (PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY) // \-------------------------------------------------- { id: "T2-PHI-013", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_pi\_consistency", description: "Scalar evaluation is unchanged by Φ.", input\_box: { id: "B\_scalar\_2", class\_id: "scalar", payload: { value: 5 } }, operator\_chain: \["Π", "Π∘Φ"\], expected: { pi\_direct: "NF\_scalar(5)", pi\_after\_phi: "NF\_scalar(5)", invariant\_ok: true } }, { id: "T2-PHI-014", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_pi\_consistency", description: "Vector-sum evaluation is invariant under Φ.", input\_box: { id: "B\_vector\_2", class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] } }, operator\_chain: \["Π", "Π∘Φ"\], expected: { pi\_direct: "NF\_vector\_sum(6)", pi\_after\_phi: "NF\_vector\_sum(6)", invariant\_ok: true } }, { id: "T2-PHI-015", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_pi\_consistency", description: "Matrix-determinant evaluation is invariant under Φ.", input\_box: { id: "B\_matrix\_2", class\_id: "matrix", payload: { shape: \[2, 2\], values: \[\[1, 2\], \[3, 4\]\] } }, operator\_chain: \["Π", "Π∘Φ"\], expected: { pi\_direct: "NF\_det(-2)", pi\_after\_phi: "NF\_det(-2)", invariant\_ok: true } }, { id: "T2-PHI-016", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_pi\_consistency", description: "Truth evaluation of proposition is invariant under Φ\_s.", input\_box: { id: "B\_prop\_2", class\_id: "proposition", payload: { formula: "P ∨ ¬P", vars: \["P"\] } }, environment: { assignment: { P: true } }, operator\_chain: \["Π", "Π∘Φ\_s"\], expected: { pi\_direct: "⊤", pi\_after\_phi: "⊤", invariant\_ok: true } }, { id: "T2-PHI-017", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_pi\_consistency", description: "Π∘Φ normalized via PHI\_RW\_02\_PHI\_PI\_NF equals NF(Π).", input\_box: { id: "B\_vector\_3", class\_id: "vector", payload: { dim: 2, values: \[10, \-10\] } }, operator\_chain: \["Π∘Φ", "PHI\_RW\_02\_PHI\_PI\_NF"\], expected: { pi\_nf: "NF\_vector\_sum(0)", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 5: δ–Φ COMMUTATION CASES (PHI\_RW\_04\_DELTA\_PHI\_COMMUTE) // \-------------------------------------------------- { id: "T2-PHI-018", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "delta\_phi\_commutation", description: "δ and Φ commute on class-preserving δ (simple shift).", input\_box: { id: "B\_vector\_4", class\_id: "vector", payload: { dim: 3, values: \[1, 1, 1\] } }, delta\_action: "add\_constant(1) to each component", operator\_chain: \["δ∘Φ", "Φ∘δ"\], expected: { relation: "δ(Φ(B)) \== Φ(δ(B))", invariant\_ok: true } }, { id: "T2-PHI-019", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "delta\_phi\_commutation", description: "δ that changes dimension breaks commutation; PHI\_RW\_04\_DELTA\_PHI\_COMMUTE not applicable.", input\_box: { id: "B\_vector\_5", class\_id: "vector", payload: { dim: 2, values: \[1, 2\] } }, delta\_action: "extend\_dimension\_to\_3\_with\_zero", operator\_chain: \["δ∘Φ", "Φ∘δ"\], expected: { relation: "δ(Φ(B)) \!= Φ(δ(B))", commutation\_guard: "disabled", invariant\_ok: true } }, { id: "T2-PHI-020", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "delta\_phi\_commutation", description: "PHI\_RW\_04\_DELTA\_PHI\_COMMUTE used only when δ preserves class.", input\_box: { id: "B\_scalar\_3", class\_id: "scalar", payload: { value: 7 } }, delta\_action: "multiply\_by\_2", operator\_chain: \["δ∘Φ", "Φ∘δ", "PHI\_RW\_04\_DELTA\_PHI\_COMMUTE"\], expected: { relation: "δ(Φ(B)) \== Φ(δ(B))", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 6: Φ⊕ AND SEMANTIC FORM SUMS // \-------------------------------------------------- { id: "T2-PHI-021", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "phi\_sum", description: "Φ⊕ combines two compatible vectors into a vector in same class.", input\_boxes: \[ { id: "B\_vec\_a", class\_id: "vector", payload: { dim: 2, values: \[1, 2\] } }, { id: "B\_vec\_b", class\_id: "vector", payload: { dim: 2, values: \[3, 4\] } } \], operator\_chain: \["Φ⊕"\], expected: { class\_id: "vector", payload: { dim: 2, values: \[4, 6\] }, invariant\_ok: true } }, { id: "T2-PHI-022", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "phi\_sum", description: "Φ⊕ on incompatible classes triggers class error.", input\_boxes: \[ { id: "B\_vec\_c", class\_id: "vector", payload: { dim: 2, values: \[1, 2\] } }, { id: "B\_scalar\_4", class\_id: "scalar", payload: { value: 5 } } \], operator\_chain: \["Φ⊕"\], expected: { result\_tag: "CLASS\_MISMATCH\_ERROR", invariant\_ok: true } }, { id: "T2-PHI-023", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_sum", description: "Π applied after Φ⊕ matches Π applied to Σ of inputs.", input\_boxes: \[ { id: "B\_vec\_d", class\_id: "vector", payload: { dim: 2, values: \[1, 1\] } }, { id: "B\_vec\_e", class\_id: "vector", payload: { dim: 2, values: \[2, 2\] } } \], operator\_chain: \["Π∘(Φ⊕)", "Π∘Σ∘(Φ,Φ)"\], expected: { pi\_after\_phi\_sum: "NF\_vector\_sum(6)", pi\_after\_sigma\_of\_phi: "NF\_vector\_sum(6)", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 7: Φ\* (ADJOINT) IDENTITY-LIKE BEHAVIOR // \-------------------------------------------------- { id: "T2-PHI-024", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "phi\_adjoint", description: "Φ\*∘Φ acts as identity on semantic class representatives.", input\_box: { id: "B\_vector\_rep\_1", class\_id: "vector", payload: { dim: 2, values: \[1, 0\] } }, operator\_chain: \["Φ", "Φ\*"\], expected: { relation: "Φ\*(Φ(B)) \== B on semantic\_class", invariant\_ok: true } }, { id: "T2-PHI-025", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "phi\_adjoint", description: "Φ\* may not leave semantic class lattice.", input\_box: { id: "B\_matrix\_rep\_1", class\_id: "matrix", payload: { shape: \[2, 2\], values: \[\[1, 0\], \[0, 1\]\] } }, operator\_chain: \["Φ", "Φ\*"\], expected: { class\_id: "matrix", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 8: MULTI-STEP δ–Φ–Π CHAINS (FROM EARLIER EXAMPLE) // \-------------------------------------------------- { id: "T2-PHI-026", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "multi\_step\_chain", description: "Reproduce tiny δ–Φ–repair chain for B0 → B1 → Φ(B1) → Φ(B1)'.", input\_box: { id: "B0", class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] } }, chain: \[ { op: "δ", out\_id: "B1", note: "dim=4 with 3 values" }, { op: "Φ", out\_id: "Φ(B1)" }, { op: "PHI\_RW\_01\_CLASS\_REPAIR", out\_id: "Φ(B1)'" } \], expected: { final\_box: { id: "Φ(B1)'", class\_id: "vector", payload: { dim: 3, values: \[1, 2, 3\] } }, invariant\_ok: true } }, { id: "T2-PHI-027", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "multi\_step\_chain", description: "Π∘Φ and Π agree in NF after repair on earlier chain.", input\_box: { id: "B1", class\_id: "vector", payload: { dim: 4, values: \[1, 2, 3\] } }, chain: \[ { op: "Φ", out\_id: "Φ(B1)" }, { op: "PHI\_RW\_01\_CLASS\_REPAIR", out\_id: "Φ(B1)'" }, { op: "Π", on: "B1", out\_id: "Π(B1)" }, { op: "Π", on: "Φ(B1)'", out\_id: "Π(Φ(B1)')" } \], expected: { pi\_direct: "NF\_vector\_sum(6)", pi\_after\_phi: "NF\_vector\_sum(6)", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 9: PROPOSITIONAL SEMANTIC SHAPE TESTS // \-------------------------------------------------- { id: "T2-PHI-028", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "propositional", description: "Φ\_s normalizes logically equivalent formulas but preserves proposition class.", input\_box: { id: "B\_prop\_3", class\_id: "proposition", payload: { formula: "P ∧ Q ∧ P", vars: \["P", "Q"\] } }, operator\_chain: \["Φ\_s"\], expected: { class\_id: "proposition", payload: { formula: "P ∧ Q" }, invariant\_ok: true } }, { id: "T2-PHI-029", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "propositional", description: "Π truth value unchanged by Φ\_s simplification.", input\_box: { id: "B\_prop\_4", class\_id: "proposition", payload: { formula: "P ∧ Q ∧ P", vars: \["P", "Q"\] } }, environment: { assignment: { P: true, Q: false } }, operator\_chain: \["Π", "Π∘Φ\_s"\], expected: { pi\_direct: "⊥", pi\_after\_phi: "⊥", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 10: EVENT / STATE FORM TESTS // \-------------------------------------------------- { id: "T2-PHI-030", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "event\_state", description: "Φ\_c projects event into canonical causal form but preserves class.", input\_box: { id: "B\_event\_2", class\_id: "event", payload: { label: "collision", time: 1.234, extra: { frame: "lab" } } }, operator\_chain: \["Φ\_c"\], expected: { class\_id: "event", payload: { label: "collision", time: 1.234 }, invariant\_ok: true } }, { id: "T2-PHI-031", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "event\_state", description: "Π evaluation (e.g. event validity) is invariant under causal Φ projection.", input\_box: { id: "B\_event\_3", class\_id: "event", payload: { label: "arrival", time: 2.5 } }, operator\_chain: \["Π", "Π∘Φ\_c"\], expected: { pi\_direct: "EVENT\_VALID", pi\_after\_phi: "EVENT\_VALID", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 11: FAILURE MODES — NO REPAIR POSSIBLE // \-------------------------------------------------- { id: "T2-PHI-032", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "no\_repair\_possible", description: "Φ on Box with completely incompatible payload must produce INVALID\_CLASS\_ERROR.", input\_box: { id: "B\_garbage\_1", class\_id: "vector", payload: { nonsense: true } }, operator\_chain: \["Φ", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { result\_tag: "INVALID\_CLASS\_ERROR", invariant\_ok: true } }, { id: "T2-PHI-033", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "no\_repair\_possible", description: "Φ on Box with class not in lattice must error.", input\_box: { id: "B\_unknown\_class\_1", class\_id: "hypervector", // not in lattice payload: { data: \[1, 2, 3\] } }, operator\_chain: \["Φ"\], expected: { result\_tag: "UNKNOWN\_CLASS\_ERROR", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 12: CROSS-CHECK Φ→Π BRIDGE OPERATOR (Φ→Π) // \-------------------------------------------------- { id: "T2-PHI-034", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_to\_pi\_bridge", description: "Φ→Π behaves like Π∘Φ on vectors.", input\_box: { id: "B\_vector\_6", class\_id: "vector", payload: { dim: 2, values: \[4, \-1\] } }, operator\_chain: \["Φ→Π", "Π∘Φ"\], expected: { phi\_to\_pi: "NF\_vector\_sum(3)", pi\_after\_phi: "NF\_vector\_sum(3)", invariant\_ok: true } }, { id: "T2-PHI-035", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "phi\_to\_pi\_bridge", description: "Φ→Π behaves like Π∘Φ on propositions.", input\_box: { id: "B\_prop\_5", class\_id: "proposition", payload: { formula: "P → Q", vars: \["P", "Q"\] } }, environment: { assignment: { P: true, Q: false } }, operator\_chain: \["Φ→Π", "Π∘Φ\_s"\], expected: { phi\_to\_pi: "⊥", pi\_after\_phi: "⊥", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 13: STRESS CASES — NESTED COMPOSITIONS // \-------------------------------------------------- { id: "T2-PHI-036", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "nested\_compositions", description: "Π∘Φ∘δ∘Φ on a stable class yields same NF as Π∘δ.", input\_box: { id: "B\_vector\_7", class\_id: "vector", payload: { dim: 3, values: \[0, 1, 2\] } }, delta\_action: "add\_constant(1)", operator\_chain: \["Π∘δ", "Π∘Φ∘δ∘Φ"\], expected: { pi\_delta: "NF\_vector\_sum(6)", // \[1,2,3\] \-\> sum=6 pi\_phi\_delta\_phi: "NF\_vector\_sum(6)", invariant\_ok: true } }, { id: "T2-PHI-037", invariant: "PHI\_INV\_02\_PROJ\_EVAL\_CONSISTENCY", category: "nested\_compositions", description: "Complex composition: Π∘Φ⊕(Φ(B1),Φ(B2)) agrees with Π on Σ of originals.", input\_boxes: \[ { id: "B\_vec\_f", class\_id: "vector", payload: { dim: 2, values: \[1, 3\] } }, { id: "B\_vec\_g", class\_id: "vector", payload: { dim: 2, values: \[2, 4\] } } \], operator\_chain: \[ "Π∘Φ⊕(Φ(B\_vec\_f), Φ(B\_vec\_g))", "Π∘Σ(B\_vec\_f, B\_vec\_g)" \], expected: { pi\_phi\_sum: "NF\_vector\_sum(10)", pi\_sigma: "NF\_vector\_sum(10)", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 14: EDGE-OF-DOMAIN TESTS (NEARLY INVALID) // \-------------------------------------------------- { id: "T2-PHI-038", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "edge\_of\_domain", description: "Vector with dim=0 is projected to scalar zero or invalid, but never undefined.", input\_box: { id: "B\_vector\_edge\_1", class\_id: "vector", payload: { dim: 0, values: \[\] } }, operator\_chain: \["Φ", "PHI\_RW\_01\_CLASS\_REPAIR"\], expected: { // Either becomes zero scalar or explicit invalid; but not undefined. allowed\_results: \[ { class\_id: "scalar", payload: { value: 0 } }, { result\_tag: "INVALID\_CLASS\_ERROR" } \], invariant\_ok: true } }, { id: "T2-PHI-039", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "edge\_of\_domain", description: "Proposition with empty var set but well-formed formula remains in proposition class.", input\_box: { id: "B\_prop\_edge\_1", class\_id: "proposition", payload: { formula: "⊤", vars: \[\] } }, operator\_chain: \["Φ\_s"\], expected: { class\_id: "proposition", invariant\_ok: true } }, // \-------------------------------------------------- // GROUP 15: META-TEST — SUITE SELF-CONSISTENCY // \-------------------------------------------------- { id: "T2-PHI-040", invariant: "PHI\_INV\_01\_CLASS\_PRESERVATION", category: "meta\_test", description: "Meta-test: ensure none of the tests rely on final class\_id='undefined' as NF.", meta\_check: { scan: "all\_tests", forbidden\_final\_class: "undefined" }, expected: { suite\_consistency: "no\_final\_undefined\_class", invariant\_ok: true } } \] }  
