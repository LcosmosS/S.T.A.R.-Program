"""
Cosmic Chronometer Likelihood
=============================

Gaussian likelihood for H(z) measurements from cosmic chronometers.
"""

from __future__ import annotations
import numpy as np
import pandas as pd


class CosmicChronometers:
    def __init__(self, cc_data):
        """
        cc_data can be:
        - a dict (embedded data module)
        - a CSV file path (legacy mode)
        """
        if isinstance(cc_data, dict):
            # Embedded data mode
            self.cc = cc_data
        else:
            # Legacy CSV mode
            df = pd.read_csv(cc_data)
            self.cc = {
                "z": df["z"].tolist(),
                "H": df["H"].tolist(),
                "sigma_H": df["sigma_H"].tolist(),
            }

