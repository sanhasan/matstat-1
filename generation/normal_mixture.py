import numpy as np


def sample_mixture(rng, size, eps, mu, sigma, tau):
    is_outlier = rng.random(size) < eps
    scale = np.where(is_outlier, tau, sigma)
    return mu + scale * rng.standard_normal(size)
