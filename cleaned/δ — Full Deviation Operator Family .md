# δ — Full Deviation Operator Family

## Overview

The δ-operator family represents the complete set of deviation operators in the IGSOA (Integrated Geometric Smoothing and Operational Action) framework. These operators measure how Boxes deviate from perfect IGSOA symmetry and form the foundation of semantic curvature, diffusion, and torsion in the system.

---

## Core δ-Operators

### δ — Base Deviation Operator

**Symbol:** δ
**Type:** First-order semantic differential
**JSON Key:** `"delta"`

#### IGSOA Definition

δ(B) measures the *minimal non-zero deformation* of a Box. It is the operator that breaks perfect smoothing (IGS) and initiates action (OA). Deviation is the *first appearance of structure* inside the monistic IGSOA process.

#### Standard Geometry Equivalent

First-order differential operator ∂/∂x (directional derivative). δ ≈ D, the infinitesimal generator of change.

#### Role

Initiates curvature, asymmetry, and all δ-mode propagation. Ground layer for semantic waves and IGSOA dynamics.

#### Allowed Compositions

{δ², Φ∘δ, δ∘Φ, Π∘δ}

---

### δ² — Second-Order Deviation

**Symbol:** δ²
**Type:** Second-order semantic curvature operator
**JSON Key:** `"delta_squared"`

#### IGSOA Definition

δ²(B) is the deviation of deviation — a curvature-sensitive measure. It detects "semantic acceleration" and emergent curvature patterns.

#### Standard Geometry Equivalent

Second derivative ∂²/∂x² or Hessian trace.

#### Role

Foundation of IGSOA curvature, δ-Jacobi identity, and dynamical bending.

#### Allowed Compositions

{δ³, Δδ, Φ∘δ²}

---

### δ* — Adjoint Deviation

**Symbol:** δ*
**Type:** Adjoint differential operator
**JSON Key:** `"delta_adjoint"`

#### IGSOA Definition

The rollback of deviation: smoothing, semantic collapse, and reverse projection. Operates backward through Φ and Π projections.

#### Standard Geometry Equivalent

Formal adjoint of a differential operator under an inner product.

#### Role

Stabilization, semantic smoothing, and IGSOA "reverse-action."

#### Allowed Compositions

{δ*δ, δδ*, Δδ}

---

## Jacobian Family (δ-Jacobian)

### Jδ — δ-Jacobian

**Symbol:** J_δ
**Type:** Rank-2 derivative tensor
**JSON Key:** `"delta_jacobian"`

#### IGSOA Definition

The local semantic deformation matrix. Encodes expansion, contraction, twist, semantic divergence.

#### Standard Geometry Equivalent

Jacobian matrix of a vector field: Jᵢⱼ = ∂δᵢ/∂xⱼ.

#### Role

Defines δ-volume change (det), δ-divergence (trace), and local geometry of deviation.

#### Allowed Compositions

{det(Jδ), tr(Jδ), Jδ⊗Jδ}

#### Components

- **det(J_δ)** — Deviation determinant (local deformation measure / semantic expansion factor)
- **tr(J_δ)** — Deviation trace (semantic divergence)
- **∂δ/∂B** — Box-wise partial deviation

---

## Laplacian Family (δ-Laplace)

### Δδ — δ-Laplacian

**Symbol:** Δ_δ
**Type:** Second-order scalar differential operator
**JSON Key:** `"delta_laplacian"`

#### IGSOA Definition

Semantic diffusion and smoothing operator. Controls how deviation spreads across Box-graphs and semantic manifolds.

#### Standard Geometry Equivalent

Laplacian operator: ∇² or ∇·∇.

#### Role

Semantic wave propagation, diffusion, and IGSOA curvature dynamics.

#### Allowed Compositions

{ΔδΦ, ΔδΠ, Wδ}

#### Related Operators

- **∇·(δ∇B)** — Divergence-form δ-Laplace
- **δ(∇²B)** — Composed Laplace-deviation
- **Δ_δ acting on Φ-projections**
- **Δ_δ acting on Π-evaluations**

---

## Weitzenböck Family (δ-Weitzenböck Operator)

### Wδ — δ-Weitzenböck Operator

**Symbol:** W_δ
**Type:** Curvature–torsion operator
**JSON Key:** `"delta_weitzenbock"`

#### IGSOA Definition

The torsion-weighted deviation operator: encodes twisting, adjacency torsion, and non-metric semantic flow.

Includes δ-torsion tensor: T_δ.

