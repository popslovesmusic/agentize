# Fully Diagrammatic Commutative Squares and Cubes

## Overview

This document provides canonical, fully diagrammatic commutative squares and cubes showing functors, natural transformations, and naturality conditions. All diagrams follow the MBC-4.0 standard and use dual-column labeling for IGSOA and Standard Category Theory terms.

### Dual-Column Label Key

| IGSOA Term | Standard Category Term |
|------------|------------------------|
| Box-state | Object |
| δ/Φ/Π map | Morphism |
| Operator Layer | Functor |
| Layer-transition | Natural transformation |

## 1. The Canonical Commutative Square (Naturality Square)

### Diagram: Functors F, G and natural transformation η : F ⇒ G

```mermaid
graph LR
    A0["F(A)"] -->| "F(f)" | A1["F(B)"];
    A2["G(A)"] -->| "G(f)" | A3["G(B)"];
    A0 -->| "η_A" | A2;
    A1 -->| "η_B" | A3;
```

### Naturality Condition

G(f) ∘ η_A = η_B ∘ F(f)

This is the primitive for every IGSOA operator interaction: δ-flow, Φ-projection, Π-evaluation, μ-weighting, Σ-contraction, Θ-routing.

## 2. The Full Commutative Cube (Three Functors, Two Naturalities)

This cube shows:
- Bottom face: functors F → G via η
- Top face: functors H ∘ F → H ∘ G via Hη
- Vertical faces: naturality of η w.r.t. f, and functoriality of H

### Diagram

```mermaid
flowchart TD
    %% Bottom face objects
    F_A["F(A)"] -->| "F(f)" | F_B["F(B)"]
    G_A["G(A)"] -->| "G(f)" | G_B["G(B)"]
    F_A -->| "η_A" | G_A
    F_B -->| "η_B" | G_B

    %% Top face objects (apply H)
    HF_A["H(F(A))"] -->| "H(F(f))" | HF_B["H(F(B))"]
    HG_A["H(G(A))"] -->| "H(G(f))" | HG_B["H(G(B))"]
    HF_A -->| "H(η_A)" | HG_A
    HF_B -->| "H(η_B)" | HG_B

    %% Vertical edges: application of H
    F_A -->| "H" | HF_A
    F_B -->| "H" | HF_B
    G_A -->| "H" | HG_A
    G_B -->| "H" | HG_B
```

This cube is strictly commutative if H is a functor and η is a natural transformation.

## 3. The Naturality Cube Condition (All 6 Faces Commute)

For any morphism f: A → B, all faces commute:

### Bottom Face
G(f) ∘ η_A = η_B ∘ F(f)

### Top Face
H(G(f)) ∘ H(η_A) = H(η_B) ∘ H(F(f))

### Front-Left Face
H(F(f)) ∘ H = H ∘ F(f)

### Front-Right Face
H(G(f)) ∘ H = H ∘ G(f)

### Back-Left Face
H(η_A) ∘ H(F(f)) = H(G(f)) ∘ H(η_A)

### Back-Right Face
H(η_B) ∘ H(F(f)) = H(G(f)) ∘ H(η_B)

In IGSOA, this is exactly the condition that δ-flow, Φ-projection, and Π-evaluation can be lifted through a mode-transform functor H (e.g., μ-weighting layer, Σ-contraction context, Θ-polarity router).

## 4. Tri-Unity Compatible Version (δ, Φ, Π)

### Diagram: F = δ-Layer, G = Φ-Layer, H = Π-Layer

```mermaid
flowchart TD
    %% Bottom layer: δ → Φ
    deltaA["δ(A)"] -->| "δ(f)" | deltaB["δ(B)"]
    phiA["Φ(A)"] -->| "Φ(f)" | phiB["Φ(B)"]
    deltaA -->| "η_A (δ→Φ)" | phiA
    deltaB -->| "η_B (δ→Φ)" | phiB

    %% Top layer: Π∘δ → Π∘Φ
    PdeltaA["Πδ(A)"] -->| "Πδ(f)" | PdeltaB["Πδ(B)"]
    PphiA["ΠΦ(A)" ] -->| "ΠΦ(f)" | PphiB["ΠΦ(B)"]
    PdeltaA -->| "Π(η_A)" | PphiA
    PdeltaB -->| "Π(η_B)" | PphiB

    %% Vertical lifting
    deltaA -->| "Π" | PdeltaA
    deltaB -->| "Π" | PdeltaB
    phiA -->| "Π" | PphiA
    phiB -->| "Π" | PphiB
```

