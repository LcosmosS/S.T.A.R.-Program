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
        
        # Map real column names to what the pipeline expects
        rename_map = {
            'zHD': 'z',
            'zCMB': 'z',
            'm_b_corr': 'mu',
            'MU_SH0ES': 'mu',
            'm_b_corr_err_DIAG': 'sigma_mu',
            'MU_SH0ES_ERR_DIAG': 'sigma_mu',
            'dmu': 'sigma_mu'
        }
        df = df.rename(columns=rename_map)
        
        # Ensure required columns exist
        if 'z' not in df.columns:
            df['z'] = df.get('zHD', df.get('zCMB', df.get('zhel', 0.0)))
        if 'mu' not in df.columns:
            df['mu'] = df.get('m_b_corr', df.get('MU_SH0ES', df.get('mB', 0.0)))
        if 'sigma_mu' not in df.columns:
            df['sigma_mu'] = df.get('m_b_corr_err_DIAG', 
                                  df.get('MU_SH0ES_ERR_DIAG', 
                                       df.get('dmu', 0.15)))
        
        print(f"Loaded real Pantheon+ with {len(df)} supernovae")
        return df.to_dict('index')
    
    # Placeholder
    print("Using placeholder")
    return {
        0: {"z": 0.01, "mu": 32.5, "sigma_mu": 0.08},
        1: {"z": 0.05, "mu": 35.0, "sigma_mu": 0.10},
    }

PANTHEON_PLUS_FULL = load_pantheon_plus()
