# -*- coding: utf-8 -*-
import json
from client import GenParkWukongDataSynthesizer

synth = GenParkWukongDataSynthesizer()

# 1. Laplace Differential Privacy Noise
dp = synth.generate_laplace_differential_privacy_noise(value=75000.0, epsilon=0.5, sensitivity=1000.0)
print(f"Differential Privacy: Orig=${dp['original_value']} -> Privatized=${dp['privatized_value']} (Noise: {dp['noise_added']}, Scale: {dp['laplace_scale_b']})")

# 2. Wasserstein Earth Mover's Distance
real_data = [12.0, 15.0, 18.0, 22.0, 25.0, 28.0, 35.0, 42.0]
synth_data = [13.0, 14.5, 19.0, 21.5, 26.0, 29.0, 33.5, 40.0]
w1 = synth.calculate_wasserstein_marginal_distance(real_data, synth_data)
print()
print(f"Wasserstein W1 Distance: {w1['wasserstein_distance_w1']} | Fidelity Score: {w1['distribution_fidelity_score']}/100 ({w1['fidelity_grade']})")

# 3. Correlation Matrix Preservation
real_corr = [
    [1.0, 0.75, 0.20],
    [0.75, 1.0, 0.15],
    [0.20, 0.15, 1.0]
]
synth_corr = [
    [1.0, 0.72, 0.23],
    [0.72, 1.0, 0.12],
    [0.23, 0.12, 1.0]
]
corr_eval = synth.evaluate_correlation_matrix_preservation(real_corr, synth_corr)
print()
print(f"Correlation Matrix Preservation: Score={corr_eval['correlation_preservation_score']}/100 | MAE={corr_eval['mean_absolute_correlation_error']} | Frobenius Norm={corr_eval['frobenius_norm_error']}")
