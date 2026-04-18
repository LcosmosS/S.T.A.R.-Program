"""
acsc.null_models
Generators for null point clouds and utilities to build reference distributions.
"""

import numpy as np
from typing import Callable, Iterable, List, Dict
from acsc.projection import project

def null_random_spatial(n_points: int, bbox: np.ndarray) -> np.ndarray:
    """
    Uniform random sample in axis-aligned bounding box.
    bbox: array-like shape (2, d) with min and max per dimension.
    """
    bbox = np.asarray(bbox, dtype=float)
    mins = bbox[0]
    maxs = bbox[1]
    return np.random.uniform(mins, maxs, size=(n_points, mins.size))

def null_permuted_invariant(records: Iterable[Dict], invariant_key: str, method: str = "primary") -> np.ndarray:
    """
    Permute a single invariant across records, then project.
    Returns projected coordinates.
    """
    recs = list(records)
    vals = [r.get(invariant_key) for r in recs]
    perm = np.random.permutation(vals)
    recs_perm = []
    for r, v in zip(recs, perm):
        r2 = dict(r)
        r2[invariant_key] = v
        recs_perm.append(r2)
    return project(recs_perm, method=method)

def build_null_distribution(metric_fn: Callable[[np.ndarray], float],
                            generator_fn: Callable[[], np.ndarray],
                            repeats: int = 200) -> List[float]:
    """
    Repeatedly generate null point clouds, compute metric_fn on each, and return list of values.
    metric_fn receives projected coords and returns a scalar (e.g., W2 to cosmic).
    generator_fn is a zero-argument callable that returns projected coords for a null sample.
    """
    vals = []
    for _ in range(repeats):
        coords = generator_fn()
        vals.append(float(metric_fn(coords)))
    return vals
