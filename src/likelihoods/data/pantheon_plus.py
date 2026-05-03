"""
Pantheon+ Full Dataset Loader
"""
from pathlib import Path
import pandas as pd

def load_pantheon_plus():
    """Load real Pantheon+ data from raw CSV/dat file."""
    raw_dir = Path(__file__).parent.parent.parent / "data" / "raw"
    
    # Try .dat first (official Pantheon+ format)
    dat_file = raw_dir / "pantheon_plus.dat"
    if dat_file.exists():
        # Pantheon+ .dat format is space-separated with specific columns
        df = pd.read_csv(dat_file, delim_whitespace=True, comment='#')
        # Rename to match what the plotting code expects
        if 'mu_err' in df.columns:
            df = df.rename(columns={'mu_err': 'sigma_mu'})
        return df
    
    # Fallback to placeholder if real file is missing
    print("Warning: Real Pantheon+ data not found. Using minimal placeholder.")
    return pd.DataFrame({
        "z": [0.01, 0.05, 0.1, 0.5, 1.0],
        "mu": [32.5, 35.0, 37.8, 42.5, 44.8],
        "sigma_mu": [0.08, 0.10, 0.12, 0.18, 0.22],
        "name": "Pantheon+ Placeholder"
    })

# Main export for the notebook
PANTHEON_PLUS_FULL = load_pantheon_plus()
