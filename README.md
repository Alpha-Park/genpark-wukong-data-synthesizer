# genpark-wukong-data-synthesizer

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Wukong Data Synthesizer is a zero-dependency differential privacy and synthetic data validation engine implementing the Laplace mechanism for privacy budget $\epsilon$, 1D Wasserstein Earth Mover's Distance distribution fidelity scoring, and Frobenius norm correlation preservation matrices.

```mermaid
flowchart LR
    A[Real Numeric Column] --> B[Laplace Mechanism Perturber]
    B --> C[Epsilon-Differentially Private Dataset]
    D[Real vs Synthetic Quantiles] --> E[Wasserstein W1 Distance Solver]
    E --> F[Empirical Distribution Fidelity Score]
    G[Pairwise Correlation Matrices] --> H[Frobenius Norm & MAE Comparator]
    H --> I[Structural Preservation Score]
```

## Features
- **Laplace Differential Privacy**: Synthesizes noise scaled to $b = \Delta f / \epsilon$ with rigorous 95% confidence intervals.
- **Wasserstein Distance Metric**: Measures exact Earth Mover's Distance $W_1$ normalized to empirical interquartile ranges.
- **Correlation Matrix Fidelity**: Verifies that synthetic feature covariance matrices preserve underlying multivariate relationships.

## Quickstart

```python
from client import GenParkWukongDataSynthesizer

synth = GenParkWukongDataSynthesizer()
res = synth.generate_laplace_differential_privacy_noise(100.0, epsilon=1.0)
print("Privatized Value:", res["privatized_value"])
```

## License
MIT
