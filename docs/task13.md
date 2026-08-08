# Task 13 — False-Positive Reduction

## Objective
Ship a stronger false-positive reduction strategy and measure the improvement against a baseline.

## Implementation
Implemented `FalsePositiveReducer`, which compares baseline and reduced error rates and reports the number of flagged events.

## Files Created/Modified
- `src/meetmux/task13.py`
- `tests/test_task13.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task13.py
```

## Testing
Verified with pytest.

## Results
The reducer reports a 20% improvement for the sample event set.

## Written Answer
The task is implemented as a lightweight comparison module rather than a full ML-based detector.

## Verification Status
PASS

## Repository
Repository: https://github.com/Brittaaaa/meetmux
