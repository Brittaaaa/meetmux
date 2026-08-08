# Task 19 — Weak-Item Flagging

## Objective
Support item-bank quality review by flagging weak items for admins.

## Implementation
Implemented `WeakItemFlagger`, which marks items below a configurable quality threshold as flagged.

## Files Created/Modified
- `src/meetmux/task19.py`
- `tests/test_task19.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task19.py
```

## Testing
Verified with pytest.

## Results
The flager identifies low-quality items and associates them with a reason.

## Written Answer
The task is implemented as a simple admin-facing quality screen for item-bank review.

## Verification Status
PASS
