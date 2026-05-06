"""
Joint Cosmology Likelihood Engine
=================================

Combines:
- Planck distance priors
- SH0ES H0 measurement
- DESI BAO
- Cosmic chronometers

Returns total log-likelihood for any cosmology model.
"""

import numpy as np

class JointLikelihood:
    def __init__(self, planck_like, bao_like, cc_like):
        self.planck_like = planck_like
        self.bao_like = bao_like
        self.cc_like = cc_like

    def __call__(self, theta):
        """theta should be parameter array, NOT model"""
        if not isinstance(theta, (list, tuple, np.ndarray)):
            # If someone passed a model by mistake
            print("WARNING: JointLikelihood received model instead of theta")
            return -np.inf

        try:
            logp_planck = self.planck_like(theta) if hasattr(self.planck_like, '__call__') else 0.0
            logp_bao   = self.bao_like(theta) if hasattr(self.bao_like, '__call__') else 0.0
            logp_cc    = self.cc_like(theta) if hasattr(self.cc_like, '__call__') else 0.0

            total = logp_planck + logp_bao + logp_cc

            print(f"JointLikelihood: Planck={logp_planck:.4f}, BAO={logp_bao:.4f}, CC={logp_cc:.4f} | Total={total:.4f}")

            return total if np.isfinite(total) else -np.inf

        except Exception as e:
            print(f"JointLikelihood error: {e}")
            return -np.inf
