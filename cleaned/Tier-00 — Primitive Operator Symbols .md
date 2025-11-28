# Tier-00 — Primitive Operator Symbols (Irreducible Alphabet)

These are symbols only, not the full operators (Tier-1+).  
They encode only meaning, signature, domain, and irreducibility.  
Primitive Operator Alphabet:

* δ — deviation  
* Φ — projection  
* Π — evaluation  
* μ — micro-weight / adjacency  
* ψ — oscillation  
* λ — curvature / deformation  
* Σ — summation / contraction  
* Θ — polarity router  
* χ — semantic time / evolution increment  
* ρ — layer operator  
* Ω — global constraint / meta-normalization

---

# 1\. tier\_00\_metadata.json

json  
Copy code  
{ "tier": "00", "name": "Primitive Operator Symbols", "intent": "Define the irreducible operator alphabet of IGSOA / MBC-4.0.", "description": "Tier-00 contains the raw primitive operator symbols δ, Φ, Π, μ, ψ, λ, Σ, Θ, χ, ρ, Ω. These represent semantic actions but are not yet lifted to full operators.", "entities": \[ {"symbol": "δ", "meaning": "deviation primitive"}, {"symbol": "Φ", "meaning": "projection primitive"}, {"symbol": "Π", "meaning": "evaluation primitive"}, {"symbol": "μ", "meaning": "local weight primitive"}, {"symbol": "ψ", "meaning": "oscillation primitive"}, {"symbol": "λ", "meaning": "curvature primitive"}, {"symbol": "Σ", "meaning": "summation primitive"}, {"symbol": "Θ", "meaning": "polarity primitive"}, {"symbol": "χ", "meaning": "evolution primitive"}, {"symbol": "ρ", "meaning": "layer primitive"}, {"symbol": "Ω", "meaning": "constraint primitive"} \], "primitives\_are\_irreducible": true, "sealed": false }  
---

# 2\. tier\_00\_operator\_pack.json

(These are symbol declarations, not full operators.)  
json  
Copy code  
{ "tier": "00", "operator\_pack": { "δ": { "type": "primitive\_symbol", "arity": 1, "domain": "semantic\_geometry" }, "Φ": { "type": "primitive\_symbol", "arity": 1, "domain": "projection\_space" }, "Π": { "type": "primitive\_symbol", "arity": 1, "domain": "evaluation\_space" }, "μ": { "type": "primitive\_symbol", "arity": 1, "domain": "local\_weight\_field" }, "ψ": { "type": "primitive\_symbol", "arity": 1, "domain": "oscillation\_modes" }, "λ": { "type": "primitive\_symbol", "arity": 1, "domain": "curvature\_modes" }, "Σ": { "type": "primitive\_symbol", "arity": 1, "domain": "contraction\_algebra" }, "Θ": { "type": "primitive\_symbol", "arity": 1, "domain": "polarity\_space" }, "χ": { "type": "primitive\_symbol", "arity": 1, "domain": "semantic\_time" }, "ρ": { "type": "primitive\_symbol", "arity": 1, "domain": "layer\_hierarchy" }, "Ω": { "type": "primitive\_symbol", "arity": 1, "domain": "global\_constraints" } } }  
---

# 3\. tier\_00\_interaction\_table.json

(Tier-00 interactions are identity-level: symbols do not interact yet.)  
json  
Copy code  
{ "tier": "00", "interaction\_table": { "rules": \[ { "pair": \["δ", "Φ"\], "interaction": "undefined at Tier-00" }, { "pair": \["δ", "Π"\], "interaction": "undefined at Tier-00" }, { "pair": \["Φ", "Π"\], "interaction": "undefined at Tier-00" }, { "pair": \["μ", "ψ"\], "interaction": "undefined at Tier-00" }, { "pair": \["λ", "ψ"\], "interaction": "undefined at Tier-00" }, { "pair": \["Σ", "Θ"\], "interaction": "undefined at Tier-00" }, { "pair": \["χ", "Ω"\], "interaction": "undefined at Tier-00" }, { "pair": \["ρ", "χ"\], "interaction": "undefined at Tier-00" }, { "pair": \["Ω", "Σ"\], "interaction": "undefined at Tier-00" } \], "note": "Tier-00 symbols are atomic and have no defined compositions prior to Tier-01." } }  
---

# 4\. tier\_00\_axiom\_box.json (sealed)

The sealed box that declares these symbols atomic and irreducible.  
json  
Copy code  
{ "axiom\_box": { "name": "Tier-00 Primitive Operator Alphabet", "sealed": true, "intent": "Define the irreducible alphabet of operator symbols.", "domain": "All subsequent tiers of the IGSOA operator hierarchy.", "axioms": \[ { "id": "A0\_1", "statement": "Each primitive operator symbol S ∈ {δ, Φ, Π, μ, ψ, λ, Σ, Θ, χ, ρ, Ω} is irreducible." }, { "id": "A0\_2", "statement": "No primitive operator symbol can be expressed as a rewrite, projection, evaluation, or contraction of any other primitive symbol." }, { "id": "A0\_3", "statement": "Primitive symbols have no internal structure at Tier-00." }, { "id": "A0\_4", "statement": "All higher-tier operators derive from compositions of these primitive symbols." } \], "constraints": \[ "No compositions allowed at Tier-00.", "No rewrite expansions allowed at Tier-00.", "No interaction rules may be added at Tier-00." \], "cross\_links": { "feeds\_into": \["Tier-01 Deviation Layer", "Tier-01 Projection Layer", "Tier-01 Evaluation Layer"\], "parent": null } } }  
---

# 5\. tier\_00\_rewrite\_system.json

(No rewrite is permitted; everything is atomic.)  
json  
Copy code  
{ "tier": "00", "rewrite\_system": { "rules": \[ { "symbol": "δ", "rewrite": "δ" }, { "symbol": "Φ", "rewrite": "Φ" }, { "symbol": "Π", "rewrite": "Π" }, { "symbol": "μ", "rewrite": "μ" }, { "symbol": "ψ", "rewrite": "ψ" }, { "symbol": "λ", "rewrite": "λ" }, { "symbol": "Σ", "rewrite": "Σ" }, { "symbol": "Θ", "rewrite": "Θ" }, { "symbol": "χ", "rewrite": "χ" }, { "symbol": "ρ", "rewrite": "ρ" }, { "symbol": "Ω", "rewrite": "Ω" } \], "note": "Irreducibility enforced: every symbol rewrites only to itself." } }  
---

# 6\. tier\_00\_module\_pack.json

Bundle includes: metadata \+ symbols \+ sealed axiom box.  
json  
Copy code  
{ "tier": "00", "module\_pack": { "modules": \[ "tier\_00\_metadata.json", "tier\_00\_operator\_pack.json", "tier\_00\_interaction\_table.json", "tier\_00\_axiom\_box.json", "tier\_00\_rewrite\_system.json" \], "export": { "primitive\_alphabet": \["δ", "Φ", "Π", "μ", "ψ", "λ", "Σ", "Θ", "χ", "ρ", "Ω"\] }, "notes": "Tier-00 establishes the atomic operator alphabet used by all higher-tier operator packs." } }  
