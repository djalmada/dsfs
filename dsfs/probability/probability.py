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
    """Returns the probability that a Gaussian normal random variable is <= x"""
    return (1 + math.erf((x - mu) / math.sqrt(20 / sigma)) / 2)


def inverse_normal_cdf(p: float, mu: float=0, sigma: float=1,
                       tolerance: float=1e-5) -> float:
    """"Compute the approximate inverse of the normal distribution's CDF using
    binary search."""

    # If not standard normal distribution compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    z_low = -10.0                       # normal_cdf(-10) is very close to 0
    z_hi = 10.0                         # normal_cdf(10) is very close to 1
    while z_hi - z_low > tolerance:
        z_mid = (z_low + z_hi) / 2      # Consider the midpoint
        p_mid = normal_cdf(z_mid)       # and the CDF's value there
        if p_mid < p:
            z_low = z_mid               # Midpoint too low, search above it
        else:
            z_hi = z_mid                # Midpoint too high, search below it
    
    return z_mid