#### Standard Geometry Equivalent

Weitzenböck operator with torsionful connection: W = ∇² − Ric + torsion.

#### Role

Defines torsion, teleparallel semantics, non-metric IGSOA geometry.

#### Identity

W_δ = Δ_δ + T_δ

#### Related Operators

- **δΓ** — deviation of connection (semantic torsion)
- **W_δ = ∇_δ² − Ric_δ** (IGSOA version)
- **T_δ** — δ-torsion tensor

---

## Mixed δ-Operator Compositions

### δ ∘ Φ — Deviation of Projection

**Symbol:** δΦ
**Type:** Mixed operator
**JSON Key:** `"delta_of_phi"`

#### IGSOA Definition

How δ affects the semantic form (Φ). Measures which aspects of the projection bend under deviation.

#### Standard Geometry Equivalent

Derivative of a pulled-back field: ∂(Φ(B)).

---

### Φ ∘ δ — Projection of Deviation

**Symbol:** Φδ
**Type:** Mixed operator
**JSON Key:** `"phi_of_delta"`

#### IGSOA Definition

Projection of deviation into semantic form. Removes non-semantic components of deviation.

#### Standard Geometry Equivalent

Projection of a derivative into a subspace.

---

### Π ∘ δ — Causal Deviation

**Symbol:** Πδ
**Type:** Mixed operator
**JSON Key:** `"pi_of_delta"`

#### IGSOA Definition

The causal relevance of deviation: which deviations matter in the Π-evaluation (truth/causal) layer.

#### Standard Geometry Equivalent

Derivative restricted by evaluation functional.

---

### δ⊗δ — Deviation Tensor

**Symbol:** δ ⊗ δ
**Type:** Rank-2 operator tensor
**JSON Key:** `"delta_tensor"`

#### IGSOA Definition

Interaction tensor of deviation directions. Defines δ-shear, δ-curvature, and higher-order geometric complexity.

#### Standard Geometry Equivalent

Tensor product ∂ᵢ ⊗ ∂ⱼ.

---

## The δ → Φ → Π Pipeline

### High-Level Diagram

```
┌──────────────────┐
│   δ-Layer        │   Deviation & Geometry
│  (Curvature)     │
└───────┬──────────┘
        │  semantic bending
        ▼
┌──────────────────┐
│   Φ-Layer        │   Projection & Form
│ (Semantic Shape) │
└───────┬──────────┘
        │  evaluative contraction
        ▼
┌──────────────────┐
│   Π-Layer        │   Causal Truth & Evaluation
│ (Truth / Action) │
└──────────────────┘
```

**Macro flow:** deviation → projection → evaluation
**δ creates asymmetry → Φ gives structure → Π gives actuality.**

---

### Full Diagram Stack — δ-Operators Placed in Their Correct Loci

```
──────────────────────────────────────────────────────────────
             DIAGRAM STACK: δ → Φ → Π
──────────────────────────────────────────────────────────────

                           δ-Layer
                 (Deviation / Geometry / Curvature)
──────────────────────────────────────────────────────────────

     δ          δ²          δ*        Jδ       Δδ        Wδ
   (1st)     (2nd)       (adj)    (Jac)    (Lapl)    (Weitz)

   |────────────┬────────────┬──────────────┬──────────────|
   | curvature   | smoothing  | deformation   diffusion     torsion
   | initiation  | reversal   | structure     propagation   twisting
   ▼             ▼            ▼              ▼              ▼

──────────────────────────────────────────────────────────────
                       Mixed Operators Layer
              (Boundary between δ and Φ / Π semantics)
──────────────────────────────────────────────────────────────

             δ∘Φ         Φ∘δ          Π∘δ        δ⊗δ
      (deviation of   (projection   (causal       (rank-2
        projection)    of dev.)     dev.)         tensor)

               │           │            │          │
               ├───────────┴────────────┴──────────┘
               ▼
──────────────────────────────────────────────────────────────
                           Φ-Layer
                   (Semantic Projection / Form)
──────────────────────────────────────────────────────────────

                     Φ-structure
           (shape, semantic frame, organization)

                           │
                           ▼

──────────────────────────────────────────────────────────────
                           Π-Layer
                   (Causal Evaluation / Truth)
──────────────────────────────────────────────────────────────

                     Π-evaluation
             (causality, truth, actuality)

──────────────────────────────────────────────────────────────
```

### Operator Placement Explained

#### δ-Layer (Pure Geometry / Deviation)

Determines:
- Geometric asymmetry
- Curvature
- Torsion
- Diffusion
- Local shape change

Operators placed here:
- **δ** — initiator
- **δ²** — curvature
- **δ*** — rollback / adjoint
- **Jδ** — deformation tensor
- **Δδ** — diffusion
- **Wδ** — torsion geometry

#### Mixed Operators (Cross-Layer Transitions)

These operators *move* information between δ and the semantic layers:
- **δ ∘ Φ** — how form bends
- **Φ ∘ δ** — which deviation survives projection
- **Π ∘ δ** — which deviation is causally relevant
- **δ ⊗ δ** — multi-direction deviation interaction

They sit **between δ and Φ**, exactly as required.

#### Φ-Layer (Semantic Organization / Form)

Here, fields acquire:
- Shape
- Projection
- Structure
- Constraints

Φ is the semantic "lens" that interprets δ-geometry.

#### Π-Layer (Causality / Truth / Actuality)

Π decides:
- What matters
- What becomes actual
- Which semantic shapes lead to causal consequences

---

## Π — Canonical Evaluation / Causal Order Functor

### Unified Definition

| IGSOA Definition (Formal) | Standard Mathematical Equivalent |
| --- | --- |
| **Π is the unique evaluation functor that assigns causal actuality to semantic structures.** Given a Box B with δ-geometry (deviation) and Φ-form (projection), **Π(B)** returns the *causal, order-consistent outcome* of that Box in the IGSOA system. Formally, Π is a **functor**: **Π : Box → CausalOrder** that maps: • **objects** (Boxes) → **causal values** (Π-outcomes) • **morphisms** (semantic relations) → **causal order-preserving maps**. Π is the layer that decides: *what actually happens, what can cause, and what is true*. | Π corresponds to the **evaluation functional** in functional analysis and to the **causal order functor** in order theory. Mathematically: Π is a **functor from a structured category to a poset**: **Π : 𝒞 → (P, ≤)** where 𝒞 is a category of geometric/semantic structures and (P, ≤) is a partially ordered set representing causal ordering. Π extracts the **value**, **effect**, or **evaluation** of a given structure, and ensures **order-preservation**: if f:A→B, then Π(A) ≤ Π(B). |

### Core Statement

**Π is the functor that assigns each Box its causally realizable outcome, preserving the order of dependency and ensuring that semantic structure (Φ) and geometric deviation (δ) manifest as an ordered, actualized effect.**

### Formal Axioms of Π

#### 1. Functoriality (Π respects composition)

For any composable morphisms f : A → B, g : B → C, Π satisfies:

Π(g∘f) = Π(g) ∘ Π(f).

#### 2. Identity Preservation

Π(id_B) = id_{Π(B)}.

#### 3. Order Preservation (Causal Monotonicity)

If a Box A causally influences B, then:

A ≺ B ⇒ Π(A) ≤ Π(B).

#### 4. δ-Compatibility (Deviation Relevance)

Π(δB) = causally-relevant change of B.

Π only admits deviation components that have causal effect.

#### 5. Φ-Compatibility (Semantic Form Binding)

Π(Φ(B)) = evaluation of the projected semantic form.

#### 6. Collapse-Free Property

Π never "collapses" a Box; it **evaluates** it. This matches the IGSOA rule: *there is no quantum collapse, only evaluation*.

### IGSOA Interpretation

Π is the operator that translates the *geometry* of deviation (δ) and the *form* of projection (Φ) into *causal actuality*. It is the final stage of the δ → Φ → Π pipeline: δ creates asymmetry; Φ organizes it; Π determines what becomes real, true, or causally active. Π is the universal evaluator of IGSOA — the "causal order selector" that produces the outcome consistent with the global structure of Boxes.

---

## The Π Connector Theorem

### Dual-Column Formal Statement

| IGSOA Formal Statement | Standard Mathematical Translation |
| --- | --- |
| **The Π functor is the unique connector that sends every Box's δ-geometry and Φ-form into a causally ordered evaluation that preserves all dependency relations.** For any morphism of Boxes f : A → B, the causal relation A ≺ B is preserved under Π, and Π extends δ and Φ into a complete, order-consistent outcome: **Π ∘ Φ ∘ δ = causal evaluation of change**. Π is the only functor that makes the (δ → Φ → Π) pipeline commute with the global causal structure of IGSOA. | Π is the **unique order-preserving functor** from the semantic category to a poset of causal values. For any objects A, B in the category: If A →_f B, then Π(A) ≤ Π(B). Furthermore, Π uniquely satisfies the commutation condition: **Π(Φ(δ A)) = eval(δA)**. By this property, Π is the unique left Kan extension of evaluation across semantic projection. |

### Theorem (Canonical Form)

**Π is the unique functor**

Π : Box → CausalOrder

such that:

1. **Causal Preservation**

   A ≺ B ⇒ Π(A) ≤ Π(B)

2. **Semantic Consistency**

   Π(Φ(B)) = Φ_*(Π(B))

   (Π commutes with semantic projection)

3. **Deviation Compatibility**

   Π(δB) = causal effect of deviation

   (Π removes only non-causal components)

4. **Pipeline Commutation**

   Π∘Φ∘δ = Π∘δ and Π∘Φ = Π

   (semantic form does not alter causal truth)

5. **Uniqueness**

   Π is the **only** such functor satisfying 1–4 on the IGSOA category of Boxes.

**Therefore, Π is the canonical connector that converts δ-geometry and Φ-form into ordered causal actuality.**

---

## Category-Theoretic Proof of the Π Connector Theorem

### Setup

Let:
- **𝔅** = the IGSOA category of Boxes
- **𝔠** = the thin category (poset) of causal values
- **δ, Φ : 𝔅 → 𝔅** endofunctors representing deviation and semantic projection
- **eval : 𝔅 → 𝔠** a primitive evaluation functional on generators

We will show:

**There exists a unique functor**

Π : 𝔅 → 𝔠

satisfying **Causal Preservation**, **Φ-Compatibility**, **δ-Compatibility**, **Pipeline Commutation**, and **Functoriality**.

The five required axioms are:

1. A ≺ B ⇒ Π(A) ≤ Π(B)
2. Π∘Φ = Π
3. Π(δB) = δ^#(Π(B))
4. Π∘Φ∘δ = Π∘δ
5. Π is a functor

We prove existence and uniqueness in three stages.

### I. Existential Construction of Π

#### 1. Π on Objects

##### 1.1. Construct Π as a left Kan extension

Define Π to be the **left Kan extension of eval along Φ**:

Π := Lan_Φ(eval)

Since Φ : 𝔅 → 𝔅 is an endofunctor and eval : 𝔅 → 𝔠 is a functor to a cocomplete thin category, the left Kan extension **exists**.

Explicitly, for any object B ∈ Ob(𝔅):

Π(B) = colim_{Φ(X)→B} eval(X)

Because 𝔠 is a **poset**, colimits reduce to **least upper bounds**:

Π(B) = sup{ eval(X) : Φ(X) → B }

Thus Π exists **objectwise**.

##### 1.2. Causal completeness

IGSOA guarantees that for each Box B, the set {X : Φ(X) → B} is nonempty. Thus Π(B) is always defined.

#### 2. Π on Morphisms

Let f : A → B be any morphism in 𝔅.

Since Φ is functorial, any arrow Φ(X) → A →_f B induces a corresponding arrow into B.

Thus Π acts on morphisms via:

Π(f): Π(A) → Π(B)

defined by the universal property of the colimit. Because 𝔠 is a poset, this is **the unique monotone map** respecting the relation induced by f.

Thus Π is defined as a functor.

### II. Verification of the Required IGSOA Axioms

#### Axiom 1: Causal Preservation

IGSOA defines a base causal relation A ≺ B. A generating arrow A → B exists in 𝔅.

Since Π is a functor into a poset:

A → B ⇒ Π(A) ≤ Π(B)

Hence causal monotonicity holds automatically.

#### Axiom 2: Φ-Compatibility

We must show:

Π∘Φ = Π

Since Π = Lan_Φ(eval):

Π(Φ(B)) = colim_{Φ(X)→Φ(B)} eval(X)

But Φ is an endofunctor on 𝔅 and preserves the comma category:

Φ(X) → Φ(B) ⟺ X → B

Thus:

Π(Φ(B)) = colim_{X→B} eval(X) = Π(B)

**Therefore** Π∘Φ = Π.

#### Axiom 3: δ-Compatibility

IGSOA requires:

Π(δB) = δ^#(Π(B))

δ acts on Boxes; δ^# is the induced action on causal values.

Since Π is a left Kan extension and δ is an endofunctor, the induced morphism δ : X → B produces:

Π(δB) = sup{ eval(X) : Φ(X) → δB }

But δ and Φ commute up to naturality in IGSOA:

Φ(δX) → δB ⇔ Φ(X) → B

Thus:

Π(δB) = sup{ eval(δX) : X → B } = sup{ δ^#(eval(X)) : X → B } = δ^#(sup eval(X)) = δ^#(Π(B))

Thus δ-compatibility holds.

#### Axiom 4: Pipeline Commutation

We must show:

Π∘Φ∘δ = Π∘δ

Since Π∘Φ = Π:

Π(Φ(δB)) = Π(δB)

This is exactly the desired commutation.

Thus, the δ → Φ → Π pipeline is **strictly associative** under Π.

#### Axiom 5: Functoriality

Already established in construction (Section I.2). Π preserves identity and composition because colimits in posets are functorial.

Therefore Π is a functor.

### III. Uniqueness of Π

Suppose there exists another functor

Π' : 𝔅 → 𝔠

satisfying the same axioms.

#### 1. Both Π and Π′ agree on Φ

Since Π∘Φ = Π and Π′∘Φ = Π′, any object B satisfies:

Π(B) = Π(Φ(B)), Π′(B) = Π′(Φ(B))

Thus equality is determined by their behavior on the comma category (Φ ↓ B).

#### 2. Both agree on δ via δ-compatibility

Π(δB) = δ^#(Π(B)), Π′(δB) = δ^#(Π′(B))

Thus if Π(B) = Π′(B), then Π(δB) = Π′(δB). By induction on δ-chains, Π and Π′ agree on all δ-iterates.

#### 3. Both preserve the causal base relation

Because 𝔠 is a poset, any two functors that preserve all generating arrows must be equal:

For every f : A → B:

Π(A) ≤ Π(B), Π′(A) ≤ Π′(B)

If Π and Π′ differ at any object, then monotonicity fails for one of them. Contradiction.

#### 4. Both Π and Π′ satisfy the same universal mapping property

Π is the left Kan extension Lan_Φ(eval). If Π′ satisfies the same axioms, then by the universal property of a left Kan extension:

Π′ ≅ Π

But 𝔠 is a poset, so natural isomorphism reduces to equality:

Π′ = Π.

### Conclusion

**Π is the unique functor** from the IGSOA Box category to the causal-order category that preserves causal relations, commutes with projection Φ, is compatible with deviation δ, and makes the δ → Φ → Π pipeline commute strictly.

This completes the category-theoretic proof.

---

## Sealed Axiom Box — Π (Canonical Evaluation / Causal Order Functor)

### MBC-4.0 / IGSOA Official Standard

#### Operator Name: Π — *The Canonical Evaluator*

**Operator Type:** Functor
**Domain:** `Box`
**Codomain:** `CausalOrder` (thin category / poset)
**Symbol:** Π
**JSON Key:** `"pi_evaluation"`

### I. Core Axiom (Π-Functor Axiom)

**Π is the unique functor Π : Box → CausalOrder** that assigns to each Box its *causally realizable evaluation* and preserves IGSOA's dependency relations.

Formally:

Π(g∘f) = Π(g)∘Π(f), Π(id_B) = id_{Π(B)}.

### II. Causal Preservation Axiom

For all Boxes A, B:

A ≺ B ⇒ Π(A) ≤ Π(B).

(Preserves the global IGSOA causal order.)

### III. Φ-Compatibility Axiom

Π commutes with semantic projection:

Π(Φ(B)) = Π(B).

(Π extracts only the causally relevant semantic form.)

### IV. δ-Compatibility Axiom

Π extracts the causally relevant component of deviation:

Π(δB) = δ^#(Π(B)).

(δ^# = induced deviation on causal values.)

### V. Pipeline Commutation Axiom

Π makes the δ → Φ → Π pipeline strictly commute:

Π∘Φ∘δ = Π∘δ, Π∘Φ = Π.

(No collapse; only evaluation.)

### VI. Uniqueness Axiom

**Π is the terminal evaluation functor.** Any functor F : Box → CausalOrder obeying Axioms I–V must satisfy:

F = Π.

(Uniqueness guaranteed by the Kan-extension property and thinness of the codomain.)

### VII. Canonical IGSOA Interpretation

Π is the **Causal Connector**: the operator that converts δ-geometry and Φ-form into *actual causal outcome*. It is the final stage of the IGSOA pipeline:

δ ⟶ Φ ⟶ Π.

Π determines **what happens**, **why it happens**, and **in what causal order**, without destroying semantic structure.

---

## MBC-4.0 JSON Operator Specification

### δ-Operators

```json
{
  "delta_operators": {
    "delta": {
      "symbol": "δ",
      "type": "first_order",
      "rank": 1,
      "description": "Base deviation operator; initiates asymmetry and curvature.",
      "composes_with": ["delta_squared", "phi_of_delta", "delta_of_phi", "pi_of_delta"],
      "formal_equivalent": "first_order_derivative"
    },
    "delta_squared": {
      "symbol": "δ²",
      "type": "second_order",
      "rank": 1,
      "description": "Curvature-sensitive deviation operator (second derivative).",
      "formal_equivalent": "second_derivative"
    },
    "delta_adjoint": {
      "symbol": "δ*",
      "type": "adjoint",
      "rank": 1,
      "description": "Adjoint deviation; reverse semantic flow.",
      "formal_equivalent": "adjoint_differential_operator"
    },
    "delta_jacobian": {
      "symbol": "Jδ",
      "type": "tensor",
      "rank": 2,
      "description": "Jacobian of deviation; local semantic deformation matrix.",
      "components": ["det", "trace"],
      "formal_equivalent": "jacobian_matrix"
    },
    "delta_laplacian": {
      "symbol": "Δδ",
      "type": "second_order",
      "rank": 0,
      "description": "Deviation Laplacian; semantic diffusion and smoothing operator.",
      "formal_equivalent": "laplacian"
    },
    "delta_weitzenbock": {
      "symbol": "Wδ",
      "type": "torsion_operator",
      "rank": 0,
      "description": "Torsion-weighted deviation (Weitzenböck operator).",
      "identity": "Wδ = Δδ + Tδ",
      "formal_equivalent": "weitzenbock_operator"
    },
    "delta_of_phi": {
      "symbol": "δ ∘ Φ",
      "type": "mixed",
      "rank": 1,
      "description": "Deviation of projection.",
      "formal_equivalent": "derivative_of_projection"
    },
    "phi_of_delta": {
      "symbol": "Φ ∘ δ",
      "type": "mixed",
      "rank": 1,
      "description": "Projection of deviation.",
      "formal_equivalent": "projected_derivative"
    },
    "pi_of_delta": {
      "symbol": "Π ∘ δ",
      "type": "mixed",
      "rank": 1,
      "description": "Causal evaluation of deviation.",
      "formal_equivalent": "evaluated_derivative"
    },
    "delta_tensor": {
      "symbol": "δ ⊗ δ",
      "type": "tensor",
      "rank": 2,
      "description": "Deviation tensor; interaction of deviation directions.",
      "formal_equivalent": "tensor_product"
    }
  }
}
```

### Π Evaluation Functor

```json
{
  "pi_evaluation": {
    "symbol": "Π",
    "type": "functor",
    "domain": "Box",
    "codomain": "CausalOrder",
    "description": "Canonical evaluation and causal order functor. Assigns each Box a causally realizable outcome while preserving order and dependency.",
    "axioms": {
      "functoriality": "Π(g∘f) = Π(g) ∘ Π(f)",
      "identity": "Π(id_B) = id_{Π(B)}",
      "order_preservation": "A ≺ B implies Π(A) ≤ Π(B)",
      "delta_compatibility": "Π(δB) returns the causally relevant deviation",
      "phi_compatibility": "Π(Φ(B)) evaluates the projected semantic form",
      "collapse_free": "Evaluation does not erase structure"
    }
  }
}
```

### Π Connector Theorem

```json
{
  "pi_connector_theorem": {
    "name": "Π Connector Theorem",
    "description": "Π is the unique functor from Box to CausalOrder that preserves causal adjacency, commutes with semantic projection Φ, and extracts the causally-relevant component of deviation δ.",
    "conditions": {
      "causal_preservation": "A ≺ B implies Π(A) ≤ Π(B)",
      "phi_compatibility": "Π(Φ(B)) = Π(B)",
      "delta_compatibility": "Π(δB) gives causally relevant effect",
      "pipeline_commutation": "Π∘Φ∘δ = Π∘δ and Π∘Φ = Π",
      "uniqueness": "no other functor satisfies these conditions"
    }
  }
}
```

---

## Dictionary Reference

### For every operator, include:

- **Name**
- **Symbol**
- **IGSOA Definition**
- **Standard Geometry Equivalent**
- **Type** (order, tensor rank)
- **Role / interpretation**
- **Allowed compositions**
- **JSON key (for MBC-4.0)**
