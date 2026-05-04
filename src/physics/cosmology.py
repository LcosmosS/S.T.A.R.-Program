from __future__ import annotations
import numpy as np
import sympy as sp
from scipy.integrate import quad

class Cosmology:
    """
    Cosmology engine with pluggable symbolic H(z).
    H_expr : str
        Sympy-compatible expression for H(z) (units: km/s/Mpc).
    params : dict
        Numeric parameter values used in H_expr.
    """
    c = 299792.458  # km/s

    def __init__(self, H_expr: str, params: dict):
        self.H_expr = H_expr
        self.params = {k: float(v) for k, v in (params or {}).items()}
        
        # Store original expression string for _evaluate
        self.expr = H_expr

        # Symbolic version
        z = sp.symbols("z")
        try:
            self.H_sym = sp.sympify(H_expr.replace("Ωm", "Om").replace("ΩΛ", "OL"))
        except Exception as e:
            raise ValueError(f"Failed to parse H_expr {H_expr!r}: {e}")

        # Lambdified fast version
        try:
            keys = tuple(self.params.keys())
            self.H = sp.lambdify((z, *keys), self.H_sym, modules=["numpy"])
        except Exception as e:
            raise RuntimeError(f"Failed to lambdify H_expr: {e}")

    def _evaluate(self, expr: str, z):
        """Safely evaluate symbolic expression at z (scalar or array)."""
        z = np.asarray(z)
        try:
            # Use lambdified version when possible
            return self.H(z, *self.params.values())
        except Exception:
            # Fallback numerical evaluation
            H0 = self.params.get('H0', 70.0)
            Om = self.params.get('Ωm', 0.3)
            OL = self.params.get('ΩΛ', 0.7)
            a = self.params.get('a', 0.0)
            b = self.params.get('b', 0.0)

            inside = Om * (1 + z)**3 + OL + a * z + b * z**2
            return H0 * np.sqrt(np.maximum(inside, 1e-10))

    def H_of_z(self, z):
        """Evaluate H(z)."""
        return self._evaluate(self.expr, z)

    def _comoving_scalar(self, zi: float) -> float:
        """Comoving distance for scalar redshift."""
        if not np.isfinite(zi) or zi < 0:
            raise ValueError(f"Invalid redshift z={zi}")

        def integrand(zp):
            Hz = float(self.H_of_z(zp))
            if Hz <= 0:
                raise RuntimeError(f"H(z) must be positive, got {Hz} at z={zp}")
            return self.c / Hz

        result, _ = quad(integrand, 0.0, float(zi), limit=200, epsabs=1e-8)
        return max(float(result), 0.0)

    def comoving_distance(self, z):
        """Dc(z) = c * ∫ dz'/H(z')"""
        z_arr = np.asarray(z)
        if z_arr.ndim == 0:
            return self._comoving_scalar(float(z_arr))
        
        return np.array([self._comoving_scalar(float(zi)) for zi in z_arr])

    def luminosity_distance(self, z):
        """DL = Dc * (1 + z)"""
        Dc = self.comoving_distance(z)
        z_arr = np.asarray(z)
        return Dc * (1.0 + z_arr)

    def distance_modulus(self, z):
        """μ = 5 log10(DL / 10 pc) with DL in Mpc"""
        DL_Mpc = self.luminosity_distance(z)
        DL_Mpc = np.maximum(DL_Mpc, 1e-6)   # safety
        
        if np.isscalar(DL_Mpc) or DL_Mpc.size == 1:
            dl = float(DL_Mpc)
            return 5.0 * (np.log10(dl * 1e6) - 1.0) if dl > 0 else -np.inf
        
        with np.errstate(divide='ignore', invalid='ignore'):
            mu = 5.0 * (np.log10(DL_Mpc * 1e6) - 1.0)
        return mu

    def angular_diameter_distance(self, z):
        """DA = Dc / (1 + z)"""
        return self.comoving_distance(z) / (1.0 + np.asarray(z))
