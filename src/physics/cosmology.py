"""
Cosmology Engine with Symbolic H(z)
==================================

This module defines a Cosmology class that accepts a symbolic expression
for H(z), parses it with sympy, lambdifies it, and integrates it to compute:

- comoving distance
- luminosity distance
- angular diameter distance
- distance modulus

This architecture supports:
- ΛCDM
- S.T.A.R. Model
- symbolic regression models
- arbitrary expansion histories
"""

from __future__ import annotations
import numpy as np
import sympy as sp
from scipy.integrate import quad


class Cosmology:
    """
    Cosmology engine with pluggable symbolic H(z).

    Parameters
    ----------
    H_expr : str
        A sympy-compatible expression for H(z).
        Example: "H0*sqrt(Ωm*(1+z)**3 + ΩΛ + a*z + b*z**2)"
    params : dict
        Dictionary of parameters appearing in H_expr.
        Example: {"H0": 70, "Ωm": 0.3, "ΩΛ": 0.7, "a": 0.1, "b": -0.02}
    """

    c = 299792.458  # speed of light in km/s

    def __init__(self, H_expr: str, params: dict):
        self.H_expr = H_expr
        self.params = params

        # Symbolic variable
        z = sp.symbols("z")

        # Parse expression
        self.H_sym = sp.sympify(H_expr)

        # Lambdify for fast evaluation
        self.H = sp.lambdify(
            (z, *params.keys()),
            self.H_sym,
            modules=["numpy"]
        )

    def H_of_z(self, z):
        """Evaluate H(z) numerically."""
        return self.H(z, *self.params.values())

    def comoving_distance(self, z):
    """
    Compute comoving distance Dc(z) = c * ∫_0^z dz' / H(z').
    Accepts scalar or array-like z. Returns float for scalar input or np.ndarray for array input.
    Raises RuntimeError on evaluation/integration failures and ValueError for invalid z.
    """
    def _comoving_scalar(zi):
        if not np.isfinite(zi):
            raise ValueError(f"Invalid redshift z={zi!r}; must be finite.")
        if zi < 0:
            raise ValueError(f"Invalid redshift z={zi!r}; must be non-negative.")

        def integrand(zp):
            try:
                Hz = self.H_of_z(zp)
            except Exception as e:
                raise RuntimeError(f"H(z) evaluation failed at z={zp}: {e}")

            # Reject Ellipsis or non-finite values
            if Hz is Ellipsis:
                raise RuntimeError(f"H(z) returned Ellipsis at z={zp}")
            Hz_arr = np.asarray(Hz)
            if Hz_arr.size != 1:
                raise RuntimeError(f"H(z) must return a scalar for scalar input; got shape {Hz_arr.shape} at z={zp}")
            Hz_val = float(Hz_arr)
            if not np.isfinite(Hz_val) or Hz_val == 0.0:
                raise RuntimeError(f"H(z) returned non-finite or zero value {Hz_val!r} at z={zp}")
            return self.c / Hz_val

        try:
            result, err = quad(integrand, 0.0, float(zi), limit=100)
        except Exception as e:
            raise RuntimeError(f"Integration of 1/H(z) failed for z={zi}: {e}")
        if not np.isfinite(result):
            raise RuntimeError(f"Integration produced non-finite result for z={zi}: {result!r}")
        return float(result)

    # Handle scalar vs array-like inputs
    try:
        z_arr = np.asarray(z)
    except Exception as e:
        raise TypeError(f"Could not convert z to array-like: {e}")

    if z_arr.ndim == 0:
        return _comoving_scalar(float(z_arr))
    else:
        # preserve input shape
        flat = z_arr.ravel()
        out = np.empty_like(flat, dtype=float)
        for i, zi in enumerate(flat):
            out[i] = _comoving_scalar(float(zi))
        return out.reshape(z_arr.shape)

    def luminosity_distance(self, z):
    """
    Luminosity distance DL(z) = (1+z) * Dc(z).
    Accepts scalar or array-like z and returns same shape as input.
    Raises the same errors as comoving_distance when underlying computations fail.
    """
    Dc = self.comoving_distance(z)
    # Broadcast (1+z) with Dc safely using numpy
    try:
        z_arr = np.asarray(z)
        return (1.0 + z_arr) * Dc
    except Exception as e:
        # If Dc is scalar and z is scalar this will still work; otherwise raise clear error
        raise RuntimeError(f"Failed to compute luminosity distance for z={z!r}: {e}")

    def angular_diameter_distance(self, z):
        """DA = Dc / (1+z)."""
        return self.comoving_distance(z) / (1 + z)

    def distance_modulus(self, z):
        """μ = 5 log10(DL / 10 pc). DL in Mpc."""
        DL_Mpc = self.luminosity_distance(z)
        DL_pc = DL_Mpc * 1e6
        return 5 * (np.log10(DL_pc) - 1)
