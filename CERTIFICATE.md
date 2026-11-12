# Verification certificate

## Claim

For k>=1, A328151(2k)=A093195(k).

For k>=0, A328151(2k+1)=2 A006339(k)².

For m>=1, D(2m²)=D(m²), with D counting unordered distinct positive square representations.

## Evidence

| What | Program | Author and date | Coverage | Result |
|---|---|---|---|---|
| Human-checkable proof | `proof.md` | Adapted by OpenAI Codex from ChatGPT, 2026-11-12 | Universal identities | Not machine-checked |
| Producer | `programs/producer.py` | ChatGPT, 2026-11-12 | N<=1,000,000; m<=707; specified minima | Passed |
| Independent check | `verification/check.py` | OpenAI Codex, 2026-11-13 | N<=100,000; m<=223 and even minima found | Passed |

The checker shares no code or precomputed tables with the producer; both count the same mathematical objects. The guide's review is recorded in `athanor-oeis/tasks/README.md`.

## Replayed for this repository

2026-11-13, Darwin arm64, Python 3.14.6: `python3 programs/producer.py` reported 19 A328151 minima checked; `python3 verification/check.py` reported the identity passed for m<=223 and even minima k=[1,2,3,4,5,6,8,9]. Complete output is in `verification/logs/`.

## Not covered

The universal proof is not machine-checked. The independent program does not cover the producer's full bound or independently check odd minima. The standard sum-of-two-squares theorem is used in the proof of existence. The guide's 4,000,000-bound computation was not replayed.

## Guide's independent check

pending

## Verdict

partial — the separate finite check covers a smaller bound and does not check odd minima; the all-index proof is not formally machine-checked.
