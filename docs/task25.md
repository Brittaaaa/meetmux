# Task 25 — Production Monitoring

## Objective
Monitor model performance in production and trigger alerts when metrics fall below a threshold.

## Implementation
Implemented `ProductionMonitor`, which accepts a series of metric records and reports whether production performance is healthy or alerting.

## Files Created/Modified
- `src/meetmux/task25.py`
- `tests/test_task25.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task25.py
```

## Testing
Verified with pytest.

## Results
The monitor emits an alert when the latest score falls below the configured threshold.

## Written Answer
Production monitoring is implemented as a simple alerting mechanism that can be extended into a real observability stack.

## Verification Status
PASS

## Repository
Repository: https://github.com/Brittaaaa/meetmux
