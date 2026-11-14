# Independent verification, 2026-11-15

Target: `iwasborninbali/oeis-A328151-unsubmitted` at commit `6813c9128c15186a6e4dc6167d46f94c3ba69efe`. This review is independent of the authors of `CERTIFICATE.md`, `proof.md`, `programs/producer.py`, and `verification/check.py`. The archived files were unpacked and inspected, including the existing output logs. No existing repository files were changed.

## Claim

For every `k >= 1`, `A328151(2k) = A093195(k)`; for every `k >= 0`, `A328151(2k+1) = 2*A006339(k)^2`; and for every `m >= 1`, `D(2m^2) = D(m^2)`, where `D(N)` counts unordered distinct positive-square representations of `N`.

This is precisely the three-part mathematical claim in `CERTIFICATE.md` lines 5–9 (not an assertion that novelty has been established).

## Proof check

**Referee verdict on the mathematical proof: correct (minor expositional points, none fatal).** Line-by-line audit:

- **Lines 3–5:** Definitions are consistent with the OEIS entries. `R(N) = 2D(N) + [N=2m^2 for some integer m >= 1]` is correct: the unordered off-diagonal representations each produce two ordered ones and a diagonal representation exists precisely for `N=2m^2`. No gap.
- **Line 7:** The orbit-count explanation is correct; uniqueness of the diagonal pair is immediate from positivity of `m`. No gap.
- **Line 9, initial `D(m^2)=T(m)`:** Correct, but the phrase "by definition" tacitly requires explaining that integral right triangles cannot have equal positive legs (otherwise `2u^2=m^2`, contradicting the irrationality of `sqrt(2)`). **Fixable exposition; not fatal.**
- **Line 9, forward bijection:** `(u,v)->(x,y)=(u+v,u-v)` for `u>v>0` is valid, preserving positivity, distinctness, and `x^2+y^2=2m^2`. However, the proof originally defined `D` with `x<y` and now uses `x>y`; an explicit swap of coordinate labels is needed for exact adherence to the stated convention. **Fixable notational gap; not fatal.**
- **Line 9, inverse bijection:** From even `x^2+y^2`, `x` and `y` have the same parity (each square has the parity of its base). Hence `(x+y)/2`, `(x-y)/2` are positive integers and satisfy the required equation; the maps are mutually inverse. The parity justification is implicit but elementary and correct. **Optional one-sentence exposition improvement; not fatal.**
- **Line 9, final `R(2m^2)=2T(m)+1`:** Follows exactly from the diagonal correction and the bijection; correct.
- **Line 11, odd minima:** Odd `R(N)` forces `N=2m^2` and then `T(m)=k`; since `2m^2` strictly increases with positive `m`, the minimum is `2*A006339(k)^2`. Correct, contingent on existence established later.
- **Line 13, even minima:** If the smallest `B` with `D(B)=k` were `2m^2`, the smaller `m^2` would contradict minimality. Conversely, `R(N)=2k` implies no diagonal pair, so `D(N)=k` and `N>=B`. Correct, contingent on existence established later.
- **Line 15, existence:** The standard two-square formula `r_2(5^(2k))=4(2k+1)` is invoked but not proved or cited. This is a classical proved theorem, *not* an unproved conjecture. After excluding four zero-coordinate solutions and diagonal ones, the remainder has eight symmetries per unordered positive unequal pair; hence `D(5^(2k))=k`, `T(5^k)=k`. **A reference or elementary proof would make this self-contained, but this is not a fatal gap.** For `k=0`, `A006339(0)=1`, `a(1)=2`, and `a(0)=0` by definition. All cases covered.

**Wrong steps: none. Fatal gaps: none. Dependencies on unproved conjectures: none.** The proof is *not formally machine-checked*, which is a scope limitation rather than a mathematical counterexample.

## Independent computation

I wrote `independent.cpp` from scratch without importing, invoking, or copying the repository's code or tables. It deliberately uses different mathematical algorithms from both existing checks:

1. Compute `s(N)=sum_{d|N} chi_4(d)` for every `1<=N<=LIMIT` by a divisor-character sieve (`chi_4(d)=1` for `d=1 mod 4`, `-1` for `d=3 mod 4`, and zero for even `d`). Jacobi's two-square theorem gives `r_2(N)=4*s(N)`, whence `R(N)=s(N)-[N is a positive square]` and `D(N)=(R(N)-[N is twice a positive square])/2`. Directly tabulate *first-occurrence* minima, with index zero initialized to `N=0`.
2. Independently obtain `T(m)` by generating primitive Euclid triples `a^2-b^2, 2ab, a^2+b^2` for `a>b>0`, `gcd(a,b)=1`, opposite parity, then adding every positive multiple of each primitive hypotenuse. This method does not use the sum-of-squares representations counted in step 1.
3. For each `m`, check `D(m^2)=D(2m^2)=T(m)` and `R(2m^2)=2T(m)+1`. Compare actual minima for **both** even and odd indices (where both sides have appeared below the chosen bound). For odd indices compute the first hypotenuse with a given triangle count independently of `R`.

Build: `g++ -std=c++17 -O3 -Wall -Wextra -pedantic independent.cpp -o independent`.
Run: `./independent 200000000 > independent.log`.

**Observed output:** All `N` through `200,000,000` evaluated; all `m=1..10,000` checked; zero bijection, arithmetic, even-minimum, or odd-minimum mismatches; **27 even** `k` values, **11 odd** `k` values with both minima available. `PASS`. Wall time measured by the program `13.9991` seconds, external `/usr/bin/time`: `real 14.01`, `user 13.44`, `sys 0.56` seconds (this machine). Detailed exact tested `k` and values are preserved in the full output log. This is **2,000 times** the independent check's `N=100,000` bound, and **200 times** the producer's `N=1,000,000` bound; the repository's previous checker did not test odd minima.

SHA-256 (local contents, before GitHub upload):

- `independent.cpp`: `1af967ba721180871ff120ab37f73bd880b9ece25658dce42b237ac4ad58531a`
- `independent.log`: `8b1f99eff5ca791fdac4ef3f5a6e2030b9c88aa3312a0bfbf905b1e093b83acd`

These are finite experiments, not substitutes for the universal proof. Arithmetic sieve relies on the classical Jacobi identity; the Euclid-triples enumeration relies on the standard primitive-triple classification.

## Prior art

Search performed **2026-11-15**, with direct OEIS entry inspection and web searches of OEIS, linked entries, history route, arXiv, MathOverflow, Math Stack Exchange, zbMATH and journal sites (including Springer, ScienceDirect and JSTOR). Findings:

