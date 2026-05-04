"""
Pantheon+ loader and module export.
Produces PANTHEON_PLUS_FULL as a dict of lists:
{
  "z": [...],
  "mu": [...],
  "sigma_mu": [...]
}
"""
from pathlib import Path
import pandas as pd
import numpy as np

def load_pantheon_plus():
    repo_root = Path(__file__).resolve().parents[3]   # Go up from src/likelihoods/data/
    csv_path = repo_root / "data" / "processed" / "pantheon_plus.csv"
    
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        
        # Normalize column names (in case of slight variations)
        rename_map = {
            "zHD": "z", "zCMB": "z", "zHEL": "z",
            "m_b_corr": "mu", "MU_SH0ES": "mu",
            "m_b_corr_err_DIAG": "sigma_mu", 
            "MU_SH0ES_ERR_DIAG": "sigma_mu",
            "dmu": "sigma_mu"
        }
        df = df.rename(columns=rename_map)
        
        # Ensure required columns
        if "z" not in df.columns or "mu" not in df.columns:
            raise KeyError(f"Missing essential columns. Found: {list(df.columns)}")
        
        if "sigma_mu" not in df.columns:
            df["sigma_mu"] = df.get("mu_err", 0.15)
        
        # Convert to numeric
        for col in ["z", "mu", "sigma_mu"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        
        df = df.dropna(subset=["z", "mu"]).reset_index(drop=True)
        
        print(f"Loaded Pantheon+ CSV: {len(df)} supernovae")
        return df   # ← Return DataFrame (easiest for plotting)
    
    else:
        print("Processed CSV not found — using placeholder")
        return pd.DataFrame({
            "z": [0.01, 0.05, 0.1, 0.5],
            "mu": [32.5, 35.0, 37.8, 42.5],
            "sigma_mu": [0.08, 0.10, 0.12, 0.18]
        })

# Export for the rest of the codebase
PANTHEON_PLUS_FULL = load_pantheon_plus()

# Module-level export used by the rest of the codebase
PANTHEON_PLUS_FULL = load_pantheon_plus()
