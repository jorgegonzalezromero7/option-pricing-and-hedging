import numpy as np
from scipy.stats import norm


def calculate_greeks(S, K, T, r, sigma, option_type="call"):

    d1 = (
        np.log(S / K)
        + (r + 0.5 * sigma ** 2) * T
    ) / (sigma * np.sqrt(T))

    d2 = d1 - sigma * np.sqrt(T)

    # Delta
    if option_type == "call":
        delta = norm.cdf(d1)
    else:
        delta = norm.cdf(d1) - 1

    # Gamma
    gamma = norm.pdf(d1) / (
        S * sigma * np.sqrt(T)
    )

    # Vega
    vega = (
        S
        * norm.pdf(d1)
        * np.sqrt(T)
    )

    # Theta
    if option_type == "call":
        theta = (
            -S * norm.pdf(d1) * sigma /
            (2 * np.sqrt(T))
            - r * K * np.exp(-r * T)
            * norm.cdf(d2)
        )
    else:
        theta = (
            -S * norm.pdf(d1) * sigma /
            (2 * np.sqrt(T))
            + r * K * np.exp(-r * T)
            * norm.cdf(-d2)
        )

    # Rho
    if option_type == "call":
        rho = (
            K * T * np.exp(-r * T)
            * norm.cdf(d2)
        )
    else:
        rho = (
            -K * T * np.exp(-r * T)
            * norm.cdf(-d2)
        )

    return {
        "Delta": delta,
        "Gamma": gamma,
        "Vega": vega,
        "Theta": theta,
        "Rho": rho
    }