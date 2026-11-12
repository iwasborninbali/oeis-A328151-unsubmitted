from math import isqrt
from functools import lru_cache

LIMIT = 1_000_000
R = [0] * (LIMIT + 1)
D = [0] * (LIMIT + 1)

# Direct enumeration of positive square pairs.
for x in range(1, isqrt(LIMIT) + 1):
    for y in range(x, isqrt(LIMIT - x*x) + 1):
        N = x*x + y*y
        if x == y:
            R[N] += 1
        else:
            R[N] += 2
            D[N] += 1

# Independent enumeration of Pythagorean triangles.
M = isqrt(LIMIT // 2)
T = [0] * (M + 1)

for m in range(1, M + 1):
    mm = m*m
    for a in range(1, m):
        b = isqrt(mm - a*a)
        if a < b and a*a + b*b == mm:
            T[m] += 1

assert all(
    R[2*m*m] == 2*T[m] + 1
    and D[m*m] == D[2*m*m] == T[m]
    for m in range(1, M + 1)
)

def isprime(n):
    return n >= 2 and all(
        n % d for d in range(2, isqrt(n)+1)
    )

primes = [
    p for p in range(5, 150)
    if p % 4 == 1 and isprime(p)
]

# Minimize products over multiplicative partitions.
@lru_cache(None)
def F(t):
    best = None

    def search(rem, upper, j, value):
        nonlocal best
        if rem == 1:
            if best is None or value < best:
                best = value
            return
        for f in range(2, min(rem, upper)+1):
            if rem % f == 0:
                v = value * primes[j]**(f-1)
                if best is None or v < best:
                    search(rem//f, f, j+1, v)

    search(t, t, 0, 1)
    return best

def predicted(n):
    if n == 0:
        return 0
    return 2*F(n) if n % 2 else min(F(n), F(n+1))

def first_indices(C):
    found = {}
    for n, c in enumerate(C):
        if c not in found:
            found[c] = n
    return found

minR = first_indices(R)
minD = first_indices(D)

verified_n = [
    n for n in range(101)
    if predicted(n) <= LIMIT
]
assert all(minR[n] == predicted(n) for n in verified_n)

verified_k = [
    k for k in range(1, 51)
    if min(F(2*k), F(2*k+1)) <= LIMIT
]
assert all(
    minD[k] == min(F(2*k), F(2*k+1))
    for k in verified_k
)

first15 = [predicted(n) for n in range(15)]

print(f"Direct search: 0 <= N <= {LIMIT:,}")
print(f"Bijection checks: 1 <= m <= {M}")
print(f"A328151 minima checked: {len(verified_n)} indices n = {verified_n}")
print(f"A093195 minima checked: {len(verified_k)} indices k = {verified_k}")
print(f"A328151(0..14) = {first15}")
