# OEIS A328151: Schoenfield's parity identities (not yet submitted)

<!-- oeis-status:begin -->
**OEIS status: not submitted** (lab registry, 13 Nov 2026).

- [A328151](https://oeis.org/A328151), Schoenfield's identities proved (D(2m^2) = D(m^2)): **candidate** (2026-11-13: repository built (core c5)). Certificate: partial.

Rules and the full registry: [athanor-oeis](https://github.com/iwasborninbali/athanor-oeis/blob/main/REGISTRY.md).
<!-- oeis-status:end -->

## Definition

For n>=0, a(n) is the least nonnegative N having exactly n ordered pairs (x,y) of positive integers with x²+y²=N; the offset is 0 and a(0)=0. A093195(k) is the least positive integer expressible as a sum of two distinct positive squares in exactly k unordered ways. A006339(k) is the least positive hypotenuse of exactly k integer right triangles, counting interchanged legs once.

The task's `context/A328151.seq` and the live [entry](https://oeis.org/A328151), read 2026-11-13, state Jon E. Schoenfield's January 23, 2022 conjecture: “Conjecture: a(2k) = A093195(k) for k >= 1, a(2k+1) = 2*A006339(k)^2 for k >= 0.” The entry still calls it a conjecture.

## Terms / result

Both displayed identities hold in their stated domains. Key to the proof is D(2m²)=D(m²), where D counts unordered distinct positive square representations.

| n | a(n) |
|---:|---:|
| 0 | 0 |
| 1 | 2 |
| 2 | 5 |
| 3 | 50 |
| 4 | 65 |
| 5 | 1250 |
| 6 | 325 |

## How it was obtained

An explicit invertible map between right triangles and distinct representations of twice a square proves the key equality. It also eliminates diagonal cases from the even minimization. See [proof.md](proof.md).

## Verification

The source program was replayed to N=1,000,000; a separately written square-lookup program checks the key identity and minima through N=100,000. The proof is human-checkable, not formally machine-checked. See [CERTIFICATE.md](CERTIFICATE.md).

## Prior art and credit

Schoenfield stated the conjecture; Chai Wah Wu had recorded the parity observation. ChatGPT supplied the proof and Claude Code reviewed it. See [PRIOR-ART.md](PRIOR-ART.md).

## Reproduce

Run `python3 programs/producer.py` and `python3 verification/check.py` (about four seconds together on the recorded machine). The former reports 19 checked A328151 indices and 707 bijection checks; the latter ends `PASS`. Full outputs are in `verification/logs/`.

## Provenance

Source `projects/science/athanor-oeis`, commit `7662d9a678c6d414685a899a631c63ac320f6840`, paths `tasks/2026-11-12-A328151-parity-formula/answers/2026-11-12-chatgpt.md`, `context/A328151.seq`, and `TASK.md`. The guide's review is recorded in `tasks/README.md`.

## Author, licence

Aleksei Kudriashov (ORCID 0009-0006-8885-5338), Athanor lab, with AI assistance (OpenAI Codex cores; Claude Code as the lab's guide). Code: MIT; data and text: CC BY 4.0 (see LICENSE.md).
