[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/LcosmosS/S.T.A.R.-Program)
---

# **The S.T.A.R. Program**  
## **Symbolic–Topological–Arithmetic–Relativity**
### **A Proposed Model for Mathematical & Theoretical Physics to Address Cosmic Expansion & the Hubble–Planck Tension**

---

**Author:** Patrick J. McNamara  
**ORCiD:** 0009‑0002‑8978‑5563  
**Project Start:** March 2025 — Active  
**Keywords:** Number Theory, Cosmology, Entropy Cohomology, Persistent Homology, Elliptic Curves, Symbolic Regression, Mathematical Physics, Theoretical Physics, Holography 

---

## **Overview**

This repository is the **primary research archive** for the **S.T.A.R. Program** — the *Symbolic–Topological–Arithmetic–Relativity Model* — a proposed theoretical physics framework that couples:

- **ACSC** — *Arithmetic–Cosmic Structure Conjecture* *( `/docs/The Arithmetic–Cosmic Structure Conjecture (ACSC) Monograph.pdf`)*
- **ECC** — *Entropy Cohomology Conjecture*  *( `/docs/The Entropy Cohomology Conjecture (ECC).pdf`)*

Together, these form a dual‑layer architecture:

- **ACSC** provides the *geometric projection law* mapping elliptic curve invariants into a cosmological manifold.  
- **ECC** provides the *entropy‑cohomological conservation law* governing symbolic information flow across that manifold.

The S.T.A.R. Program proposes that the **large‑scale structure of the universe**, the **effective expansion rate**, and the **Hubble–Planck tension** arise from the interaction between:

- arithmetic projection geometry  
- entropy curvature  
- persistent cohomology classes  
- symbolic geodesics  
- scalar‑field coupling  

This repository contains the **full theoretical monographs**, **computational toolkit**, **TDA stability pipeline**, and **symbolic regression engine** that define the S.T.A.R. Program.

- *(See [OVERVIEW.md](OVERVIEW.md) for a more in depth overview.)* 
- *(See  `/docs/_Arithmetic Invariants and Cosmological Geometry in Cartography_.pdf` for project details.)* 
- *(See [/docs/First_Principles.md](/docs/First_Principles.md), `/docs/first_principals.py` & `/docs/first_principals_results.txt` for evidance towards Hubble-Planck Tension resolution.)*


---

## **Core Idea**

The S.T.A.R. Program asserts that the universe can be projected as a **Symbolic Field**, where:

- arithmetic invariants  
- entropy curvature  
- topological persistence  
- and geometric projection laws  

jointly determine cosmic structure.

A central prediction of the S.T.A.R. Program is a **scale-dependent effective Hubble parameter** that naturally emerges from the arithmetic projection and entropy dynamics:

$H_{\rm eff}(z) = H_0 \cdot \langle \Omega_E \rangle_z$

where $\(\Omega_E\)$ is the real period of the elliptic curve \(E\), and the redshift-dependent average is taken over curves that are “visible” or dominant at redshift $\(z\)$:

$\langle \Omega_E \rangle_z = \frac{\sum_E w_E(z) \, \Omega_E}{\sum_E w_E(z)}.$

The weight function $\(w_E(z)\)$ is constructed from the model’s natural mechanisms:

- **Projection distortions and local-versus-global sampling**: At low $\(z\)$ (late universe, local distance ladder), the observer preferentially samples a biased subset of the projected point cloud $\(\{\Phi(E)\}\)$, favoring denser regions or lower-distortion patches after sinusoidal, oblate, and force-directed corrections. At high $\(z\)$ (CMB epoch), the average approaches the full global distribution.
  
