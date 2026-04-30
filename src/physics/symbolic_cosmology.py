"""
Symbolic Regression Integration for Cosmology
=============================================

This module integrates symbolic regression models with the Cosmology engine.
It accepts a sympy expression or a string expression for H(z), and wraps it
into a Cosmology instance.

Used to test alternative expansion histories and Hubble tension resolutions.
"""

from __future__ import annotations
import sympy as sp
from src.physics.cosmology import Cosmology


class SymbolicCosmology:
    """
    Wraps a symbolic regression model into a Cosmology engine.

    Parameters
    ----------
    H_expr : str or sympy.Expr
        Symbolic expression for H(z).
    params : dict
        Parameter dictionary for the expression.
    """

    def __init__(self, H_expr, params):
        if isinstance(H_expr, sp.Expr):
            H_expr = str(H_expr)

        self.H_expr = H_expr
        self.params = params

        self.cosmo = Cosmology(H_expr, params)

    def H(self, z):
        return self.cosmo.H_of_z(z)

    def distance_modulus(self, z):
        return self.cosmo.distance_modulus(z)

    def comoving_distance(self, z):
        return self.cosmo.comoving_distance(z)

    def luminosity_distance(self, z):
        return self.cosmo.luminosity_distance(z)
