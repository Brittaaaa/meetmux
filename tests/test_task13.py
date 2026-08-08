from meetmux.task13 import FalsePositiveReducer


def test_false_positive_reducer_reports_improvement():
    reducer = FalsePositiveReducer(baseline_rate=0.2)
    metrics = reducer.compare([
        {"event_id": "a", "confidence": 0.8},
        {"event_id": "b", "confidence": 0.5},
        {"event_id": "c", "confidence": 0.7},
    ])

    assert metrics["baseline_rate"] == 0.2
    assert metrics["reduced_rate"] == 0.16
    assert metrics["flagged_events"] == 2
    assert metrics["improvement"] == 20.0