This is the Tri-Unity cube in strict categorical form.

## 5. Ultra-General Operator Cube Template for MBC-4.0 JSON

General cube schema for extraction agents:

```json
{
  "commutative_cube": {
    "functors": ["F", "G", "H"],
    "natural_transformation": "eta: F ⇒ G",
    "objects": ["A", "B"],
    "morphisms": ["f: A → B"],
    "faces_commute": {
      "bottom":  "G(f) ∘ η_A = η_B ∘ F(f)",
      "top":     "H(G(f)) ∘ H(η_A) = H(η_B) ∘ H(F(f)",
      "left":    "...",
      "right":   "...",
      "front":   "...",
      "back":    "..."
    }
  }
}
```

# MBC-4.0 JSON Schema for Commutative Diagrams

## Schema Overview

Version: MBC-4.0.CommDiag.v1

This schema supports:
- Commutative Squares
- Commutative Cubes
- Higher-dimensional extensions (n-cubes)

It enforces:
- Functors
- Natural transformations
- Objects
- Morphisms
- Faces (each with a commutation law)

## Complete Schema Definition

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "MBC-4.0 Commutative Diagram Schema",
  "type": "object",
  "required": ["diagram_type", "objects", "morphisms", "functors", "faces"],
  "properties": {
    "diagram_type": {
      "type": "string",
      "enum": ["square", "cube", "n-cube"]
    },

    "objects": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id"],
        "properties": {
          "id": { "type": "string" },
          "label": { "type": "string" },
          "semantic_role": {
            "type": "string",
            "enum": ["state", "box", "operator-output",
                     "δ-layer", "Φ-layer", "Π-layer", "μ-layer",
                     "arbitrary"]
          }
        }
      }
    },

    "morphisms": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "from", "to"],
        "properties": {
          "id": { "type": "string" },
          "from": { "type": "string" },
          "to": { "type": "string" },
          "label": { "type": "string" },
          "semantic_type": {
            "type": "string",
            "enum": ["map", "δ", "Φ", "Π", "μ", "Σ", "Θ", "functor-map"]
          }
        }
      }
    },

    "functors": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id"],
        "properties": {
          "id": { "type": "string" },
          "label": { "type": "string" },
          "kind": {
            "type": "string",
            "enum": ["δ", "Φ", "Π", "μ", "Σ", "Θ", "general"]
          }
        }
      }
    },

    "natural_transformations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "from_functor", "to_functor"],
        "properties": {
          "id": { "type": "string" },
          "from_functor": { "type": "string" },
          "to_functor": { "type": "string" },
          "components": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["object", "morphism"],
              "properties": {
                "object": { "type": "string" },
                "morphism": { "type": "string" }
              }
            }
          }
        }
      }
    },

    "faces": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "boundary", "commutes"],
        "properties": {
          "id": { "type": "string" },
          "dimension": { "type": "integer", "enum": [2, 3] },
          "boundary": {
            "type": "array",
            "items": { "type": "string" }
          },
          "commutes": {
            "type": "object",
            "required": ["equation"],
            "properties": {
              "equation": { "type": "string" },
              "semantic_layer": {
                "type": "string",
                "enum": ["δ", "Φ", "Π", "μ", "Σ", "Θ", "general"]
              }
            }
          }
        }
      }
    }
  }
}
```

# Worked Examples

## 1. Tri-Unity Square (δ → Φ via η)

Diagram type: square

Meaning: The δ-layer and Φ-layer act functorially, and η encodes the δ→Φ projection.

```json
{
  "diagram_type": "square",

  "objects": [
    { "id": "FA", "label": "δ(A)", "semantic_role": "δ-layer" },
    { "id": "FB", "label": "δ(B)", "semantic_role": "δ-layer" },
    { "id": "GA", "label": "Φ(A)", "semantic_role": "Φ-layer" },
    { "id": "GB", "label": "Φ(B)", "semantic_role": "Φ-layer" }
  ],

  "morphisms": [
    { "id": "delta_f", "from": "FA", "to": "FB", "label": "δ(f)", "semantic_type": "δ" },
    { "id": "phi_f",   "from": "GA", "to": "GB", "label": "Φ(f)", "semantic_type": "Φ" },
    { "id": "eta_A",   "from": "FA", "to": "GA", "label": "η_A", "semantic_type": "map" },
    { "id": "eta_B",   "from": "FB", "to": "GB", "label": "η_B", "semantic_type": "map" }
  ],

  "functors": [
    { "id": "delta", "label": "δ", "kind": "δ" },
    { "id": "phi",   "label": "Φ", "kind": "Φ" }
  ],

  "natural_transformations": [
    {
      "id": "eta",
      "from_functor": "delta",
      "to_functor": "phi",
      "components": [
        { "object": "A", "morphism": "eta_A" },
        { "object": "B", "morphism": "eta_B" }
      ]
    }
  ],

  "faces": [
    {
      "id": "naturality_square",
      "dimension": 2,
      "boundary": ["delta_f", "eta_B", "phi_f", "eta_A"],
      "commutes": {
        "equation": "Φ(f) ∘ η_A = η_B ∘ δ(f)",
        "semantic_layer": "general"
      }
    }
  ]
}
```

## 2. Tri-Unity Cube (δ → Φ lifted through Π)

Diagram type: cube

Meaning: Π lifts the δ→Φ natural transformation; all 6 faces commute.

```json
{
  "diagram_type": "cube",

  "objects": [
    { "id": "FA",    "label": "δ(A)",   "semantic_role": "δ-layer" },
    { "id": "FB",    "label": "δ(B)",   "semantic_role": "δ-layer" },
    { "id": "GA",    "label": "Φ(A)",   "semantic_role": "Φ-layer" },
    { "id": "GB",    "label": "Φ(B)",   "semantic_role": "Φ-layer" },

    { "id": "PFA",   "label": "Πδ(A)",  "semantic_role": "Π-layer" },
    { "id": "PFB",   "label": "Πδ(B)",  "semantic_role": "Π-layer" },
    { "id": "PGA",   "label": "ΠΦ(A)",  "semantic_role": "Π-layer" },
    { "id": "PGB",   "label": "ΠΦ(B)",  "semantic_role": "Π-layer" }
  ],

  "morphisms": [
    { "id": "delta_f", "from": "FA", "to": "FB", "label": "δ(f)", "semantic_type": "δ" },
    { "id": "phi_f",   "from": "GA", "to": "GB", "label": "Φ(f)", "semantic_type": "Φ" },
    { "id": "eta_A",   "from": "FA", "to": "GA", "label": "η_A", "semantic_type": "map" },
    { "id": "eta_B",   "from": "FB", "to": "GB", "label": "η_B", "semantic_type": "map" },

    { "id": "P_delta_f", "from": "PFA", "to": "PFB", "label": "Πδ(f)", "semantic_type": "Π" },
    { "id": "P_phi_f",   "from": "PGA", "to": "PGB", "label": "ΠΦ(f)", "semantic_type": "Π" },

    { "id": "P_eta_A",   "from": "PFA", "to": "PGA", "label": "Π(η_A)", "semantic_type": "map" },
    { "id": "P_eta_B",   "from": "PFB", "to": "PGB", "label": "Π(η_B)", "semantic_type": "map" }
  ],

  "functors": [
    { "id": "delta", "label": "δ", "kind": "δ" },
    { "id": "phi",   "label": "Φ", "kind": "Φ" },
    { "id": "pi",    "label": "Π", "kind": "Π" }
  ],

  "natural_transformations": [
    {
      "id": "eta",
      "from_functor": "delta",
      "to_functor": "phi",
      "components": [
        { "object": "A", "morphism": "eta_A" },
        { "object": "B", "morphism": "eta_B" }
      ]
    }
  ],

  "faces": [
    {
      "id": "bottom_face",
      "dimension": 2,
      "boundary": ["delta_f", "eta_B", "phi_f", "eta_A"],
      "commutes": {
        "equation": "Φ(f) ∘ η_A = η_B ∘ δ(f)",
        "semantic_layer": "general"
      }
    },
    {
      "id": "top_face",
      "dimension": 2,
      "boundary": ["P_delta_f", "P_eta_B", "P_phi_f", "P_eta_A"],
      "commutes": {
        "equation": "ΠΦ(f) ∘ Π(η_A) = Π(η_B) ∘ Πδ(f)",
        "semantic_layer": "Π"
      }
    },
    {
      "id": "front_left",
      "dimension": 2,
      "boundary": ["FA", "PFA", "PGA", "GA"],
      "commutes": {
        "equation": "Π(δ(A)) = Π(Φ(A)) ∘ η_A",
        "semantic_layer": "general"
      }
    },
    {
      "id": "front_right",
      "dimension": 2,
      "boundary": ["FB", "PFB", "PGB", "GB"],
      "commutes": {
        "equation": "Π(δ(B)) = Π(Φ(B)) ∘ η_B",
        "semantic_layer": "general"
      }
    }
  ]
}
```

## 3. Tri-Unity + μ Hypercube (δ → Φ → Π with μ-weighting layer)

This is a 4-dimensional cube (tesseract face) showing:
- Face 1: δ → Φ (naturality)
- Face 2: Φ → Π (lift)
- Face 3: δ → Π (composite)
- Face 4: μ lifts all three
- Face 5-6: cross-commutation faces

This demonstrates μ as a functorial local-density weighting that preserves all Tri-Unity relations.

```json
{
  "diagram_type": "n-cube",

  "objects": [
    { "id": "FA",   "label": "δ(A)",   "semantic_role": "δ-layer" },
    { "id": "GA",   "label": "Φ(A)",   "semantic_role": "Φ-layer" },
    { "id": "PA",   "label": "Π(A)",   "semantic_role": "Π-layer" },
    { "id": "mFA",  "label": "μδ(A)",  "semantic_role": "μ-layer" },
    { "id": "mGA",  "label": "μΦ(A)",  "semantic_role": "μ-layer" },
    { "id": "mPA",  "label": "μΠ(A)",  "semantic_role": "μ-layer" },

    { "id": "FB",   "label": "δ(B)",   "semantic_role": "δ-layer" },
    { "id": "GB",   "label": "Φ(B)",   "semantic_role": "Φ-layer" },
    { "id": "PB",   "label": "Π(B)",   "semantic_role": "Π-layer" },
    { "id": "mFB",  "label": "μδ(B)",  "semantic_role": "μ-layer" },
    { "id": "mGB",  "label": "μΦ(B)",  "semantic_role": "μ-layer" },
    { "id": "mPB",  "label": "μΠ(B)",  "semantic_role": "μ-layer" }
  ],

  "morphisms": [
    { "id": "delta_f", "from": "FA", "to": "FB", "label": "δ(f)", "semantic_type": "δ" },
    { "id": "phi_f",   "from": "GA", "to": "GB", "label": "Φ(f)", "semantic_type": "Φ" },
    { "id": "pi_f",    "from": "PA", "to": "PB", "label": "Π(f)", "semantic_type": "Π" },

    { "id": "etaA",  "from": "FA", "to": "GA", "label": "η_A", "semantic_type": "map" },
    { "id": "thetaA", "from": "GA", "to": "PA", "label": "τ_A: Φ→Π", "semantic_type": "map" },

    { "id": "etaB",  "from": "FB", "to": "GB", "label": "η_B", "semantic_type": "map" },
    { "id": "thetaB", "from": "GB", "to": "PB", "label": "τ_B: Φ→Π", "semantic_type": "map" },

    { "id": "mu_delta_f", "from": "mFA", "to": "mFB", "label": "μδ(f)", "semantic_type": "μ" },
    { "id": "mu_phi_f",   "from": "mGA", "to": "mGB", "label": "μφ(f)", "semantic_type": "μ" },
    { "id": "mu_pi_f",    "from": "mPA", "to": "mPB", "label": "μπ(f)", "semantic_type": "μ" },

    { "id": "mu_etaA",   "from": "mFA", "to": "mGA", "label": "μ(η_A)", "semantic_type": "map" },
    { "id": "mu_thetaA", "from": "mGA", "to": "mPA", "label": "μ(τ_A)", "semantic_type": "map" },

    { "id": "mu_etaB",   "from": "mFB", "to": "mGB", "label": "μ(η_B)", "semantic_type": "map" },
    { "id": "mu_thetaB", "from": "mGB", "to": "mPB", "label": "μ(τ_B)", "semantic_type": "map" }
  ],

  "functors": [
    { "id": "delta", "label": "δ", "kind": "δ" },
    { "id": "phi",   "label": "Φ", "kind": "Φ" },
    { "id": "pi",    "label": "Π", "kind": "Π" },
    { "id": "mu",    "label": "μ", "kind": "μ" }
  ],

  "natural_transformations": [
    {
      "id": "eta",
      "from_functor": "delta",
      "to_functor": "phi",
      "components": [
        { "object": "A", "morphism": "etaA" },
        { "object": "B", "morphism": "etaB" }
      ]
    },
    {
      "id": "tau",
      "from_functor": "phi",
      "to_functor": "pi",
      "components": [
        { "object": "A", "morphism": "thetaA" },
        { "object": "B", "morphism": "thetaB" }
      ]
    }
  ],

  "faces": [
    {
      "id": "delta_to_phi",
      "dimension": 2,
      "boundary": ["delta_f", "etaB", "phi_f", "etaA"],
      "commutes": {
        "equation": "Φ(f) ∘ η_A = η_B ∘ δ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "phi_to_pi",
      "dimension": 2,
      "boundary": ["phi_f", "thetaB", "pi_f", "thetaA"],
      "commutes": {
        "equation": "Π(f) ∘ τ_A = τ_B ∘ Φ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "delta_to_pi_composite",
      "dimension": 2,
      "boundary": ["delta_f", "thetaB", "pi_f", "etaA"],
      "commutes": {
        "equation": "Π(f) ∘ (τ_A ∘ η_A) = (τ_B ∘ η_B) ∘ δ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "mu_lift_delta_phi",
      "dimension": 2,
      "boundary": ["mu_delta_f", "mu_etaB", "mu_phi_f", "mu_etaA"],
      "commutes": {
        "equation": "μφ(f) ∘ μ(η_A) = μ(η_B) ∘ μδ(f)",
        "semantic_layer": "μ"
      }
    },

    {
      "id": "mu_lift_phi_pi",
      "dimension": 2,
      "boundary": ["mu_phi_f", "mu_thetaB", "mu_pi_f", "mu_thetaA"],
      "commutes": {
        "equation": "μπ(f) ∘ μ(τ_A) = μ(τ_B) ∘ μφ(f)",
        "semantic_layer": "μ"
      }
    },

    {
      "id": "mu_lift_delta_pi_composite",
      "dimension": 2,
      "boundary": ["mu_delta_f", "mu_thetaB", "mu_pi_f", "mu_etaA"],
      "commutes": {
        "equation": "μπ(f) ∘ μ(τ_A ∘ η_A) = μ(τ_B ∘ η_B) ∘ μδ(f)",
        "semantic_layer": "μ"
      }
    }
  ]
}
```

## 4. Tri-Unity + μ + Σ "5-Functor Pentacube"

This represents five functors forming a 5-dimensional commutative hypercube:
- δ — deviation / geometric adjacency
- Φ — projection / semantic shaping
- Π — evaluation / causal truth
- μ — micro-adjacency weighting / metric density
- Σ — semantic contraction / summation

### Functor Chain

δ ⇒_η Φ ⇒_τ Π ⇒_κ μ ⇒_σ Σ

Each transformation is natural, therefore each adds a new dimension.

```json
{
  "diagram_type": "n-cube",

  "objects": [
    { "id": "dA",  "label": "δ(A)",   "semantic_role": "δ-layer" },
    { "id": "fA",  "label": "Φ(A)",   "semantic_role": "Φ-layer" },
    { "id": "pA",  "label": "Π(A)",   "semantic_role": "Π-layer" },
    { "id": "mA",  "label": "μ(A)",   "semantic_role": "μ-layer" },
    { "id": "sA",  "label": "Σ(A)",   "semantic_role": "Σ-layer" },

    { "id": "dB",  "label": "δ(B)",   "semantic_role": "δ-layer" },
    { "id": "fB",  "label": "Φ(B)",   "semantic_role": "Φ-layer" },
    { "id": "pB",  "label": "Π(B)",   "semantic_role": "Π-layer" },
    { "id": "mB",  "label": "μ(B)",   "semantic_role": "μ-layer" },
    { "id": "sB",  "label": "Σ(B)",   "semantic_role": "Σ-layer" }
  ],

  "morphisms": [
    { "id": "d_f",  "from": "dA", "to": "dB", "label": "δ(f)", "semantic_type": "δ" },
    { "id": "f_f",  "from": "fA", "to": "fB", "label": "Φ(f)", "semantic_type": "Φ" },
    { "id": "p_f",  "from": "pA", "to": "pB", "label": "Π(f)", "semantic_type": "Π" },
    { "id": "m_f",  "from": "mA", "to": "mB", "label": "μ(f)", "semantic_type": "μ" },
    { "id": "s_f",  "from": "sA", "to": "sB", "label": "Σ(f)", "semantic_type": "Σ" },

    { "id": "etaA",   "from": "dA", "to": "fA", "label": "η_A", "semantic_type": "map" },
    { "id": "etaB",   "from": "dB", "to": "fB", "label": "η_B", "semantic_type": "map" },

    { "id": "tauA",   "from": "fA", "to": "pA", "label": "τ_A", "semantic_type": "map" },
    { "id": "tauB",   "from": "fB", "to": "pB", "label": "τ_B", "semantic_type": "map" },

    { "id": "kapA",   "from": "pA", "to": "mA", "label": "κ_A", "semantic_type": "map" },
    { "id": "kapB",   "from": "pB", "to": "mB", "label": "κ_B", "semantic_type": "map" },

    { "id": "sigA",   "from": "mA", "to": "sA", "label": "σ_A", "semantic_type": "map" },
    { "id": "sigB",   "from": "mB", "to": "sB", "label": "σ_B", "semantic_type": "map" }
  ],

  "functors": [
    { "id": "delta", "label": "δ", "kind": "δ" },
    { "id": "phi",   "label": "Φ", "kind": "Φ" },
    { "id": "pi",    "label": "Π", "kind": "Π" },
    { "id": "mu",    "label": "μ", "kind": "μ" },
    { "id": "sigma", "label": "Σ", "kind": "Σ" }
  ],

  "natural_transformations": [
    {
      "id": "eta",
      "from_functor": "delta",
      "to_functor": "phi",
      "components": [
        { "object": "A", "morphism": "etaA" },
        { "object": "B", "morphism": "etaB" }
      ]
    },
    {
      "id": "tau",
      "from_functor": "phi",
      "to_functor": "pi",
      "components": [
        { "object": "A", "morphism": "tauA" },
        { "object": "B", "morphism": "tauB" }
      ]
    },
    {
      "id": "kappa",
      "from_functor": "pi",
      "to_functor": "mu",
      "components": [
        { "object": "A", "morphism": "kapA" },
        { "object": "B", "morphism": "kapB" }
      ]
    },
    {
      "id": "sigma_nat",
      "from_functor": "mu",
      "to_functor": "sigma",
      "components": [
        { "object": "A", "morphism": "sigA" },
        { "object": "B", "morphism": "sigB" }
      ]
    }
  ],

  "faces": [

    {
      "id": "delta_to_phi",
      "dimension": 2,
      "boundary": ["d_f", "etaB", "f_f", "etaA"],
      "commutes": {
        "equation": "Φ(f) ∘ η_A = η_B ∘ δ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "phi_to_pi",
      "dimension": 2,
      "boundary": ["f_f", "tauB", "p_f", "tauA"],
      "commutes": {
        "equation": "Π(f) ∘ τ_A = τ_B ∘ Φ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "pi_to_mu",
      "dimension": 2,
      "boundary": ["p_f", "kapB", "m_f", "kapA"],
      "commutes": {
        "equation": "μ(f) ∘ κ_A = κ_B ∘ Π(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "mu_to_sigma",
      "dimension": 2,
      "boundary": ["m_f", "sigB", "s_f", "sigA"],
      "commutes": {
        "equation": "Σ(f) ∘ σ_A = σ_B ∘ μ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "delta_to_pi_composite",
      "dimension": 2,
      "boundary": ["d_f", "tauB", "p_f", "etaA"],
      "commutes": {
        "equation": "Π(f) ∘ (τ_A ∘ η_A) = (τ_B ∘ η_B) ∘ δ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "delta_to_mu_composite",
      "dimension": 2,
      "boundary": ["d_f", "kapB", "m_f", "etaA"],
      "commutes": {
        "equation": "μ(f) ∘ (κ_A ∘ τ_A ∘ η_A) = (κ_B ∘ τ_B ∘ η_B) ∘ δ(f)",
        "semantic_layer": "general"
      }
    },

    {
      "id": "delta_to_sigma_composite",
      "dimension": 2,
      "boundary": ["d_f", "sigB", "s_f", "etaA"],
      "commutes": {
        "equation": "Σ(f) ∘ (σ_A ∘ κ_A ∘ τ_A ∘ η_A) = (σ_B ∘ κ_B ∘ τ_B ∘ η_B) ∘ δ(f)",
        "semantic_layer": "Σ"
      }
    },

    {
      "id": "phi_to_mu_composite",
      "dimension": 2,
      "boundary": ["f_f", "kapB", "m_f", "tauA"],
      "commutes": {
        "equation": "μ(f) ∘ (κ_A ∘ τ_A) = (κ_B ∘ τ_B) ∘ Φ(f)",
        "semantic_layer": "μ"
      }
    },

    {
      "id": "phi_to_sigma_composite",
      "dimension": 2,
      "boundary": ["f_f", "sigB", "s_f", "tauA"],
      "commutes": {
        "equation": "Σ(f) ∘ (σ_A ∘ κ_A ∘ τ_A) = (σ_B ∘ κ_B ∘ τ_B) ∘ Φ(f)",
        "semantic_layer": "Σ"
      }
    },

    {
      "id": "pi_to_sigma_composite",
      "dimension": 2,
      "boundary": ["p_f", "sigB", "s_f", "kapA"],
      "commutes": {
        "equation": "Σ(f) ∘ (σ_A ∘ κ_A) = (σ_B ∘ κ_B) ∘ Π(f)",
        "semantic_layer": "Σ"
      }
    }

  ]
}
```

### Pentacube Structure

| Dimension | Functor | Transformation |
|-----------|---------|----------------|
| 1 | δ | identity |
| 2 | Φ | η : δ ⇒ Φ |
| 3 | Π | τ : Φ ⇒ Π |
| 4 | μ | κ : Π ⇒ μ |
| 5 | Σ | σ : μ ⇒ Σ |

The pentacube contains:
- 10 explicitly encoded faces
- 5 functors
- 5 layers of naturality
- δ → Φ → Π → μ → Σ totalized operator-flow

# MBC-4.0 Functor Interaction Table

## Dual-Column Functor Overview

| IGSOA Operator | Category Theory Term | Meaning |
|----------------|---------------------|---------|
| δ | Functor δ | Deviation / geometric gradient |
| Φ | Functor Φ | Projection into semantic form |
| Π | Functor Π | Evaluation / causal truth |
| μ | Functor μ | Micro-adjacency weighting (local metric) |
| Σ | Functor Σ | Semantic contraction / summation |

## Canonical Interaction Table (All 25 Binary Pairs)

Every cell contains the semantic effect when applying one functor after another on a Box state.

Rows = functor applied first.
Columns = functor applied second.

### IGSOA Operator Interaction Table

| ∘ | δ | Φ | Π | μ | Σ |
|---|---|---|---|---|---|
| δ | δ∘δ = δ² (2nd deviation) | δΦ (shape deformation) | δΠ (evaluated gradient) | δμ (weighted gradient) | δΣ (contracted gradient) |
| Φ | Φδ (semantic deviation) | Φ² = Φ (idempotent proj.) | ΦΠ (semantic truth-map) | Φμ (weighted projection) | ΦΣ (contracted projection) |
| Π | Πδ (evaluation of change) | ΠΦ (semantic evaluation) | Π² = Π (idempotent truth) | Πμ (evaluate weight) | ΠΣ (evaluate contraction) |
| μ | μδ (metric-adjusted δ) | μΦ (metric-adjusted Φ) | μΠ (metric-adjusted Π) | μ² = μ (local reweighting) | μΣ (weighted sum) |
| Σ | Σδ (summed gradient) | ΣΦ (summed projection) | ΣΠ (summed truth) | Σμ (summed density) | Σ² = Σ (contraction idempotent) |

### Observations

Idempotent functors: Φ² = Φ, Π² = Π, μ² = μ, Σ² = Σ

δ is not idempotent, because δ² is higher geometric deviation (2nd order).

Σ is a terminal collapse operator (semantic contraction).

δ → Φ → Π → μ → Σ forms a canonical monotone ladder.

## Machine-Readable Functor Interaction Table

```json
{
  "functor_interactions": {
    "delta": {
      "delta": "delta^2",
      "phi": "delta_phi",
      "pi": "delta_pi",
      "mu": "delta_mu",
      "sigma": "delta_sigma"
    },
    "phi": {
      "delta": "phi_delta",
      "phi": "phi",
      "pi": "phi_pi",
      "mu": "phi_mu",
      "sigma": "phi_sigma"
    },
    "pi": {
      "delta": "pi_delta",
      "phi": "pi_phi",
      "pi": "pi",
      "mu": "pi_mu",
      "sigma": "pi_sigma"
    },
    "mu": {
      "delta": "mu_delta",
      "phi": "mu_phi",
      "pi": "mu_pi",
      "mu": "mu",
      "sigma": "mu_sigma"
    },
    "sigma": {
      "delta": "sigma_delta",
      "phi": "sigma_phi",
      "pi": "sigma_pi",
      "mu": "sigma_mu",
      "sigma": "sigma"
    }
  }
}
```

## Functor Composition Rewrite Rules

This powers normalization and canonical form.

```json
{
  "functor_rewrite_rules": [
    {
      "pattern": ["phi", "phi"],
      "rewrite": ["phi"]
    },
    {
      "pattern": ["pi", "pi"],
      "rewrite": ["pi"]
    },
    {
      "pattern": ["mu", "mu"],
      "rewrite": ["mu"]
    },
    {
      "pattern": ["sigma", "sigma"],
      "rewrite": ["sigma"]
    },

    {
      "pattern": ["delta", "delta"],
      "rewrite": ["delta2"]
    },

    {
      "pattern": ["delta", "phi"],
      "rewrite": ["delta_phi"]
    },
    {
      "pattern": ["phi", "delta"],
      "rewrite": ["phi_delta"]
    },

    {
      "pattern": ["phi", "pi"],
      "rewrite": ["phi_pi"]
    },
    {
      "pattern": ["pi", "phi"],
      "rewrite": ["pi_phi"]
    },

    {
      "pattern": ["pi", "mu"],
      "rewrite": ["pi_mu"]
    },
    {
      "pattern": ["mu", "pi"],
      "rewrite": ["mu_pi"]
    },

    {
      "pattern": ["mu", "sigma"],
      "rewrite": ["mu_sigma"]
    },
    {
      "pattern": ["sigma", "mu"],
      "rewrite": ["sigma_mu"]
    }
  ]
}
```

This ensures:
- Canonical form is unique
- Every expression involving δ, Φ, Π, μ, Σ reduces
- Agents can unify operator expressions across diagrams
- Operator algebra remains consistent across volumes

## Automatic Capabilities

With the interaction table and rewrite system, agents can:

### Normalize Any Operator Chain

Example: Σ μ Π Φ δ → σ_mu_pi_phi_delta

### Infer Missing Cube Faces

Any of the 2-faces of the pentacube can be auto-filled.

### Validate Naturality

Given F and G and a proposed η, the agent checks the equations.

### Build Operator-Flow Chains

Tri-Unity extended to full 5-functor hierarchy.

### Detect Contradictions

If a document asserts Φ∘Φ ≠ Φ, the system flags it.

### Compute Canonical Operator Normal Form

This is essential for MBC-4.0 reasoning and the Box Algebra layer.
