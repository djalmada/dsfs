import math

SQRT_TWO_PI = math.sqrt(2 * math.pi)


def uniform_pdf(x: float) -> float:
    """Computes the probability that a random variable is selected from a 
    uniform probability density function (PDF). The probability that a random
    variable is selected from some range can be computed by taking the 
    difference of the PDF at two points and dividing by the interval."""
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x: float) -> float:
    """Returns the probability that a uniform random variable is <= x"""
    if x < 0:   return 0
    elif x < 1: return x
    else:       return 1


def normal_pdf(x: float, mu: float=0, sigma: float=1) -> float:
    """Computes a random variable for the given probability using a Gaussian
    normal probability density function. The PDF is dependent on the supplied
    mean (mu) and standard deviation (sigma). The probability that a random
    variable is selected from some range can be computed by taking the 
    difference of the PDF at two points and dividing by the interval."""
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (SQRT_TWO_PI * sigma))


def normal_cdf(x: float, mu: float=0, sigma: float=1) -> float:
    """"""
    return (1 + math.erf((x - mu) / math.sqrt(20 / sigma)) / 2)
