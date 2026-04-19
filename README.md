---

# **Arithmetic–Cosmic Structure Conjecture (ACSC) — Reproducible Pipeline**

This repository contains the full computational framework for testing the **Arithmetic–Cosmic Structure Conjecture (ACSC)**: a proposed structural correspondence between the arithmetic invariants of elliptic curves over ℚ and the large‑scale topology of cosmic structure.

The code, data pipeline, and documentation here implement the preregistered falsification protocol described in the manuscript *“The Arithmetic–Cosmic Structure Conjecture (ACSC)”*. All steps—from data ingestion to projection, quantile alignment, TDA computation, null models, and statistical testing—are fully reproducible.

---

## **1\. Overview**

The ACSC asserts that after applying a stable, rank‑normalized projection

 prime : E → ℝ3

 to elliptic curves E/ℚ, and aligning the resulting point cloud to observational cosmic data via a non‑linear quantile transform, the persistent homology of the arithmetic cloud approximates that of the cosmic web with bounded error.

This repository provides:

* A complete implementation of the projection family (primary \+ alternatives)  
* Quantile alignment tools  
* TDA pipeline (GUDHI/Ripser)  
* Null models A–D  
* Statistical tests and decision rules  
* Ablation and robustness experiments  
* Reproducible environment (Dockerfile, requirements, notebooks)

---

## **2\. Repository Structure**

Arithmetic-Cosmic-Structure-Conjecture-ACSC/  
├── README.md  
├── LICENSE  
├── CITATION.cff  
├── acsc/                          \# Core Python package  
│   ├── \_\_init\_\_.py  
│   ├── core.py                    \# Complexity-14 filter, scarcity functions  
│   ├── validation.py              \# Rank consistency, statistics  
│   └── utils.py  
├── data/  
│   ├── raw/  
│   │   ├── cremona\_raw\_parsed.csv  
│   │   └── lmfdb\_raw\_parsed.csv  
│   └── processed/  
│       ├── cremona\_3selmer\_full\_pari.csv  
│       ├── lmfdb\_3selmer\_full\_pari.csv  
│       └── acsc\_final\_combined.csv  
├── notebooks/  
│   ├── 01\_data\_preparation.ipynb  
│   ├── 02\_complexity14\_filter.ipynb  
│   └── 03\_acsc\_statistics.ipynb  
├── scripts/  
│   ├── generate\_raw.py  
│   ├── compute\_3selmer\_full\_pari.py  
│   └── acsc\_validation\_batch.py  
├── results/  
│   ├── figures/  
│   │   └── acsc\_scarcity\_plot.png  
│   └── tables/  
├── docker/  
│   └── Dockerfile  
├── requirements.txt  
└── pyproject.toml                 \# or setup.py

---

## **3\. Data Requirements**

### **Arithmetic Data**

* Source: Cremona/LMFDB or SageMath tables  
* Pre‑registered bound: N  N  
* Must include **full isogeny classes**  
* Required invariants:  
   Delta (Δ), N, r, R, Omega (𝛀), T 

### **Cosmic Data**

* Source: SDSS or DESI  
* Must be **volume‑limited** and in **comoving coordinates**  
* Pre‑register survey, cuts, and volume

---

## **4\. Projection Maps** 

### **Primary Projection (** prime **)**

Implements the rank‑normalized spherical projection described in the manuscript, including:

* Radial coordinate   
    VE \= V0 TElog(𝛀E/2π)RE1/max(1/rE)exp(𝜳r(E))    
    
* Angular coordinates  
   \[ \\theta\_E \= \\mathrm{mod}(\\log\_{10}|\\Delta\_E|, 2\\pi), \\quad \\phi\_E \= \\mathrm{mod}(\\pi \\log\_{10} N\_E, \\pi) \]

### **Alternative Projections**