- **Isogeny class density**: Curves connected by higher-degree isogenies contribute progressively more at later times, shifting the effective scale factor according to $\(g_{E'}(t) = g_E(t) + \eta \log m\)$.

This formulation produces regime-dependent values consistent with current observations:

$$
\frac{\dot{a}}{a}\bigg|_{\text{local (low } z)}
\approx H_0 \cdot \langle \Omega_E \rangle_{\text{late}}
\quad (\sim 72{-}74\ \text{km/s/Mpc})
$$

$$
\frac{\dot{a}}{a}\bigg|_{\text{CMB (high } z)}
\approx H_0 \cdot \langle \Omega_E \rangle_{\text{early}}
\quad (\sim 67.4\ \text{km/s/Mpc})
$$

The precise functional form of the weights $\(w_E(z)\)$ (including any tunable parameters) is **not imposed a priori**. Instead, the symbolic regression engine in `/src/symbolic_regression/` is trained on the full projected point cloud to discover the optimal weighting that best reconciles the projected arithmetic structure with observed cosmological data. This allows the model to learn the natural mapping from arithmetic invariants to effective expansion history without manual fine-tuning.

- *(See [/docs/Symbolic_Action_Principle.md](/docs/Symbolic_Action_Principle.md), `/docs/star_v3.1.py`, `/docs/star_v3.1 output.pdf`, & `/docs/STAR.ipynb`)*

## **The S.T.A.R. Trilogy Architecture**

This repository represents the **theory layering** of a three‑part research program:

### **1. ACSC — Geometry**  
*Arithmetic–Cosmic Structure Conjecture*  
Defines the projection map $\( \Phi(E) \)$, the k‑factor scaling, density‑equalizing rescaling, and the Global‑to‑Local Mapping Paradox Correction Theory.

### **2. ECC — Field Theory**  
*Entropy Cohomology Conjecture*  
Defines the entropy field $\( \mathcal{M}(x) \)$, the differential forms $\( \theta = d\mathcal{M} \)$, $\( \omega = d\theta \)$, and the cohomology class $\(\omega\)$ governing symbolic conservation.

### **3. S.T.A.R. Program — Combined Physics**  
*Symbolic–Topological–Arithmetic–Relativity Model*  
Combines ACSC + ECC into a full cosmological model with:

- metric perturbations  
- scalar‑field coupling  
- symbolic Sachs–Wolfe transfer  
- cosmic‑web alignment  
- symbolic regression law discovery
- *(See [/docs/Symbolic_Action_Principle.md](/docs/Symbolic_Action_Principle.md), `/docs/star_v3.1.py`, `star_v3.1 output.pdf`  [/docs/STAR.ipynb](/docs/STAR.ipynb), `/docs/_Arithmetic Invariants and Cosmological Geometry in Cartography_.pdf` & `/docs/Appendices for Arithmetic Invariants and Cosmological Geometry in Cartography.pdf`)*

This repository is the **central hub** of the S.T.A.R. Program, and ultimately proposes the introduction of a **Symbolic Field-Theory** paradigm.

*Future exploration and refinement to include a Symbolic-Topological-Arithemetic-Relativity-Mission-Analysis-Program (S.T.A.R.M.A.P.) for a *"topographical"* map of cosmic radiation and gravitational density, and S.T.A.R-Mission-Analysis-Tool (S.M.A.T.) akin to NASA'S General-Mission-Analysis-Tool (G.M.A.T.)* 

---

## **Repository Structure**

```
S.T.A.R.-Program/
├── README.md
├── LICENSE
├── CITATION.cff
│
├── src/
|   ├── acsc/                     # # ACSC projection geometry
|   ├── analysis/                 # Documentation generation
|   ├── blender/                  # Paradox correction + infinite zoom
|   ├── cli/                      # Cosmological inference constraints
|   ├── data/                     # Sky survey integration preprocessing
│   ├── entropy/                  # ECC entropy/cohomology machinery               
│   ├── likelihoods/              # Comparisons to Planck/SH0ES + DESI BAO + PANTHEON+
|   ├── pipeline/                 # Inference + PaperFigure pipelines
│   ├── physics/                  # S.T.A.R. cosmological physics
│   ├── symbolic_regression/      # Constrained GP + law discovery
│   ├── tda/                      # Persistent homology + stability
|   ├── tests/                    # Sky survey integration
|   ├── utils/                    # Astronomical utilities
|   └── visualization/            # PaperFigure + plotting
│    
├── data/
│   ├── raw/                      # LMFDB + Cremona datasets
│   └── processed/                # Cleaned + merged arithmetic data
│
├── notebooks/
│   ├── projection_demo.ipynb
│   ├── entropy_field_demo.ipynb
│   ├── hubble_tension_fit.ipynb
│   └── tda_analysis.ipynb
│
├── scripts/
│   ├── generate_raw.py
│   ├── compute_3selmer_full_pari.py
│   └── star_validation_batch.py
│
├── results/
│   ├── figures/
│   └── tables/
│
├── manuscript/                   # Full S.T.A.R. monograph (PDF + LaTeX)
├── theory-verification/          # PH barcodes + arithmetic point clouds
└── docs/                         # High-resolution diagrams + maps
```

---

## **Reproducibility Statement**

Reproducibility is a core principle of the S.T.A.R. Program.

- All projection operators  
- All entropy/cohomology computations  
- All TDA pipelines  
- All symbolic regression constraints  
- All cosmological fits  

are implemented in this repository.

The **v3.1 leakage‑free pipeline** achieves:

$R^2 = 0.9864$ (undergoing rigorous confirmation)

on synthetic cosmic structures, validated through:

- bootstrap persistence landscapes  
- Wasserstein stability  
- null‑scramble rejection  
- isogeny‑invariance tests  

Researchers are encouraged to:

- inspect the manuscript and thesis pdf's in `/docs`
- run the full validation pipeline in `/scripts`  
- explore the symbolic regression manifold in `/examples/exports`  
- [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/LcosmosS/S.T.A.R.-Program)
---

## **Installation**

```bash
git clone https://github.com/LcosmosS/S.T.A.R.-Program.git
cd ~/S.T.A.R.-Program
pip install -r requirements.txt
```

---

## **Citation**

If you use the S.T.A.R. Program, ACSC, ECC, or any associated data pipelines, please cite:

```
McNamara, P. J. (2026).
The S.T.A.R. Program: A Symbolic–Topological–Arithmetic–Relativity Model.
GitHub Repository.
https://github.com/LcosmosS/S.T.A.R.-Program
```

BibTeX:

```bibtex
@misc{mcnamara2026star,
  author       = {Patrick J. McNamara},
  title        = {The S.T.A.R. Program: A Symbolic--Topological--Arithmetic--Relativity Model},
  year         = {2026},
  howpublished = {\url{https://github.com/LcosmosS/S.T.A.R.-Program}},
  note         = {Combined ACSC + ECC Framework}
}
```

---
