# Task 12 — Resume/JD Parsing v0

## Objective
Create a simple parsing pipeline that converts resume or job description text into structured skills.

## Implementation
Implemented `ResumeParser`, which tokenizes text, detects known keywords, and returns a list of structured skill objects with associated confidence scores.

## Files Created/Modified
- `src/meetmux/task12.py`
- `tests/test_task12.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task12.py
```

## Testing
Verified with pytest.

## Results
The parser extracts keywords such as Python, SQL, and machine learning as structured skills.

## Written Answer
The parsing module operates as a rule-based extractor that produces structured skills from unstructured text.

## Verification Status
PASS
