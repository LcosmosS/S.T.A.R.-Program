"""
Top‑level package initializer for the S.T.A.R. model.
"""

# Re-export subpackages for convenience (optional)
from . import entropy
from . import physics
from . import tda
from . import symbolic_regression
from . import acsc

__all__ = [
    "entropy",
    "physics",
    "tda",
    "symbolic_regression",
    "acsc",
]

# ensure numeric parameter values (avoid sympy types)
self.params = {k: float(v) for k, v in (params or {}).items()}
# then lambdify using the stable key order
keys = tuple(self.params.keys())
self.H = sp.lambdify((z, *keys), self.H_sym, modules=["numpy"])
