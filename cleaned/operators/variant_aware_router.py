"""
VariantAwareRouter - Pooled Operator Variant Selection System

Automatically selects optimal operator variant based on execution context.
Resolves logical conflicts by pooling canonical + alternative formulations.

Author: MBC Framework
Date: 2025-11-28
Version: 1.0.0
"""

import json
import logging
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


# ============================================================================
# CONFIGURATION
# ============================================================================

logger = logging.getLogger(__name__)


class GeometryType(Enum):
    """Geometry classification for operator selection."""
    FLAT = "flat"
    CURVED = "curved"
    UNKNOWN = "unknown"


class AbstractionLevel(Enum):
    """Abstraction level for ψ-transformation."""
    BASE_OPERATOR = "base_operator"
    PSI_LAYER = "psi_layer"
    MIXED = "mixed"
    UNKNOWN = "unknown"


class NumericalMode(Enum):
    """Numerical computation mode."""
    HIGH_PRECISION = "high_precision"
    STABILITY_CRITICAL = "stability_critical"
    ANALYTICAL = "analytical"
    NORMAL = "normal"


class SafetyMode(Enum):
    """Safety/risk mode."""
    CONSERVATIVE = "conservative"
    EXPLORATORY = "exploratory"
    NORMAL = "normal"


@dataclass
class ExecutionContext:
    """
    Execution context for variant selection.

    Attributes:
        geometry_type: Flat vs curved geometry
        abstraction_level: Base vs ψ-transformed operators
        numerical_mode: Precision/stability requirements
        safety_mode: Conservative vs exploratory
        custom_flags: Additional context-specific flags
    """
    geometry_type: GeometryType = GeometryType.UNKNOWN
    abstraction_level: AbstractionLevel = AbstractionLevel.UNKNOWN
    numerical_mode: NumericalMode = NumericalMode.NORMAL
    safety_mode: SafetyMode = SafetyMode.NORMAL
    custom_flags: Dict[str, Any] = None

    def __post_init__(self):
        if self.custom_flags is None:
            self.custom_flags = {}


@dataclass
class VariantSelection:
    """
    Result of variant selection.

    Attributes:
        variant_id: Selected variant identifier
        formulation: The actual formulation to use
        reason: Why this variant was selected
        performance: Expected performance characteristics
        fallback_chain: Ordered list of fallback variants
    """
    variant_id: str
    formulation: Dict[str, Any]
    reason: str
    performance: Dict[str, str]
    fallback_chain: List[str]


# ============================================================================
# VARIANT-AWARE ROUTER
# ============================================================================