* **PTD**: ((\\log|\\Delta|, \\log\\Omega, \\log(1+|E(\\mathbb{Q})\_{\\mathrm{tors}}|)))  
* **MCJ**: ((\\log N, \\log j(E), \\log(1+R)))

All constants (e.g., (V\_0), (N\_{\\max}), scaling factors) must be pre‑registered.

---

## **5\. Domain Alignment (Quantile Transform)**

Implements the coordinate‑wise non‑linear quantile alignment:

1. Fit empirical CDFs (F\_j^{\\mathrm{cosmo}}) on the cosmic cloud  
2. Fit empirical CDFs (F\_j^{\\mathrm{arith}}) on the arithmetic cloud  
3. Transform each coordinate via  
    \[ p\_j \\mapsto (F\_j^{\\mathrm{cosmo}})^{-1}(F\_j^{\\mathrm{arith}}(p\_j)) \]

This step ensures marginal distributions match, isolating **structural** differences.

---

## **6\. Topological Data Analysis**

* Vietoris–Rips complexes (GUDHI or Ripser)  
* Pre‑registered filtration range (\[\\varepsilon\_{\\min}, \\varepsilon\_{\\max}\])  
* Compute persistence diagrams (D\_k) for (k \= 0,1,2)  
* Primary metric: **2‑Wasserstein distance** (W\_2(D\_k(P), D\_k(M)))

### **Topological Locked Scale**

Choose one (pre‑registered):

* Fixed: (\\varepsilon\_\* \= 25.0) Mpc  
* Adaptive: median k‑NN distance of cosmic data

---

## **7\. Null Models**

Implemented nulls:

* **Null‑A**: Uniform random points  
* **Null‑B**: Permuted invariants (e.g., shuffle (r\_E))  
* **Null‑C**: Alternative projections (PTD, MCJ)  
* **Null‑D**: Poisson process matched to cosmic density

Each null is run with (m \\ge 50\) repetitions.

---

## **8\. Statistical Testing**

For each homological degree (k):

* Compute observed (W\_k^{\\mathrm{obs}})  
* Compute empirical null distributions  
* One‑sided p‑value:  
   \[ p\_{k,j} \= \\frac{1 \+ \#{i : W\_{k,j}(i) \\le W\_k^{\\mathrm{obs}}}}{m+1} \]  
* Multiple testing correction: **Benjamini–Hochberg (FDR 0.05)**

### **Decision Rule (Falsification)**

Support ACSC if:

* (W\_k^{\\mathrm{obs}} \< \\varepsilon\_k) for all (k)  
* For at least one null model, (p\_{1,j} \< 0.01) after correction

Otherwise: **fail to reject H₀** (ACSC falsified for this Φ and dataset).

---

## **9\. Robustness & Ablation**

Includes:

* Subsample stability  
* Gaussian jitter tests  
* Parameter sweeps over (N\_{\\max}, \\Delta\_{\\max}, \\alpha)  
* Ablation of invariants (e.g., remove (R\_E) or Ψ\_r)  
* Cross‑survey validation (SDSS → DESI)

All robustness criteria are pre‑specified.

---

## **10\. Reproducibility**

This repository includes:

* **Dockerfile** with pinned versions  
* `requirements.txt`  
* All scripts and notebooks needed to reproduce figures and tables  
* Random seeds and manifest of all inputs  
* Instructions for running the full pipeline end‑to‑end

---

## **11\. Quick Start**

### **Build the environment**

docker build \-t acsc .  
docker run \-it \--rm \-v $PWD:/workspace acsc

### **Run the full pipeline**

python \-m acsc.run\_all \--config configs/default.yaml

### **Or explore interactively**

Open JupyterLab inside the container:

jupyter lab \--ip=0.0.0.0 \--allow-root

---

## **12\. Citation**

If you use this code, please cite the ACSC manuscript:

“The Arithmetic–Cosmic Structure Conjecture (ACSC).”  
 *Manuscript in preparation.*

---

## **13\. License**

MIT License (or your preferred license).

---

