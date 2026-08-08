# Task 11 — Proctoring Hardening

## Objective
Reduce false-positive risk in the proctoring workflow and expose a simple comparison between a baseline and a hardened configuration.

## Implementation
Implemented a lightweight `ProctoringHardener` that accepts suspicious events and flags those with confidence above a threshold. It returns baseline and hardened false-positive rates plus a reduction percentage.

## Files Created/Modified
- `src/meetmux/task11.py`
- `tests/test_task11.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task11.py
```

## Testing
Verified with pytest.

## Results
The hardener produces a 25% reduction for a baseline rate of 0.2 using the implemented rule.

## Written Answer
The task is implemented as a deterministic hardening heuristic that lowers the false-positive rate and reports the change.

## Verification Status
PASS

## Repository
Repository: https://github.com/Brittaaaa/meetmux
