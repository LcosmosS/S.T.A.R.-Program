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
    def __init__(self, H_expr, param_names, priors, proposal_widths, joint_likelihood):
        self.H_expr = H_expr
        self.param_names = param_names
        self.priors = priors
        self.proposal_widths = proposal_widths
        self.joint_likelihood = joint_likelihood

    def _log_prior(self, theta):
        lp = 0
        for val, name in zip(theta, self.param_names):
            mu, sigma = self.priors[name]
            lp += -0.5 * ((val - mu) / sigma)**2
        return lp

    def _log_posterior(self, theta):
        params = dict(zip(self.param_names, theta))
        model = SymbolicCosmology(self.H_expr, params)
        return self._log_prior(theta) + self.joint_likelihood.log_likelihood(model)

    def run(self, theta0, nsteps=10000):
        chain = np.zeros((nsteps, len(theta0)))
        chain[0] = theta0
        logp = self._log_posterior(theta0)

        for i in range(1, nsteps):
            proposal = chain[i-1] + np.array([
                np.random.normal(0, self.proposal_widths[name])
                for name in self.param_names
            ])

            logp_new = self._log_posterior(proposal)
            accept = np.random.rand() < np.exp(logp_new - logp)

            if accept:
                chain[i] = proposal
                logp = logp_new
            else:
                chain[i] = chain[i-1]

        return chain
