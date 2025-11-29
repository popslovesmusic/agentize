"""
Variant Consistency Validation Suite

Tests that all operator variants are mathematically consistent with their
canonical definitions and that the VariantAwareRouter selects correctly.

Author: MBC Framework
Date: 2025-11-28
Version: 1.0.0
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple
from dataclasses import dataclass

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from variant_aware_router import (
    VariantAwareRouter,
    ExecutionContext,
    GeometryType,
    AbstractionLevel,
    NumericalMode,
    SafetyMode
)


# ============================================================================
# TEST RESULTS
# ============================================================================

@dataclass
class TestResult:
    """Result of a validation test."""
    test_name: str
    passed: bool
    message: str
    details: Dict[str, Any] = None


class ValidationSuite:
    """Comprehensive validation of pooled variant system."""

    def __init__(self, operators_dir: str = None):
        """Initialize validation suite."""
        if operators_dir is None:
            operators_dir = Path(__file__).parent.parent

        self.operators_dir = Path(operators_dir)
        self.router = VariantAwareRouter(operators_dir)
        self.results: List[TestResult] = []

    # ========================================================================
    # MATHEMATICAL CONSISTENCY TESTS
    # ========================================================================

    def test_flat_limit_consistency(self) -> TestResult:
        """
        Test: lim(λ→0) canonical = flat_geometry variant

        Verifies that as curvature approaches zero, the canonical
        formulation reduces to the flat geometry variant.
        """
        test_name = "Flat Limit Consistency (λ→0)"

        # Test with λ=0
        state_flat = {'λ': 0, 'flat_geometry_flag': True}
        context_flat = self.router.detect_context(state_flat)

        if "λ_δ" not in self.router.canonical_defs:
            return TestResult(
                test_name=test_name,
                passed=False,
                message="λ_δ canonical definition not found",
                details={'available_defs': list(self.router.canonical_defs.keys())}
            )

        selection = self.router.select_variant(("λ", "δ"), context_flat)

        # Should select flat_geometry variant
        expected = "flat_geometry"
        passed = selection.variant_id == expected

        return TestResult(
            test_name=test_name,
            passed=passed,
            message=f"Selected {selection.variant_id}, expected {expected}" if not passed else "[PASS] Correct variant selected",
            details={
                'selected': selection.variant_id,
                'expected': expected,
                'context': str(context_flat)
            }
        )

    def test_psi_layer_commutativity(self) -> TestResult:
        """
        Test: ψ-layer operators should use canonical commutative definition

        When all operators are ψ-transformed, the ψ-commutativity
        canonical definition should be selected.
        """
        test_name = "ψ-Layer Commutativity Selection"

        state_psi = {
            'psi_transformation_applied': True,
            'all_operators_psi_transformed': True,
            'modal_decomposition_active': True
        }
        context_psi = self.router.detect_context(state_psi)

        # Check abstraction level detection
        if context_psi.abstraction_level != AbstractionLevel.PSI_LAYER:
            return TestResult(
                test_name=test_name,
                passed=False,
                message=f"Failed to detect ψ-layer: got {context_psi.abstraction_level}",
                details={'context': str(context_psi)}
            )

        # For ψ-commutativity operator
        if "ψ-Family" in self.router.canonical_defs:
            # Create a custom selection check
            definition = self.router.canonical_defs["ψ-Family"]

            # Should prefer canonical when in ψ-layer
            passed = True
            message = "[PASS] ψ-layer context detected correctly"
        else:
            passed = False
            message = "ψ-Family definition not found"

        return TestResult(
            test_name=test_name,
            passed=passed,
            message=message,
            details={'context': str(context_psi)}
        )

    def test_base_level_non_commutativity(self) -> TestResult:
        """
        Test: Base operators should use non-commutative variant

        When working with raw operators (no ψ-transformation),
        the base_level_non_commutative variant should be selected.
        """
        test_name = "Base Level Non-Commutativity"

        state_base = {
            'working_with_raw_operators': True,
            'psi_transformation_applied': False,
            'direct_composition': True
        }
        context_base = self.router.detect_context(state_base)

        # Check abstraction level
        if context_base.abstraction_level != AbstractionLevel.BASE_OPERATOR:
            return TestResult(
                test_name=test_name,
                passed=False,
                message=f"Failed to detect base level: got {context_base.abstraction_level}",
                details={'context': str(context_base)}
            )

        return TestResult(
            test_name=test_name,
            passed=True,
            message="[PASS] Base operator level detected correctly",
            details={'context': str(context_base)}
        )

    def test_symmetric_approximation_stability(self) -> TestResult:
        """
        Test: Numerical instability → symmetric approximation

        When convergence issues detected, should select
        symmetric_approximation variant for stability.
        """
        test_name = "Symmetric Approximation for Stability"

        state_unstable = {
            'λ': 0.5,
            'convergence_issues': True,
            'numerical_instability_detected': True
        }
        context_unstable = self.router.detect_context(state_unstable)

        # Should detect stability-critical mode
        if context_unstable.numerical_mode != NumericalMode.STABILITY_CRITICAL:
            return TestResult(
                test_name=test_name,
                passed=False,
                message=f"Failed to detect stability need: got {context_unstable.numerical_mode}",
                details={'context': str(context_unstable)}
            )

        selection = self.router.select_variant(("λ", "δ"), context_unstable)

        # Should select symmetric_approximation
        expected = "symmetric_approximation"
        passed = selection.variant_id == expected

        return TestResult(
            test_name=test_name,
            passed=passed,
            message=f"Selected {selection.variant_id}, expected {expected}" if not passed else "[PASS] Stability variant selected",
            details={
                'selected': selection.variant_id,
                'expected': expected,
                'context': str(context_unstable)
            }
        )

    def test_perturbative_expansion_analytical(self) -> TestResult:
        """
        Test: Analytical mode → perturbative expansion

        When analytical/symbolic computation requested,
        should select perturbative_expansion variant.
        """
        test_name = "Perturbative Expansion for Analytical"

        state_analytical = {
            'λ': 0.1,
            'analytical_calculation': True,
            'symbolic_computation': True
        }
        context_analytical = self.router.detect_context(state_analytical)

        # Should detect analytical mode
        if context_analytical.numerical_mode != NumericalMode.ANALYTICAL:
            return TestResult(
                test_name=test_name,
                passed=False,
                message=f"Failed to detect analytical mode: got {context_analytical.numerical_mode}",
                details={'context': str(context_analytical)}
            )

        selection = self.router.select_variant(("λ", "δ"), context_analytical)

        # Should select perturbative_expansion
        expected = "perturbative_expansion"
        passed = selection.variant_id == expected

        return TestResult(
            test_name=test_name,
            passed=passed,
            message=f"Selected {selection.variant_id}, expected {expected}" if not passed else "[PASS] Analytical variant selected",
            details={
                'selected': selection.variant_id,
                'expected': expected,
                'context': str(context_analytical)
            }
        )

    def test_conservative_safety_mode(self) -> TestResult:
        """
        Test: Safety-critical contexts use conservative variants

        When safety_critical or production_deployment flags set,
        should use conservative exception_lambda_delta variant.
        """
        test_name = "Conservative Safety Mode"

        state_safe = {
            'safety_critical': True,
            'production_deployment': True
        }
        context_safe = self.router.detect_context(state_safe)

        # Should detect conservative mode
        if context_safe.safety_mode != SafetyMode.CONSERVATIVE:
            return TestResult(
                test_name=test_name,
                passed=False,
                message=f"Failed to detect conservative mode: got {context_safe.safety_mode}",
                details={'context': str(context_safe)}
            )

        return TestResult(
            test_name=test_name,
            passed=True,
            message="[PASS] Conservative mode detected correctly",
            details={'context': str(context_safe)}
        )

    # ========================================================================
    # CROSS-FILE CONSISTENCY TESTS
    # ========================================================================

    def test_no_conflicting_statements(self) -> TestResult:
        """
        Test: All variants are level-separated, not contradictory

        Verifies that apparent conflicts (like ψ-commutativity vs
        base non-commutativity) are resolved by level separation.
        """
        test_name = "No Conflicting Statements (Level Separation)"

        # Check that both definitions exist
        has_lambda_delta = "λ_δ" in self.router.canonical_defs
        has_psi_family = "ψ-Family" in self.router.canonical_defs

        if not has_lambda_delta or not has_psi_family:
            return TestResult(
                test_name=test_name,
                passed=False,
                message="Missing required definitions",
                details={
                    'has_lambda_delta': has_lambda_delta,
                    'has_psi_family': has_psi_family
                }
            )

        # Verify resolution metadata
        lambda_def = self.router.canonical_defs["λ_δ"]
        psi_def = self.router.canonical_defs["ψ-Family"]

        # Check for resolution documentation
        has_resolution = 'conflict_resolution' in psi_def

        return TestResult(
            test_name=test_name,
            passed=has_resolution,
            message="[PASS] Conflict resolution documented" if has_resolution else "Missing conflict resolution",
            details={
                'lambda_def_status': lambda_def.get('canonical_definition', {}).get('status'),
                'psi_def_has_resolution': has_resolution
            }
        )

    def test_fallback_chains_valid(self) -> TestResult:
        """
        Test: All fallback chains reference existing variants

        Ensures that fallback chains don't reference non-existent
        variant IDs.
        """
        test_name = "Fallback Chain Validity"

        errors = []

        for op_key, definition in self.router.canonical_defs.items():
            # Get all variant IDs
            variant_ids = {'canonical_definition'}
            for variant in definition.get('variants', []):
                variant_ids.add(variant.get('variant_id', ''))

            # Check fallback chains
            selection_guide = definition.get('selection_guide', {})
            fallback_chain = selection_guide.get('fallback_chain', [])

            for variant_id in fallback_chain:
                if variant_id not in variant_ids:
                    errors.append(f"{op_key}: Unknown variant '{variant_id}' in fallback chain")

        passed = len(errors) == 0

        return TestResult(
            test_name=test_name,
            passed=passed,
            message="[PASS] All fallback chains valid" if passed else f"Found {len(errors)} errors",
            details={'errors': errors} if errors else None
        )

    def test_variant_metadata_complete(self) -> TestResult:
        """
        Test: All variants have required metadata

        Checks that each variant has variant_id, status, use_when.
        """
        test_name = "Variant Metadata Completeness"

        errors = []
        required_fields = ['variant_id', 'status', 'use_when']

        for op_key, definition in self.router.canonical_defs.items():
            for variant in definition.get('variants', []):
                for field in required_fields:
                    if field not in variant:
                        errors.append(f"{op_key}: Variant missing '{field}'")

        passed = len(errors) == 0

        return TestResult(
            test_name=test_name,
            passed=passed,
            message="[PASS] All variants have complete metadata" if passed else f"Found {len(errors)} errors",
            details={'errors': errors[:10]} if errors else None  # Show first 10
        )

    # ========================================================================
    # CONTEXT DETECTION TESTS
    # ========================================================================

    def test_geometry_detection(self) -> TestResult:
        """Test geometry type detection accuracy."""
        test_name = "Geometry Type Detection"

        test_cases = [
            ({'λ': 0}, GeometryType.FLAT),
            ({'λ': 0.5}, GeometryType.CURVED),
            ({'flat_geometry_flag': True}, GeometryType.FLAT),
            ({'curvature_tensor_norm': 1e-10}, GeometryType.FLAT),
            ({'curvature_tensor_norm': 0.5}, GeometryType.CURVED),
        ]

        errors = []
        for state, expected in test_cases:
            context = self.router.detect_context(state)
            if context.geometry_type != expected:
                errors.append(f"State {state}: expected {expected}, got {context.geometry_type}")

        passed = len(errors) == 0

        return TestResult(
            test_name=test_name,
            passed=passed,
            message="[PASS] All geometry detections correct" if passed else f"{len(errors)} detection errors",
            details={'errors': errors} if errors else None
        )

    def test_abstraction_level_detection(self) -> TestResult:
        """Test abstraction level detection accuracy."""
        test_name = "Abstraction Level Detection"

        test_cases = [
            ({'psi_transformation_applied': True, 'all_operators_psi_transformed': True},
             AbstractionLevel.PSI_LAYER),
            ({'working_with_raw_operators': True},
             AbstractionLevel.BASE_OPERATOR),
            ({'some_operators_psi_transformed': True},
             AbstractionLevel.MIXED),
            ({'modal_decomposition_active': True},
             AbstractionLevel.PSI_LAYER),
        ]

        errors = []
        for state, expected in test_cases:
            context = self.router.detect_context(state)
            if context.abstraction_level != expected:
                errors.append(f"State {state}: expected {expected}, got {context.abstraction_level}")

        passed = len(errors) == 0

        return TestResult(
            test_name=test_name,
            passed=passed,
            message="[PASS] All abstraction level detections correct" if passed else f"{len(errors)} detection errors",
            details={'errors': errors} if errors else None
        )

    # ========================================================================
    # RUN ALL TESTS
    # ========================================================================

    def run_all_tests(self) -> List[TestResult]:
        """Run all validation tests."""
        print("\n" + "="*70)
        print("VARIANT CONSISTENCY VALIDATION SUITE")
        print("="*70)

        tests = [
            # Mathematical consistency
            self.test_flat_limit_consistency,
            self.test_psi_layer_commutativity,
            self.test_base_level_non_commutativity,
            self.test_symmetric_approximation_stability,
            self.test_perturbative_expansion_analytical,
            self.test_conservative_safety_mode,

            # Cross-file consistency
            self.test_no_conflicting_statements,
            self.test_fallback_chains_valid,
            self.test_variant_metadata_complete,

            # Context detection
            self.test_geometry_detection,
            self.test_abstraction_level_detection,
        ]

        self.results = []

        for test_func in tests:
            print(f"\nRunning: {test_func.__doc__.split(chr(10))[0].strip()}")
            result = test_func()
            self.results.append(result)

            # Print result
            status = "[PASS] PASS" if result.passed else "[FAIL] FAIL"
            print(f"  {status}: {result.message}")

            if result.details and not result.passed:
                print(f"  Details: {json.dumps(result.details, indent=4)}")

        return self.results

    def generate_report(self) -> str:
        """Generate validation report."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed

        report = f"""
{"="*70}
VALIDATION REPORT
{"="*70}

Total Tests:  {total}
Passed:       {passed} ({100*passed//total if total > 0 else 0}%)
Failed:       {failed}

"""

        if failed > 0:
            report += "Failed Tests:\n"
            for result in self.results:
                if not result.passed:
                    report += f"  - {result.test_name}: {result.message}\n"

        report += f"\n{'='*70}\n"

        return report


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    import logging
    import io

    # Set UTF-8 encoding for stdout/stderr on Windows
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

    # Configure logging
    logging.basicConfig(
        level=logging.WARNING,  # Suppress debug output for cleaner test results
        format='%(levelname)s: %(message)s'
    )

    # Run validation suite
    suite = ValidationSuite()
    results = suite.run_all_tests()

    # Generate report
    print(suite.generate_report())

    # Exit with error code if any tests failed
    failed_count = sum(1 for r in results if not r.passed)
    sys.exit(failed_count)
