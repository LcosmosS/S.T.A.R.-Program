# Contributing to S.T.A.R. Program

**S.T.A.R. Program** (Symbolic–Topological–Arithmetic–Relativity) is an open research project exploring a novel framework for mathematical and theoretical physics. Contributions are welcome from researchers, developers, and enthusiasts committed to rigorous, reproducible, and innovative work at the intersection of mathematical-physics and number theory, topology, symbolic computation, theroetical-physics, and cosmology.

## Code of Conduct

All contributors are expected to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md), based on the [Contributor Covenant](https://www.contributor-covenant.org). Respectful, constructive, and inclusive collaboration is highly valued.

## Ways to Contribute

Contributions are welcome in several areas:

- **Theoretical Developments** — Extensions to the ACSC or ECC conjectures, new lemmas, or mathematical refinements.
- **Computational Cosmology** — Improvements to MCMC pipelines, likelihood functions, or symbolic regression.
- **Topological Data Analysis** — Enhancements to persistent homology pipelines and stability analysis.
- **Software Engineering** — Performance optimization, robustness, testing, and CI/CD improvements.
- **Documentation & Visualization** — Better notebooks, figures, and explanatory materials.
- **Data & Infrastructure** — Curating cosmological datasets and improving data loaders.

## Development Setup

### Prerequisites
- Python 3.10+
- SageMath (recommended for symbolic computation)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/LcosmosS/S.T.A.R.-Program.git
```
```bash
# checkout the repository
cd S.T.A.R.-Program
```
```bash
# Install in editable mode with development dependencies
pip install -e ".[dev]"
```
```bash
# (Optional but recommended) Install SageMath packages if needed
sage -pip install -e ".[dev]"
```
### Running Notebooks

All core demonstrations are in the examples/ directory:
```bash
jupyter nbconvert --to notebook --execute examples/full_cosmology_inference.ipynb --output examples/full_cosmology_inference-executed.ipynb
```
### Project Structure
```
textsrc/
├── likelihoods/           # Data loaders and cosmological likelihoods
├── physics/               # Core models, symbolic cosmology, and MCMC
├── pipeline/              # Analysis and figure-generation pipelines
├── visualization/         # Publication-quality plotting tools
├── acsc/                  # Arithmetic-Cosmic Structure Conjecture modules
├── ecc/                   # Entropy Cohomology Conjecture modules
└── tda/                   # Topological Data Analysis tools

examples/                  # Jupyter notebooks demonstrating key features
data/                      # Raw and processed cosmological datasets
```
### Pull Request Process

Fork the repository and create a feature branch:
```bash
git checkout -b feature/your-contribution-name
```
Make your changes following the style guidelines below.
Ensure all modified notebooks execute successfully.
Submit a Pull Request with a clear title and description.

### PR Requirements

Clear motivation and description of changes
All affected notebooks must run end-to-end
Code must pass Black formatting
Appropriate tests or validation (when applicable)
Updated documentation where relevant

### Style Guide

Code Formatting: Use Black with default settings.
Docstrings: Google style.
Type Hints: Encouraged for new code.
Naming: Use descriptive variable and function names.
Reproducibility: Prefer explicit seeds and deterministic behavior where possible.

### Testing
```bash
# Run all notebooks (recommended before submitting PR)
./scripts/run_all_notebooks.sh
```
### Recognition
All contributors will be acknowledged in the AUTHORS.md file and in relevant publications where appropriate. Significant theoretical or algorithmic contributions may warrant co-authorship on resulting papers.

### Questions?
Feel free to open a Discussion or contact the maintainer.

**Thank you for contributing to the advancement of mathematical and theoretical physics.**
