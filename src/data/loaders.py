from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[2] / "data" / "raw"

def load_sky_surveys():
    sky_2mass_gaia = pd.read_csv(DATA / "JApJ94494_2MASS_GAIADR3_EPOCH.csv")
    sky_sdss_desi_simbad = pd.read_csv(DATA / "DESIDR8_SDSSDR16_SIMBAD.csv")
    return sky_2mass_gaia, sky_sdss_desi_simbad
