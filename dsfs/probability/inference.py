from probability import (
    normal_cdf,
    inverse_normal_cdf,
)
from typing import Tuple
import math


def normal_approximation_to_binomial(n: int, p: float) -> Tuple[float, float]:
    """"""
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)

    return mu, sigma


def normal_probability_above(lo: float, mu: float=0, sigma: float = 1) -> float:
    """"""
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo: float, hi: float, mu: float=0, sigma: float=1) -> float:
    """"""
    return 1 - normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo: float, hi: float, mu: float=0, sigma: float=1) -> float:
    """"""
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability: float, mu: float=0, sigma: float=1) -> float:
    """"""
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability: float, mu: float=0, sigma: float=1) -> float:
    """"""
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability: float, mu: float=0, sigma: float=1) -> Tuple[float, float]:
    """"""
    tail_probability = (1 - probability) / 2

    # Upper bound should have tail probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)

    # Lower bound should have tail probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound
