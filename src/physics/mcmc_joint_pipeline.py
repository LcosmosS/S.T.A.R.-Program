"""
Full MCMC Pipeline for Joint Cosmology Likelihood
=================================================

Runs Metropolis–Hastings MCMC using:
- Planck + SH0ES
- DESI BAO
- Cosmic Chronometers
"""

from __future__ import annotations
import numpy as np
from src.physics.symbolic_cosmology import SymbolicCosmology

class JointMCMCPipeline:
    """
    Numerically stable Metropolis–Hastings MCMC for the S.T.A.R. Model.

    Fixes included:
    - Rejects proposals that produce invalid cosmologies (negative sqrt argument)
    - Rejects proposals that produce NaN or inf log-likelihoods
    - Clamps sqrt arguments inside SymbolicCosmology
    - Prevents overflow in exp(logp_new - logp)
    - Enforces physical priors explicitly
    """

    def __init__(self, H_expr, param_names, priors, proposal_widths, joint_likelihood):
        self.H_expr = H_expr
        self.param_names = param_names
        self.priors = priors
        self.proposal_widths = proposal_widths
        self.joint_likelihood = joint_likelihood

    # ------------------------------------------------------------
    # PRIOR
    # ------------------------------------------------------------
    def _log_prior(self, theta):
        """
        Gaussian priors with explicit physical constraints.
        """
        for val, name in zip(theta, self.param_names):
            mu, sigma = self.priors[name]

            # Physical constraints
            if name == "Ωm" and val < 0:
                return -np.inf
            if name == "ΩΛ" and val < 0:
                return -np.inf
            if name == "H0" and val <= 0:
                return -np.inf

            # Gaussian prior
            lp = -0.5 * ((val - mu) / sigma) ** 2
            if not np.isfinite(lp):
                return -np.inf

        return lp

    # ------------------------------------------------------------
    # POSTERIOR
    # ------------------------------------------------------------
    def _log_posterior(self, theta):
        """
        Combined prior + likelihood with NaN protection.
        """
        lp = self._log_prior(theta)
        if not np.isfinite(lp):
            return -np.inf

        # Build model safely
        try:
            from .symbolic_cosmology import SymbolicCosmology
            model = SymbolicCosmology(self.H_expr, dict(zip(self.param_names, theta)))
        except Exception:
            return -np.inf

        # Evaluate likelihood
        try:
            ll = self.joint_likelihood.log_likelihood(model)
        except Exception:
            return -np.inf

        if not np.isfinite(ll):
            return -np.inf

        return lp + ll

    # ------------------------------------------------------------
    # MCMC
    # ------------------------------------------------------------
    def run(self, theta0, nsteps=5000):
        """
        Stable Metropolis–Hastings sampler.
        """
        theta0 = np.asarray(theta0, dtype=float)
        ndim = len(theta0)

        chain = np.zeros((nsteps, ndim))
        chain[0] = theta0

        logp = self._log_posterior(theta0)
        if not np.isfinite(logp):
            raise RuntimeError("Initial theta0 has invalid posterior.")

        for i in range(1, nsteps):
            # Propose new parameters
            proposal = chain[i - 1] + np.array([
                np.random.normal(0, self.proposal_widths[name])
                for name in self.param_names
            ])

            logp_new = self._log_posterior(proposal)

            # Compute acceptance probability safely
            delta = logp_new - logp

            if delta >= 0:
                accept = True
            else:
                # Prevent overflow in exp(delta)
                if delta < -700:
                    accept = False
                else:
                    accept = np.random.rand() < np.exp(delta)

            if accept:
                chain[i] = proposal
                logp = logp_new
            else:
                chain[i] = chain[i - 1]

        return chain
