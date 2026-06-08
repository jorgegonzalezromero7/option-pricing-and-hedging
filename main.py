from pricing.greeks import calculate_greeks
from pricing.black_scholes import black_scholes_price


S = 100
K = 100
T = 1
r = 0.05
sigma = 0.2

call = black_scholes_price(
    S,
    K,
    T,
    r,
    sigma,
    "call"
)

put = black_scholes_price(
    S,
    K,
    T,
    r,
    sigma,
    "put"
)

print(f"Call price: {call:.2f}")
print(f"Put price: {put:.2f}")

greeks = calculate_greeks(
    S,
    K,
    T,
    r,
    sigma,
    "call"
)

print("\nCall Greeks:")

for greek, value in greeks.items():
    print(f"{greek}: {value:.4f}")