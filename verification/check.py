"""Independent square-lookup check, OpenAI Codex, 2026-11-13."""
from math import isqrt
L = 100000
squares = {x*x: x for x in range(1, isqrt(L)+1)}
def pairs(n):
    return [(x, squares[n-x*x]) for x in range(1, isqrt(n)+1)
            if n-x*x in squares and x <= squares[n-x*x]]
def D(n):
    return sum(x < y for x,y in pairs(n))
def R(n):
    return sum(1 if x == y else 2 for x,y in pairs(n))
for m in range(1, isqrt(L//2)+1):
    assert D(2*m*m) == D(m*m)
    assert R(2*m*m) == 2*D(m*m)+1
first_r, first_d = {}, {}
for n in range(L+1):
    first_r.setdefault(R(n), n)
    first_d.setdefault(D(n), n)
for k, n in first_d.items():
    if k and 2*k in first_r:
        assert first_r[2*k] == n
print('square lookup range:', L)
print('bijection identity: PASS for m <=', isqrt(L//2))
print('even minima compared:', sorted(k for k in first_d if k and 2*k in first_r))
print('PASS')
