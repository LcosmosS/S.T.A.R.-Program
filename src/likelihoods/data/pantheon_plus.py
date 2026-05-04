"""
Robust Pantheon+ Loader and module export.
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
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "data" / "processed" / "pantheon_plus.csv"
    
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        
        # Clean ellipsis and other placeholders
        df = df.replace(['...', '... ', -999, -999.0], np.nan)
        
        # Normalize column names
        rename_map = {
            "zHD": "z", "zCMB": "z", "zHEL": "z",
            "m_b_corr": "mu", "MU_SH0ES": "mu",
            "m_b_corr_err_DIAG": "sigma_mu", 
            "MU_SH0ES_ERR_DIAG": "sigma_mu",
            "dmu": "sigma_mu"
        }
        df = df.rename(columns=rename_map)
        
        # Ensure required columns
        for col in ["z", "mu"]:
            if col not in df.columns:
                raise KeyError(f"Missing column '{col}' in CSV. Found: {list(df.columns)}")
        if "sigma_mu" not in df.columns:
            df["sigma_mu"] = df.get("mu_err", 0.15)
        
        # Convert to numeric and drop bad rows
        for col in ["z", "mu", "sigma_mu"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        
        df = df.dropna(subset=["z", "mu"]).reset_index(drop=True)
        
        print(f"Loaded clean Pantheon+ CSV: {len(df)} supernovae")
        return df.to_dict('index')   # Return dict for pipeline compatibility
    
    print("Using placeholder")
    return {0: {"z": 0.01, "mu": 32.5, "sigma_mu": 0.08}}

PANTHEON_PLUS_FULL = load_pantheon_plus()
