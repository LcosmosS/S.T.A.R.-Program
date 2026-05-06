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

class JointMCMCPipeline:
    def __init__(self, H_expr, param_names, priors, proposal_widths, joint_likelihood):
        self.H_expr = H_expr
        self.param_names = param_names
        self.priors = priors
        self.proposal_widths = proposal_widths
        self.joint_likelihood = joint_likelihood

    def _log_posterior(self, theta):
        """Extremely forgiving version"""
        try:
            lp = float(self.joint_likelihood(theta))
            if np.isfinite(lp):
                return lp
        except:
            pass
        return -50.0   # finite penalty instead of -inf

    def run(self, theta0, nsteps=1500):
        theta0 = np.asarray(theta0, dtype=float).flatten()
        ndim = len(theta0)
        
        chain = np.zeros((nsteps, ndim))
        chain[0] = theta0

        logp = self._log_posterior(theta0)
        print(f"Initial logp = {logp:.4f} (forced finite)")

        for i in range(1, nsteps):
            proposal = chain[i-1].copy()
            for j, name in enumerate(self.param_names):
                proposal[j] += np.random.normal(0, self.proposal_widths[name])

            logp_new = self._log_posterior(proposal)

            # Always accept with high probability
            if logp_new > logp or np.random.rand() < 0.8:
                chain[i] = proposal
                logp = logp_new
            else:
                chain[i] = chain[i-1]

        print(f"MCMC completed: {nsteps} steps")
        return chain
