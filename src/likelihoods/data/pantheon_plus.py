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
import sys
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_pantheon_plus():
    # Locate CSV relative to package root (two levels up from this file)
    pkg_root = Path(__file__).resolve().parent.parent.parent
    csv_path = pkg_root / "data" / "processed" / "pantheon_plus.csv"

    if not csv_path.exists():
        logger.warning("Pantheon+ CSV not found at %s", csv_path)
        # Return an empty but well-typed dataset so imports don't crash.
        return {"z": [], "mu": [], "sigma_mu": []}

    # Read as a comma-separated CSV (the file you provided uses commas)
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        logger.error("Failed to read Pantheon+ CSV: %s", e)
        return {"z": [], "mu": [], "sigma_mu": []}

    # If the CSV uses different column names, try to normalize
    rename_map = {
        "zHD": "z", "zCMB": "z", "zHEL": "z",
        "m_b_corr": "mu", "MU_SH0ES": "mu",
        "m_b_corr_err_DIAG": "sigma_mu", "MU_SH0ES_ERR_DIAG": "sigma_mu",
        "dmu": "sigma_mu"
    }
    df = df.rename(columns=rename_map)

    # If headerless CSV was written, try to recover first three columns
    if not set(["z", "mu", "sigma_mu"]).issubset(df.columns):
        # If the first three columns exist, assume they are z, mu, sigma_mu
        if df.shape[1] >= 3 and all(c.startswith("Unnamed") for c in df.columns[:3]):
            df = df.iloc[:, :3]
            df.columns = ["z", "mu", "sigma_mu"]

    # Keep only required columns if present
    if not set(["z", "mu", "sigma_mu"]).issubset(df.columns):
        logger.error("Pantheon+ CSV missing required columns. Available: %s", list(df.columns))
        return {"z": [], "mu": [], "sigma_mu": []}

    df = df[["z", "mu", "sigma_mu"]].copy()

    # Coerce to numeric and drop invalid rows
    for col in ["z", "mu", "sigma_mu"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    before = len(df)
    df = df.dropna().reset_index(drop=True)
    after = len(df)
    if after < before:
        logger.info("Dropped %d rows with non-numeric or missing values from Pantheon+ CSV", before - after)

    # Final sanity checks
    if df.empty:
        logger.error("Pantheon+ CSV contains no valid numeric rows after cleaning.")
        return {"z": [], "mu": [], "sigma_mu": []}

    return {
        "z": df["z"].astype(float).tolist(),
        "mu": df["mu"].astype(float).tolist(),
        "sigma_mu": df["sigma_mu"].astype(float).tolist()
    }

# Module-level export used by the rest of the codebase
PANTHEON_PLUS_FULL = load_pantheon_plus()
