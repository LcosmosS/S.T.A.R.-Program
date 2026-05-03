"""
Pantheon+ Full Dataset Loader 
"""
from pathlib import Path
import pandas as pd

def load_pantheon_plus():
    raw_dir = Path(__file__).parent.parent.parent / "data" / "raw"
    dat_file = raw_dir / "pantheon_plus.dat"
    
    if dat_file.exists():
        # Read the real Pantheon+ .dat file
        df = pd.read_csv(dat_file, delim_whitespace=True, comment='#')
        
        # Standardize column names
        if 'mu_err' in df.columns and 'sigma_mu' not in df.columns:
            df = df.rename(columns={'mu_err': 'sigma_mu'})
        
        # Convert to dict format expected by the pipeline
        return df.to_dict('records')   # <-- This is the key change
    
    # Fallback placeholder
    print("Warning: Real Pantheon+ data not found. Using placeholder.")
    return [
        {"z": 0.01, "mu": 32.5, "sigma_mu": 0.08},
        {"z": 0.05, "mu": 35.0, "sigma_mu": 0.10},
        {"z": 0.1,  "mu": 37.8, "sigma_mu": 0.12},
        {"z": 0.5,  "mu": 42.5, "sigma_mu": 0.18},
        {"z": 1.0,  "mu": 44.8, "sigma_mu": 0.22},
    ]

# Export for the notebook
PANTHEON_PLUS_FULL = load_pantheon_plus()
