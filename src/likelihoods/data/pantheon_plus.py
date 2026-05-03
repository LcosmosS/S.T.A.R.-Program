"""
Pantheon+ Loader 
"""
from pathlib import Path
import pandas as pd

def load_pantheon_plus():
    raw_dir = Path(__file__).parent.parent.parent / "data" / "raw"
    dat_file = raw_dir / "pantheon_plus.dat"
    
    if dat_file.exists():
        # Read Pantheon+ .dat format
        df = pd.read_csv(dat_file, delim_whitespace=True, comment='#', header=0)
        
        # Standardize column names to what the pipeline expects
        rename_map = {
            'z': 'z',
            'mu': 'mu',
            'mu_err': 'sigma_mu',
            'dmu': 'sigma_mu',      # sometimes used
        }
        df = df.rename(columns=rename_map)
        
        # Ensure required columns exist
        if 'z' not in df.columns or 'mu' not in df.columns:
            df['z'] = df.get('zcmb', df.get('zhel', 0.0))
            df['mu'] = df.get('mu', df.get('mB', 0.0))
            if 'sigma_mu' not in df.columns:
                df['sigma_mu'] = df.get('mu_err', df.get('dmu', 0.15))
        
        print(f"Loaded real Pantheon+ with {len(df)} supernovae")
        return df.to_dict('records')
    
    # Fallback
    print("Using placeholder Pantheon+ data")
    return [
        {"z": 0.01, "mu": 32.5, "sigma_mu": 0.08},
        {"z": 0.05, "mu": 35.0, "sigma_mu": 0.10},
        {"z": 0.1,  "mu": 37.8, "sigma_mu": 0.12},
    ]

PANTHEON_PLUS_FULL = load_pantheon_plus()
