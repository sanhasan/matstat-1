import numpy as np
from numpy.typing import NDArray


def sample_exponential(
    rng: np.random.Generator, iters: int, sample_size: int
) -> NDArray[np.float64]:
    return rng.exponential(scale=1.0, size=(iters, sample_size))


def less_F(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """-(e^{-x} - 1)"""
    return -np.expm1(-x)


def greather_F(x: NDArray[np.float64]) -> NDArray[np.float64]:
    """e^{-x}"""
    return np.exp(-x)
