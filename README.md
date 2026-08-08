# MeetMux

MeetMux is a lightweight, testable Python implementation of the Phase 2 AI/ML workstreams. It provides deterministic reference components for proctoring hardening, resume/JD parsing, skill ontology ingestion, recommendation and explanation, item-quality review, validation, fairness, drift, MLOps records, and production monitoring.

## Phase 2 scope

Tasks 11–25 are implemented and verified. The original task briefs are retained in `task_pdfs/`; task-by-task implementation notes are in `docs/task11.md` through `docs/task25.md`.

## Project structure

- `src/meetmux/` — reusable Task 11–25 modules.
- `tests/` — unit tests for each task plus pipeline coverage.
- `task_pdfs/` — source task briefs.
- `docs/` — task requirements, per-task notes, and audit material.
- `WRITTEN_ANSWERS.md` — reviewer-oriented answers and task commit links.
- `TASK_TRACKER.md` — task status and verification record.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the tests

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests
```

The latest verification run completed with **16 passed** tests.

## Dependencies

- `pytest` for automated verification.
- `pypdf` for reviewing the supplied PDF briefs.

## Repository

https://github.com/Brittaaaa/meetmux
