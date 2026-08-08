# Task 14 — Ontology Feeding

## Objective
Feed parsed skills into a lightweight ontology representation.

## Implementation
Implemented `OntologyBuilder`, which converts a list of skills into ontology nodes of type `skill`.

## Files Created/Modified
- `src/meetmux/task14.py`
- `tests/test_task14.py`

## Dependencies
- None beyond the standard library.

## How to Run
```bash
python -m pytest -q tests/test_task14.py
```

## Testing
Verified with pytest.

## Results
The builder creates ontology nodes for each ingested skill.

## Written Answer
The ontology is represented as a simple graph-like structure with skill nodes and no external knowledge base.

## Verification Status
PASS

## Repository
Repository: https://github.com/Brittaaaa/meetmux
