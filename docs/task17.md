# Task 17 — Recommendation v1 Live

## Objective
Ship the recommendation v1 workflow so it produces ranked results from candidate profiles.

## Implementation
Implemented `RecommendationEngine`, which takes candidate profile dictionaries and returns sorted recommendations with explanations.

## Files Created/Modified
- `src/meetmux/task17.py`
- `tests/test_task17.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task17.py
```

## Testing
Verified with pytest.

## Results
The engine returns ranked recommendations with explanation text.

## Written Answer
The recommendation logic is a simple scoring heuristic suitable for a v1 implementation.

## Verification Status
PASS
