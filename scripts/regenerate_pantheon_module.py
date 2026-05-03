#!/usr/bin/env python3
# scripts/regenerate_pantheon_module.py
import pandas as pd
from pathlib import Path
import sys

RAW = Path("data/raw/pantheon_plus.dat")
OUT = Path("src/likelihoods/data/pantheon_plus.py")  # canonical module

if not RAW.exists():
    print(f"Error: {RAW} not found. Place pantheon_plus.dat in data/raw/", file=sys.stderr)
    sys.exit(1)

df = pd.read_csv(RAW, delim_whitespace=True, comment="#", header=0)

rename_map = {
    "zHD": "z", "zCMB": "z",
    "m_b_corr": "mu", "MU_SH0ES": "mu",
    "m_b_corr_err_DIAG": "sigma_mu", "MU_SH0ES_ERR_DIAG": "sigma_mu",
    "dmu": "sigma_mu"
}
df = df.rename(columns=rename_map)

# Resolve alternatives
df["z"] = df.get("z", df.get("zHD", df.get("zCMB")))
df["mu"] = df.get("mu", df.get("m_b_corr", df.get("MU_SH0ES")))
df["sigma_mu"] = df.get("sigma_mu", df.get("m_b_corr_err_DIAG", df.get("MU_SH0ES_ERR_DIAG")))

# Keep only required columns and drop missing / non-numeric rows
df = df[["z", "mu", "sigma_mu"]].dropna()
df = df.astype(float)

z = df["z"].tolist()
mu = df["mu"].tolist()
sigma = df["sigma_mu"].tolist()

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, "w") as f:
    f.write("# Auto-generated Pantheon+ dataset (numeric lists)\n")
    f.write("# Do not edit manually. Regenerate with scripts/regenerate_pantheon_module.py\n\n")
    f.write("PANTHEON_PLUS_FULL = {\n")
    f.write(f"    'z': {z},\n")
    f.write(f"    'mu': {mu},\n")
    f.write(f"    'sigma_mu': {sigma}\n")
    f.write("}\n")

print('Wrote', OUT, 'with', len(z), 'SNe')
