"""
Paper-Ready Cosmology Figure Pipeline
=====================================

This module automates the generation of all paper-ready figures for the
S.T.A.R. cosmology model:

- Hubble diagram
- H(z) comparison
- Distance modulus curves
- Residuals
- Posterior corner plots
- Best-fit parameter extraction
- Constraint table generation

Works entirely with embedded Python dictionaries (CI-safe).
"""

from __future__ import annotations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import corner
import os

from src.physics.cosmology import Cosmology
from src.physics.symbolic_cosmology import SymbolicCosmology


class PaperFiguresPipeline:
    """
    Automated figure generator for cosmology inference results.

    Parameters
    ----------
    chain : ndarray
        MCMC chain of shape (nsteps, nparams)
    param_names : list[str]
        Names of parameters in the chain
    H_expr : str
        Symbolic expression for H(z)
    data_paths : dict
        Dictionary containing embedded datasets:
        {
            "planck": PLANCK_2015,
            "bao": DESI_BAO_DR1,
            "cc": COSMIC_CHRONOMETERS
        }
    """

    def __init__(self, chain, param_names, H_expr, data_paths):
        self.chain = chain
        self.param_names = param_names
        self.H_expr = H_expr
        self.data_paths = data_paths

    # ---------------------------------------------------------
    # Best-fit extraction
    # ---------------------------------------------------------
    def best_fit_params(self):
        return np.mean(self.chain, axis=0)

    def best_fit_model(self):
        params = dict(zip(self.param_names, self.best_fit_params()))
        return SymbolicCosmology(self.H_expr, params)

    # ---------------------------------------------------------
    # Data loading (dict → DataFrame)
    # ---------------------------------------------------------
    def _load_df(self, data):
        if isinstance(data, dict):
            return pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            return data.copy()
        else:
            raise TypeError("Data must be a dict or DataFrame")

    # ---------------------------------------------------------
    # Figure generation
    # ---------------------------------------------------------
    def plot_corner(self, output_dir):
        fig = corner.corner(self.chain, labels=self.param_names, show_titles=True)
        fig.savefig(os.path.join(output_dir, "corner_plot.png"), dpi=200)
        plt.close(fig)

    def plot_Hz(self, star, output_dir):
        z = np.linspace(0, 2, 200)
        H_star = np.array([star.H(zi) for zi in z])

        plt.figure(figsize=(10, 6))
        plt.plot(z, H_star, label="S.T.A.R.", lw=2)
        plt.xlabel("z")
        plt.ylabel("H(z)")
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "Hz.png"), dpi=200)
        plt.close()

    def plot_residuals(self, df, lcdm, star, output_dir):
        z = df["z"].values
        mu_obs = df["mu"].values

        mu_lcdm = np.array([lcdm.distance_modulus(zi) for zi in z])
        mu_star = np.array([star.distance_modulus(zi) for zi in z])

        plt.figure(figsize=(10, 4))
        plt.scatter(z, mu_obs - mu_lcdm, s=10, label="Obs - ΛCDM")
        plt.scatter(z, mu_obs - mu_star, s=10, label="Obs - S.T.A.R.")
        plt.axhline(0, color="black", lw=1)
        plt.xlabel("z")
        plt.ylabel("Residual μ")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "residuals.png"), dpi=200)
        plt.close()

    # ---------------------------------------------------------
    # Main pipeline
    # ---------------------------------------------------------
    def run(self, output_dir):
        os.makedirs(output_dir, exist_ok=True)

        # Load datasets
        df_planck = self._load_df(self.data_paths["planck"])

        # Build models
        star = self.best_fit_model()
        lcdm = Cosmology("H0*sqrt(Ωm*(1+z)**3 + ΩΛ)", {"H0": 70, "Ωm": 0.3, "ΩΛ": 0.7})

        # Generate figures
        self.plot_corner(output_dir)
        self.plot_Hz(star, output_dir)
        self.plot_residuals(df_planck, lcdm, star, output_dir)

        # Return constraints
        constraints = dict(zip(self.param_names, self.best_fit_params()))
        return constraints
