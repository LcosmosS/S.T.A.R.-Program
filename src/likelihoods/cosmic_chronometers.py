"""
Cosmic Chronometer Likelihood
=============================

Gaussian likelihood for H(z) measurements from cosmic chronometers.
"""

from __future__ import annotations
import numpy as np
import pandas as pd


class CosmicChronometers:
    def __init__(self, cc_csv):
        self.cc = pd.read_csv(cc_csv)

    def log_likelihood(self, model):
        z = self.cc["z"].values
        H_obs = self.cc["H"].values
        sigma = self.cc["sigma_H"].values

        H_model = np.array([model.H(zi) for zi in z])
        chi2 = np.sum(((H_obs - H_model) / sigma)**2)
        return -0.5 * chi2
