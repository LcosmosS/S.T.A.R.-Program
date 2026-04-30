"""
DESI BAO Likelihood
===================

Implements Gaussian likelihood for DESI BAO measurements:
- D_M(z) / r_d
- H(z) * r_d
"""

from __future__ import annotations
import numpy as np
import pandas as pd


class DESIBAO:
    def __init__(self, bao_csv, r_d=147.1):
        """
        Parameters
        ----------
        bao_csv : str
            CSV containing DESI BAO measurements
        r_d : float
            Sound horizon at drag epoch
        """
        self.bao = pd.read_csv(bao_csv)
        self.r_d = r_d

    def log_likelihood(self, model):
        chi2 = 0

        for _, row in self.bao.iterrows():
            z = row["z"]
            DM_over_rd_obs = row["DM_over_rd"]
            H_rd_obs = row["H_rd"]
            sigma_DM = row["sigma_DM"]
            sigma_H = row["sigma_H"]

            # Model predictions
            Dc = model.comoving_distance(z)
            DM_over_rd_model = Dc / self.r_d
            H_rd_model = model.H(z) * self.r_d

            chi2 += ((DM_over_rd_obs - DM_over_rd_model) / sigma_DM)**2
            chi2 += ((H_rd_obs - H_rd_model) / sigma_H)**2

        return -0.5 * chi2
