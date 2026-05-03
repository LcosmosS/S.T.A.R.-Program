"""
Pantheon+ Loader 
"""
from pathlib import Path
import pandas as pd

def load_pantheon_plus():
    raw_dir = Path(__file__).parent.parent.parent / "data" / "raw"
    dat_file = raw_dir / "pantheon_plus.dat"
    
    if dat_file.exists():
        df = pd.read_csv(dat_file, delim_whitespace=True, comment='#', header=0)
        
        # Standardize columns
        if 'mu_err' in df.columns:
            df = df.rename(columns={'mu_err': 'sigma_mu'})
        if 'z' not in df.columns:
            df['z'] = df.get('zcmb', df.get('zhel', df.get('z', 0.0)))
        if 'mu' not in df.columns:
            df['mu'] = df.get('mu', df.get('mB', 0.0))
        if 'sigma_mu' not in df.columns:
            df['sigma_mu'] = df.get('dmu', 0.15)
        
        print(f"Loaded real Pantheon+ with {len(df)} SNe Ia")
        return df.to_dict('index')   # <-- dict with integer keys (matches other datasets)
    
    # Placeholder fallback
    print("Using Pantheon+ placeholder")
    return {
        0: {"z": 0.01, "mu": 32.5, "sigma_mu": 0.08},
        1: {"z": 0.05, "mu": 35.0, "sigma_mu": 0.10},
        2: {"z": 0.1,  "mu": 37.8, "sigma_mu": 0.12},
        3: {"z": 0.5,  "mu": 42.5, "sigma_mu": 0.18},
    }

PANTHEON_PLUS_FULL = load_pantheon_plus()
