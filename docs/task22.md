# Task 22 — Drift Monitoring and Retraining

## Objective
Stand up drift monitoring and define a retraining trigger.

## Implementation
Implemented `DriftMonitor`, which compares baseline and current metric scores to detect drift and recommend retraining.

## Files Created/Modified
- `src/meetmux/task22.py`
- `tests/test_task22.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task22.py
```

## Testing
Verified with pytest.

## Results
The monitor detects drift when the deviation exceeds the configured threshold.

## Written Answer
Drift monitoring is implemented as a simple deviation-based trigger suitable for a v1 MLOps foundation.

## Verification Status
PASS