class VariantAwareRouter:
    """
    Router that selects between canonical and alternative operator formulations
    based on execution context.

    Resolves logical conflicts (Audit Findings #1, #3) by pooling variants
    and selecting context-appropriate formulations.
    """

    def __init__(self, operators_dir: str = None):
        """
        Initialize VariantAwareRouter.

        Args:
            operators_dir: Path to operators directory containing
                          canonical/, variants/, selection/ subdirectories
        """
        if operators_dir is None:
            operators_dir = Path(__file__).parent

        self.operators_dir = Path(operators_dir)
        self.canonical_dir = self.operators_dir / "canonical"
        self.variants_dir = self.operators_dir / "variants"
        self.selection_dir = self.operators_dir / "selection"

        # Load configurations
        self.canonical_defs = self._load_canonical_definitions()
        self.selection_guide = self._load_selection_guide()

        # Performance tracking
        self.selection_history = []

        logger.info(f"VariantAwareRouter initialized with {len(self.canonical_defs)} operator definitions")

    def _load_canonical_definitions(self) -> Dict[str, Dict[str, Any]]:
        """Load all canonical operator definitions."""
        definitions = {}

        if not self.canonical_dir.exists():
            logger.warning(f"Canonical directory not found: {self.canonical_dir}")
            return definitions

        for json_file in self.canonical_dir.glob("*.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    # Skip comment lines for JSON5 compatibility
                    content = '\n'.join(line for line in f if not line.strip().startswith('//'))
                    definition = json.loads(content)

                    # Extract operator identifier
                    if "operator_pair" in definition:
                        key = "_".join(definition["operator_pair"])
                    elif "operator_family" in definition:
                        key = definition["operator_family"]
                    else:
                        key = json_file.stem

                    definitions[key] = definition
                    logger.debug(f"Loaded canonical definition: {key}")

            except Exception as e:
                logger.error(f"Failed to load {json_file}: {e}")

        return definitions

    def _load_selection_guide(self) -> Dict[str, Any]:
        """Load context selection guide."""
        guide_file = self.selection_dir / "context_selection_guide.json"

        if not guide_file.exists():
            logger.warning(f"Selection guide not found: {guide_file}")
            return {}

        try:
            with open(guide_file, 'r', encoding='utf-8') as f:
                # Skip comment lines
                content = '\n'.join(line for line in f if not line.strip().startswith('//'))
                guide = json.loads(content)
                logger.info("Loaded context selection guide")
                return guide
        except Exception as e:
            logger.error(f"Failed to load selection guide: {e}")
            return {}

    # ========================================================================
    # CONTEXT DETECTION
    # ========================================================================

    def detect_context(self, state: Dict[str, Any]) -> ExecutionContext:
        """
        Detect execution context from state.

        Args:
            state: Current execution state with context indicators

        Returns:
            Detected ExecutionContext
        """
        context = ExecutionContext()

        # Detect geometry type
        context.geometry_type = self._detect_geometry_type(state)

        # Detect abstraction level
        context.abstraction_level = self._detect_abstraction_level(state)

        # Detect numerical mode
        context.numerical_mode = self._detect_numerical_mode(state)

        # Detect safety mode
        context.safety_mode = self._detect_safety_mode(state)

        # Copy custom flags
        context.custom_flags = state.get('custom_flags', {})

        logger.debug(f"Detected context: {context}")
        return context

    def _detect_geometry_type(self, state: Dict[str, Any]) -> GeometryType:
        """Detect if geometry is flat or curved."""
        # Check explicit flag
        if state.get('flat_geometry_flag'):
            return GeometryType.FLAT
        if state.get('curved_geometry_flag'):
            return GeometryType.CURVED

        # Check curvature operator
        if 'λ' in state:
            lambda_val = state['λ']
            if lambda_val == 0 or (hasattr(lambda_val, '__abs__') and abs(lambda_val) < 1e-10):
                return GeometryType.FLAT
            else:
                return GeometryType.CURVED
        elif 'lambda' in state:
            lambda_val = state['lambda']
            if lambda_val == 0 or (hasattr(lambda_val, '__abs__') and abs(lambda_val) < 1e-10):
                return GeometryType.FLAT
            else:
                return GeometryType.CURVED

        # Check curvature tensor norm
        if 'curvature_tensor_norm' in state:
            if state['curvature_tensor_norm'] < 1e-8:
                return GeometryType.FLAT
            else:
                return GeometryType.CURVED

        return GeometryType.UNKNOWN

    def _detect_abstraction_level(self, state: Dict[str, Any]) -> AbstractionLevel:
        """Detect operator abstraction level (base vs ψ-transformed)."""
        # Check explicit flags
        if state.get('psi_transformation_applied'):
            if state.get('all_operators_psi_transformed'):
                return AbstractionLevel.PSI_LAYER
            else:
                return AbstractionLevel.MIXED

        # Check for ψ-related indicators
        if state.get('modal_decomposition_active') or state.get('wave_space_analysis'):
            return AbstractionLevel.PSI_LAYER

        if state.get('working_with_raw_operators') or state.get('direct_composition'):
            return AbstractionLevel.BASE_OPERATOR

        if state.get('some_operators_psi_transformed'):
            return AbstractionLevel.MIXED

        return AbstractionLevel.UNKNOWN

    def _detect_numerical_mode(self, state: Dict[str, Any]) -> NumericalMode:
        """Detect numerical computation mode."""
        if state.get('convergence_issues') or state.get('numerical_instability_detected'):
            return NumericalMode.STABILITY_CRITICAL

        if state.get('analytical_calculation') or state.get('symbolic_computation'):
            return NumericalMode.ANALYTICAL

        if state.get('numerical_precision') == 'high':
            return NumericalMode.HIGH_PRECISION

        return NumericalMode.NORMAL

    def _detect_safety_mode(self, state: Dict[str, Any]) -> SafetyMode:
        """Detect safety/risk mode."""
        if state.get('safety_critical') or state.get('production_deployment'):
            return SafetyMode.CONSERVATIVE

        if state.get('research_mode') or state.get('experimental_feature'):
            return SafetyMode.EXPLORATORY

        return SafetyMode.NORMAL

    # ========================================================================
    # VARIANT SELECTION
    # ========================================================================

    def select_variant(self,
                      operator_pair: Tuple[str, str],
                      context: ExecutionContext) -> VariantSelection:
        """
        Select optimal variant for operator pair given context.

        Args:
            operator_pair: Tuple of operator names (e.g., ("λ", "δ"))
            context: Execution context

        Returns:
            VariantSelection with selected formulation
        """
        # Get operator key
        operator_key = "_".join(operator_pair)

        # Get canonical definition
        if operator_key not in self.canonical_defs:
            logger.warning(f"No canonical definition for {operator_key}, using fallback")
            return self._fallback_selection(operator_key, context)

        definition = self.canonical_defs[operator_key]

        # Apply selection logic
        selected = self._apply_selection_logic(definition, context)

        # Record selection
        self.selection_history.append({
            'operator': operator_key,
            'context': context,
            'selected': selected.variant_id,
            'reason': selected.reason
        })

        logger.info(f"Selected variant '{selected.variant_id}' for {operator_key}: {selected.reason}")

        return selected

    def _apply_selection_logic(self,
                               definition: Dict[str, Any],
                               context: ExecutionContext) -> VariantSelection:
        """Apply selection logic from definition."""
        # Check each variant's use_when conditions
        variants = definition.get('variants', [])

        # Try each variant in priority order
        for variant in variants:
            if self._check_variant_conditions(variant, context):
                return VariantSelection(
                    variant_id=variant['variant_id'],
                    formulation=variant,
                    reason=variant.get('physical_meaning', 'Context match'),
                    performance=self._get_performance(definition, variant['variant_id']),
                    fallback_chain=self._build_fallback_chain(definition, variant['variant_id'])
                )

        # Default to canonical
        canonical = definition['canonical_definition']
        return VariantSelection(
            variant_id='canonical_definition',
            formulation=canonical,
            reason=canonical.get('physical_meaning', 'Default canonical'),
            performance=self._get_performance(definition, 'canonical_definition'),
            fallback_chain=self._build_fallback_chain(definition, 'canonical_definition')
        )

    def _check_variant_conditions(self,
                                  variant: Dict[str, Any],
                                  context: ExecutionContext) -> bool:
        """Check if variant's use_when conditions match context."""
        use_when = variant.get('use_when', [])

        for condition in use_when:
            condition_lower = condition.lower()

            # Check geometry conditions
            if 'flat' in condition_lower and context.geometry_type == GeometryType.FLAT:
                return True
            if 'curved' in condition_lower and context.geometry_type == GeometryType.CURVED:
                return True

            # Check abstraction level
            if 'psi' in condition_lower and 'layer' in condition_lower:
                if context.abstraction_level == AbstractionLevel.PSI_LAYER:
                    return True
            if 'base' in condition_lower or 'raw' in condition_lower:
                if context.abstraction_level == AbstractionLevel.BASE_OPERATOR:
                    return True
            if 'mixed' in condition_lower or 'transitional' in condition_lower:
                if context.abstraction_level == AbstractionLevel.MIXED:
                    return True

            # Check numerical mode
            if 'numerical' in condition_lower and 'stability' in condition_lower:
                if context.numerical_mode == NumericalMode.STABILITY_CRITICAL:
                    return True
            if 'analytical' in condition_lower:
                if context.numerical_mode == NumericalMode.ANALYTICAL:
                    return True

            # Check safety mode
            if 'conservative' in condition_lower or 'safety' in condition_lower:
                if context.safety_mode == SafetyMode.CONSERVATIVE:
                    return True

        return False

    def _get_performance(self, definition: Dict[str, Any], variant_id: str) -> Dict[str, str]:
        """Get performance characteristics for variant."""
        # Try to find in selection guide
        if 'selection_guide' in definition:
            perf = definition['selection_guide'].get('performance_notes', {})
            if variant_id in perf:
                return {'note': perf[variant_id]}

        # Default performance info
        if variant_id == 'canonical_definition':
            return {'cost': 'HIGH', 'accuracy': 'EXACT'}
        elif 'flat' in variant_id:
            return {'cost': 'LOW', 'accuracy': 'EXACT (when applicable)'}
        elif 'symmetric' in variant_id:
            return {'cost': 'MEDIUM', 'accuracy': 'APPROXIMATE'}
        else:
            return {'cost': 'MEDIUM', 'accuracy': 'VARIES'}

    def _build_fallback_chain(self,
                             definition: Dict[str, Any],
                             current_variant: str) -> List[str]:
        """Build fallback chain for current variant."""
        # Check if definition specifies fallback chain
        if 'selection_guide' in definition:
            fallback = definition['selection_guide'].get('fallback_chain', [])
            if fallback:
                # Move current variant to front
                chain = [v for v in fallback if v != current_variant]
                return [current_variant] + chain

        # Default fallback: current → canonical
        if current_variant == 'canonical_definition':
            return [current_variant]
        else:
            return [current_variant, 'canonical_definition']

    def _fallback_selection(self,
                           operator_key: str,
                           context: ExecutionContext) -> VariantSelection:
        """Fallback selection when no definition found."""
        logger.warning(f"Using fallback for {operator_key}")
        return VariantSelection(
            variant_id='fallback',
            formulation={'note': 'No definition found'},
            reason='Fallback - no canonical definition available',
            performance={'cost': 'UNKNOWN', 'accuracy': 'UNKNOWN'},
            fallback_chain=['fallback']
        )

    # ========================================================================
    # COMPOSITION WITH FALLBACK
    # ========================================================================

    def compose_with_fallback(self,
                             operator_a: str,
                             operator_b: str,
                             state: Dict[str, Any],
                             context: ExecutionContext = None) -> Dict[str, Any]:
        """
        Compose operators with automatic fallback if canonical fails.

        Args:
            operator_a: First operator
            operator_b: Second operator
            state: Current state
            context: Execution context (auto-detected if None)

        Returns:
            Composition result with variant info
        """
        # Detect context if not provided
        if context is None:
            context = self.detect_context(state)

        # Select variant
        selection = self.select_variant((operator_a, operator_b), context)

        # Attempt composition with selected variant
        try:
            result = self._apply_composition(
                operator_a,
                operator_b,
                state,
                selection.formulation
            )

            # Validate result
            if self._validate_result(result):
                return {
                    'result': result,
                    'variant_used': selection.variant_id,
                    'success': True,
                    'fallback_attempted': False
                }

        except Exception as e:
            logger.warning(f"Composition failed with {selection.variant_id}: {e}")

        # Try fallback chain
        for fallback_variant_id in selection.fallback_chain[1:]:  # Skip first (already tried)
            try:
                logger.info(f"Trying fallback: {fallback_variant_id}")

                # Find fallback formulation
                fallback_formulation = self._get_variant_formulation(
                    (operator_a, operator_b),
                    fallback_variant_id
                )

                result = self._apply_composition(
                    operator_a,
                    operator_b,
                    state,
                    fallback_formulation
                )

                if self._validate_result(result):
                    logger.info(f"Fallback {fallback_variant_id} succeeded")
                    return {
                        'result': result,
                        'variant_used': fallback_variant_id,
                        'success': True,
                        'fallback_attempted': True,
                        'original_variant': selection.variant_id
                    }

            except Exception as e:
                logger.warning(f"Fallback {fallback_variant_id} failed: {e}")
                continue

        # All variants failed
        raise RuntimeError(f"All formulations failed for {operator_a}∘{operator_b}")

    def _get_variant_formulation(self,
                                operator_pair: Tuple[str, str],
                                variant_id: str) -> Dict[str, Any]:
        """Get specific variant formulation."""
        operator_key = "_".join(operator_pair)
        definition = self.canonical_defs.get(operator_key, {})

        if variant_id == 'canonical_definition':
            return definition.get('canonical_definition', {})

        # Search variants
        for variant in definition.get('variants', []):
            if variant['variant_id'] == variant_id:
                return variant

        return {}

    def _apply_composition(self,
                          operator_a: str,
                          operator_b: str,
                          state: Dict[str, Any],
                          formulation: Dict[str, Any]) -> Any:
        """Apply operator composition using specified formulation."""
        # This is a placeholder - actual implementation would apply the
        # mathematical formulation from the variant definition

        logger.debug(f"Applying {operator_a}∘{operator_b} with formulation: {formulation.get('variant_id', 'canonical')}")

        # For demonstration: return composition info
        return {
            'composition': f"{operator_a}∘{operator_b}",
            'formulation': formulation.get('variant_id', 'canonical'),
            'state': state
        }

    def _validate_result(self, result: Any) -> bool:
        """Validate composition result."""
        # Placeholder validation
        return result is not None

    # ========================================================================
    # DIAGNOSTICS & REPORTING
    # ========================================================================

    def get_selection_stats(self) -> Dict[str, Any]:
        """Get statistics on variant selections."""
        if not self.selection_history:
            return {'total_selections': 0}

        stats = {
            'total_selections': len(self.selection_history),
            'by_variant': {},
            'by_operator': {},
            'by_context_geometry': {},
            'by_context_level': {}
        }

        for entry in self.selection_history:
            variant = entry['selected']
            operator = entry['operator']
            context = entry['context']

            # Count by variant
            stats['by_variant'][variant] = stats['by_variant'].get(variant, 0) + 1

            # Count by operator
            stats['by_operator'][operator] = stats['by_operator'].get(operator, 0) + 1

            # Count by geometry type
            geom = context.geometry_type.value
            stats['by_context_geometry'][geom] = stats['by_context_geometry'].get(geom, 0) + 1

            # Count by abstraction level
            level = context.abstraction_level.value
            stats['by_context_level'][level] = stats['by_context_level'].get(level, 0) + 1

        return stats

    def explain_selection(self,
                         operator_pair: Tuple[str, str],
                         context: ExecutionContext) -> str:
        """Generate human-readable explanation of variant selection."""
        selection = self.select_variant(operator_pair, context)

        explanation = f"""
Variant Selection Explanation
============================

Operator Pair: {operator_pair[0]} ∘ {operator_pair[1]}

Context:
  - Geometry: {context.geometry_type.value}
  - Abstraction Level: {context.abstraction_level.value}
  - Numerical Mode: {context.numerical_mode.value}
  - Safety Mode: {context.safety_mode.value}

Selected Variant: {selection.variant_id}

Reason: {selection.reason}

Performance:
  {selection.performance}

Fallback Chain: {' → '.join(selection.fallback_chain)}
"""
        return explanation


# ============================================================================
# EXAMPLE USAGE
# ============================================================================

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Initialize router
    router = VariantAwareRouter()

    # Example 1: Flat geometry
    print("\n" + "="*70)
    print("Example 1: Flat Geometry")
    print("="*70)

    state_flat = {
        'λ': 0,
        'flat_geometry_flag': True,
        'numerical_precision': 'high'
    }

    context_flat = router.detect_context(state_flat)
    selection_flat = router.select_variant(("λ", "δ"), context_flat)

    print(router.explain_selection(("λ", "δ"), context_flat))

    # Example 2: ψ-layer with all operators transformed
    print("\n" + "="*70)
    print("Example 2: ψ-Layer Analysis")
    print("="*70)

    state_psi = {
        'psi_transformation_applied': True,
        'all_operators_psi_transformed': True,
        'modal_decomposition_active': True
    }

    context_psi = router.detect_context(state_psi)

    # For ψ-commutativity
    if 'ψ-Family' in router.canonical_defs:
        selection_psi = router.select_variant(("ψ", "commutativity"), context_psi)
        print(f"Selected: {selection_psi.variant_id}")
        print(f"Reason: {selection_psi.reason}")

    # Example 3: Numerical stability needed
    print("\n" + "="*70)
    print("Example 3: Numerical Stability")
    print("="*70)

    state_numerical = {
        'λ': 0.5,
        'convergence_issues': True,
        'numerical_instability_detected': True
    }

    context_numerical = router.detect_context(state_numerical)
    selection_numerical = router.select_variant(("λ", "δ"), context_numerical)

    print(router.explain_selection(("λ", "δ"), context_numerical))

    # Show statistics
    print("\n" + "="*70)
    print("Selection Statistics")
    print("="*70)
    print(json.dumps(router.get_selection_stats(), indent=2))
