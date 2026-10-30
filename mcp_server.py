# -*- coding: utf-8 -*-
"""
GenPark Wukong Data Synthesizer FastMCP Server
"""

import json
from typing import Dict, List, Any, Optional
from mcp.server.fastmcp import FastMCP
from client import GenParkWukongDataSynthesizer

mcp = FastMCP("genpark-wukong-data-synthesizer")
synth = GenParkWukongDataSynthesizer()

@mcp.tool()
def generate_laplace_differential_privacy_noise(
    value: float,
    epsilon: float = 1.0,
    sensitivity: float = 1.0
) -> str:
    """
    Adds differentially private Laplace noise to protect tabular attributes.
    """
    res = synth.generate_laplace_differential_privacy_noise(value, epsilon, sensitivity)
    return json.dumps(res, indent=2)

@mcp.tool()
def calculate_wasserstein_marginal_distance(
    real_samples_json: str,
    synth_samples_json: str
) -> str:
    """
    Calculates 1D Wasserstein Earth Mover's Distance between distributions.
    """
    real = json.loads(real_samples_json)
    synthetic = json.loads(synth_samples_json)
    res = synth.calculate_wasserstein_marginal_distance(real, synthetic)
    return json.dumps(res, indent=2)

@mcp.tool()
def evaluate_correlation_matrix_preservation(
    real_corr_matrix_json: str,
    synth_corr_matrix_json: str
) -> str:
    """
    Computes Frobenius norm difference and MAE between real and synthetic correlation matrices.
    """
    real_m = json.loads(real_corr_matrix_json)
    synth_m = json.loads(synth_corr_matrix_json)
    res = synth.evaluate_correlation_matrix_preservation(real_m, synth_m)
    return json.dumps(res, indent=2)

def main():
    print("Testing Data Synthesizer:")
    print(generate_laplace_differential_privacy_noise(100.0, 1.0, 1.0))

if __name__ == "__main__":
    main()
