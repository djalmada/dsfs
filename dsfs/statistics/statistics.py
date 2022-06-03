from collections import Counter
from dsfs.linalg import (
    Vector,
    dot,
)
from typing import (
    List,
)
import math


def mean(v: Vector) -> float:
    """Computes the average of a list of values"""
    return sum(v) / len(v)


def _median_odd(v: Vector) -> float:
    """Computes the median when the quantity of data is odd"""
    return sorted(v)[len(v) // 2]


def _median_even(v: Vector) -> float:
    """Computes the median when the quantity of data is odd"""
    sorted_v = sorted(v.data)
    hi_midpoint = len(v) // 2
    return (sorted_v[hi_midpoint - 1] + sorted_v[hi_midpoint]) / 2


def median(v: Vector) -> float:
    """Computes the median (middle value)"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


def quantile(v: Vector, p: float) -> float:
    """Returns the pth-percentile value in the input data"""
    p_index = int(p * len(v))
    return sorted(v)[p_index]


def mode(v: Vector) -> List[float]:
    """Returns a list of the most common value(s) in the input data"""
    counts = Counter(v)
    max_count = max(counts.values())
    return [v_i for v_i, count in counts.items() if count == max_count]


def data_range(v: Vector) -> float:
    """Returns the range of the input data"""
    return max(v) - min(v)


def standardize(v: Vector) -> Vector:
    """Computes the standard score such that the mean becomes zero"""
    v_bar = mean(v)
    return Vector([v_i - v_bar for v_i in v])


def variance(v: Vector) -> float:
    """Computes the average squared deviation from the mean"""
    assert len(v) >= 2, "Variance requires at least two data points"

    num_elements = len(v)
    standard_score = standardize(v)
    return standard_score.sum_of_squares() / (num_elements - 1)


def standard_deviation(v: Vector) -> float:
    """Computes the standard deviation as the square root of the variance"""
    return math.sqrt(variance(v))


def interquartile_range(v: Vector) -> float:
    """Returns the difference between the 75%-ile and the 25%-ile"""
    return quantile(v, 0.75) - quantile(v, 0.25)


def covariance(v: Vector, w: Vector) -> float:
    """Computes the variance between two variables and their means in tandem"""
    assert len(v) == len(w), "The inputs must have the same length"

    return dot(standardize(v), standardize(w)) / (len(v) - 1)


def correlation(v: Vector, w: List[float]) -> float:
    """Measures how much the input lists vary in tandem about their means"""
    stdev_v = standard_deviation(v)
    stdev_w = standard_deviation(w)
    if stdev_v > 0 and stdev_w > 0:
        return covariance(v, w) / stdev_v / stdev_w
    else:
        return 0


def chi_squared(v: Vector) -> float:
    """"""
    pass