1. **[OEIS A328151](https://oeis.org/A328151)**: Jon E. Schoenfield's exact two parity formulas remain explicitly labeled **"Conjecture" (Jan. 23, 2022)**. Chai Wah Wu recorded the odd-index shape `2*m^2` on Jun. 28, 2024, not the full minimum formula. The page lists extensions through Aug. 16, 2026, but no proof link for the full identities. The [OEIS edit-history URL](https://oeis.org/history?seq=A328151) returned HTTP 403 in this environment, so individual edit diffs could **not** be audited.
2. **[OEIS A093195](https://oeis.org/A093195)** (Lekraj Beedassy, 2004) already gives `A093195(k)=min(A018782(2k), A018782(2k+1))` and Ant King's 2009/2010 algorithm for minima. **[A018782](https://oeis.org/A018782)** explicitly reciprocates this relationship. These predate the certificate but are not themselves the full A328151 parity theorem.
3. **[OEIS A006339](https://oeis.org/A006339)** gives the least hypotenuse for exactly `k` different Pythagorean triangles, including `A006339(0)=1`, with Albert H. Mao's January 2012 explicit construction. **[A054994](https://oeis.org/A054994)** (2004; Jan. 2022 cross-reference) already relates least hypotenuses to primes `1 mod 4`.
4. **[OEIS A063725](https://oeis.org/A063725)** gives `R(N)` and, in a formula attributed to Ridouane Oudra **Dec. 8, 2025**, states `R(2n)=R(n)+A143259(n)`; **[A143259](https://oeis.org/A143259)** is `1` on squares, `-1` on twice-squares and `0` otherwise. Substituting `n=m^2` gives `R(2m^2)=R(m^2)+1`, which, using the standard diagonal correction, **already implies the key equality** `D(2m^2)=D(m^2)`. Thus an equivalent counting identity is recorded in prior OEIS art; the key equality cannot safely be advertised as novel without a more exact historical analysis. A063725 also contains earlier two-square formulas attributed to Charles R. Greathouse IV (2016).
5. **[Math Stack Exchange, "Does a²+b²=2c² have any integer solution?" (May 20–24, 2020)](https://math.stackexchange.com/questions/3683854/does-a2-b2-2-c2-have-any-integer-solution)**: a May 24, 2020 comment by richrow explicitly exhibits the inverse map `((a+b)/2,(a-b)/2)` and the forward map `(u+v,u-v)` from Pythagorean triples; a May 21 answer by Adam Bailey also displays `(u-v)^2+(u+v)^2=2m^2`. This **predates the submitted bijection** by six years. It does not state Schoenfield's 2022 formulas (which were later).
6. **Journal precedent**: M. A. Nyblom, ["On the enumeration of Pythagorean triples having a fixed base length," *Gazette of the Australian Mathematical Society* 36(3) (2009), 204–207](https://citeseerx.ist.psu.edu/document?doi=739418a1cf07d0adec8ac5cbb8de58d85226c4ad&repid=rep1&type=pdf), provides the classical Jacobi-counting context and identifies `r_2(m^2)/4 - 1` as the *ordered* count of nonzero Pythagorean leg pairs. Not evidence of prior publication of the full A328151 formula. See also [J. A. Perez, arXiv:1102.4312 (2011)](https://arxiv.org/abs/1102.4312) for classical links between binary quadratic forms and Pythagorean triangles.
7. **MathOverflow**: [question 244491 on counting Pythagorean triples](https://mathoverflow.net/questions/244491/is-there-any-formula-to-find-number-of-pythagorean-triplets-between-two-integers/451748) addresses related representation counts, not the full exact A328151 parity statement. Searches for the OEIS identifiers and the identities on MathOverflow, arXiv, zbMATH, and indexed journal websites did **not** reveal a prior publication of *both complete* parity identities, but absence of a search hit does not establish novelty. In particular, access to the full OEIS edit history and comprehensive zbMATH/journal full text was incomplete.
8. **OEIS cross-references [A374159](https://oeis.org/A374159), [A374160](https://oeis.org/A374160), [A374161](https://oeis.org/A374161)** are analogues for other diagonal quadratic forms, not prior proofs of this identity; [A374160](https://oeis.org/A374160) was inspected. Some linked pages were intermittently blocked with HTTP 403.

**Originality assessment:** The original Schoenfield *conjecture* is prior art. The coordinate bijection and its central arithmetic consequence substantially predate the repository (2020 and 2025). No verified earlier source was found that explicitly establishes **both entire minimum identities** as a theorem. Consequently a claim that *the complete proof is historically new* is **not established**. Attribution should distinguish the conjecture, earlier elementary transformation, and the independent proof submitted here.

## Verdict

**PARTIAL on the combined truth-and-novelty assessment.** The mathematical claim is **true**: its proof is correct on referee inspection and all three claimed identities pass a substantially larger independent computation, including previously untested odd minima. **No counterexample or fatal proof gap exists.** However, the asserted *novelty* of the core map/counting identity is contradicted by explicit earlier public material, and novelty of the complete combination of the two formulas has **not** been established by an exhaustive priority search. Full OEIS edit-history access was unavailable; no formal machine proof was attempted or claimed.
