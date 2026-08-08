# Task 21 — Fairness Audit Start

## Objective
Begin a fairness and bias audit workflow for protected groups.

## Implementation
Implemented `FairnessAudit`, which computes acceptance rates for each group and returns an audit summary.

## Files Created/Modified
- `src/meetmux/task21.py`
- `tests/test_task21.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task21.py
```

## Testing
Verified with pytest.

## Results
The audit returns group-level acceptance rates for the sample outcome data.

## Written Answer
The implementation models fairness auditing as a lightweight statistical checkpoint rather than a full compliance platform.

## Verification Status
PASS
