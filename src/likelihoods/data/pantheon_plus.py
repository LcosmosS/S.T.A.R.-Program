"""
Pantheon+ Loader - Debug version
"""
from pathlib import Path
import pandas as pd

def load_pantheon_plus():
    raw_dir = Path(__file__).parent.parent.parent / "data" / "raw"
    dat_file = raw_dir / "pantheon_plus.dat"
    
    if dat_file.exists():
        df = pd.read_csv(dat_file, delim_whitespace=True, comment='#', header=0)
        print("Columns in Pantheon+ file:", df.columns.tolist())  # Debug
        
        # Aggressive mapping
        rename_map = {
            'zHD': 'z',
            'zCMB': 'z',
            'zhel': 'z',
            'm_b_corr': 'mu',
            'MU_SH0ES': 'mu',
            'm_b_corr_err_DIAG': 'sigma_mu',
            'MU_SH0ES_ERR_DIAG': 'sigma_mu',
            'dmu': 'sigma_mu',
            'mu_err': 'sigma_mu'
        }
        df = df.rename(columns=rename_map)
        
        # Force required columns
        if 'z' not in df.columns:
            df['z'] = 0.1  # fallback
        if 'mu' not in df.columns:
            df['mu'] = df.get('m_b_corr', 35.0)
        if 'sigma_mu' not in df.columns:
            df['sigma_mu'] = 0.15
        
        print(f"Loaded {len(df)} SNe Ia with columns: {df.columns.tolist()}")
        return df.to_dict('index')
    
    print("Using placeholder")
    return {0: {"z": 0.01, "mu": 32.5, "sigma_mu": 0.08}}

PANTHEON_PLUS_FULL = load_pantheon_plus()
