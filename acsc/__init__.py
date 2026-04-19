#!/bin/bash

"""
ACSC: Arithmetic–Cosmic Structure Conjecture computational framework.

A reproducible pipeline for testing the correspondence between topological features
of elliptic-curve arithmetic clouds and cosmic structure.
"""

__version__ = "0.1.0"
__author__ = "Patrick J. McNamara"

# Core exports for convenient access
from .projection import project, primary_projection, projection_ptd, projection_mcj
from .quantile import QuantileAligner
from .tda_pipeline import compute_persistence, persistence_wasserstein
from .statistics import w2_between_diagrams, empirical_p_value, effect_size

__all__ = [
    "project",
    "primary_projection",
    "projection_ptd",
    "projection_mcj",
    "QuantileAligner",
    "compute_persistence",
    "persistence_wasserstein",
    "w2_between_diagrams",
    "empirical_p_value",
    "effect_size",
]


