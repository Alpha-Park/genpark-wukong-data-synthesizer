# -*- coding: utf-8 -*-
"""
GenPark Wukong Data Synthesizer Client
Zero-dependency differential privacy Laplace mechanism noise generator,
Wasserstein marginal distance fidelity evaluator, and correlation matrix preservation auditor.
"""

import math
import random
from typing import Dict, List, Any, Optional

class GenParkWukongDataSynthesizer:
    """
    Synthesizes privacy-preserving tabular datasets using Laplace mechanisms,
    measures 1D Wasserstein Earth Mover's Distance, and checks correlation preservation.
    """

    def generate_laplace_differential_privacy_noise(
        self,
        value: float,
        epsilon: float = 1.0,
        sensitivity: float = 1.0
    ) -> Dict[str, Any]:
        """
        Adds differentially private Laplace noise: Lap(b) where scale b = sensitivity / epsilon.
        """
        if epsilon <= 0 or sensitivity <= 0:
            raise ValueError("Epsilon and sensitivity must be strictly positive.")

        b = sensitivity / epsilon
        
        # Inverse transform sampling for Laplace distribution:
        # u ~ Uniform(-0.5, 0.5)
        # x = -b * sign(u) * ln(1 - 2|u|)
        u = random.random() - 0.5
        sgn = 1.0 if u >= 0 else -1.0
        abs_u = abs(u)
        noise = -b * sgn * math.log(max(1e-12, 1.0 - 2.0 * abs_u))

        privatized_value = round(value + noise, 4)
        variance = 2.0 * (b ** 2)
        ci_95 = round(1.96 * math.sqrt(variance), 4)

        return {
            "original_value": value,
            "privatized_value": privatized_value,
            "noise_added": round(noise, 4),
            "epsilon_privacy_budget": epsilon,
            "sensitivity": sensitivity,
            "laplace_scale_b": round(b, 4),
            "theoretical_noise_variance": round(variance, 4),
            "noise_confidence_interval_95_pct": [round(privatized_value - ci_95, 4), round(privatized_value + ci_95, 4)]
        }

    def calculate_wasserstein_marginal_distance(
        self,
        real_samples: List[float],
        synth_samples: List[float]
    ) -> Dict[str, Any]:
        """
        Calculates 1D Wasserstein (Earth Mover's Distance) between real and synthetic sample distributions:
        W_1 = (1 / N) * sum(|u_(i) - v_(i)|) for sorted samples.
        """
        if not real_samples or not synth_samples:
            raise ValueError("Sample arrays cannot be empty.")

        u = sorted(real_samples)
        v = sorted(synth_samples)

        # Quantile interpolation to compare equal lengths
        n = max(len(u), len(v), 20)
        u_quantiles = [u[int(i * (len(u) - 1) / (n - 1))] for i in range(n)]
        v_quantiles = [v[int(i * (len(v) - 1) / (n - 1))] for i in range(n)]

        w1_dist = sum(abs(a - b) for a, b in zip(u_quantiles, v_quantiles)) / float(n)

        # Scale relative to real data IQR
        q25 = u[int(0.25 * (len(u) - 1))]
        q75 = u[int(0.75 * (len(u) - 1))]
        iqr = max(1e-6, q75 - q25)
        normalized_w1 = w1_dist / iqr

        fidelity_score = round(max(0.0, min(100.0, 100.0 * math.exp(-normalized_w1))), 1)

        return {
            "wasserstein_distance_w1": round(w1_dist, 4),
            "real_data_iqr": round(iqr, 4),
            "normalized_wasserstein": round(normalized_w1, 4),
            "distribution_fidelity_score": fidelity_score,
            "fidelity_grade": "EXCELLENT" if fidelity_score >= 80.0 else ("GOOD" if fidelity_score >= 60.0 else "POOR_FIT")
        }

    def evaluate_correlation_matrix_preservation(
        self,
        real_corr_matrix: List[List[float]],
        synth_corr_matrix: List[List[float]]
    ) -> Dict[str, Any]:
        """
        Computes Frobenius norm difference and Mean Absolute Error (MAE) between real and synthetic correlation matrices.
        """
        dim = len(real_corr_matrix)
        if dim == 0 or len(synth_corr_matrix) != dim:
            raise ValueError("Correlation matrices must be non-empty square matrices of equal dimension.")

        sum_sq_diff = 0.0
        sum_abs_diff = 0.0
        total_pairs = 0

        for i in range(dim):
            for j in range(dim):
                r = real_corr_matrix[i][j]
                s = synth_corr_matrix[i][j]
                diff = r - s
                sum_sq_diff += diff * diff
                if i != j:
                    sum_abs_diff += abs(diff)
                    total_pairs += 1

        frobenius_norm = math.sqrt(sum_sq_diff)
        mae = sum_abs_diff / max(1, total_pairs)
        preservation_score = round(max(0.0, min(100.0, 100.0 * (1.0 - mae))), 1)

        return {
            "matrix_dimension": dim,
            "frobenius_norm_error": round(frobenius_norm, 4),
            "mean_absolute_correlation_error": round(mae, 4),
            "correlation_preservation_score": preservation_score,
            "preservation_status": "HIGH_PRESERVATION" if preservation_score >= 85.0 else ("MODERATE" if preservation_score >= 70.0 else "STRUCTURAL_COLLAPSE")
        }
