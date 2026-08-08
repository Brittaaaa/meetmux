from meetmux.task11 import ProctoringHardener


def test_proctoring_hardener_reduces_false_positive_rate():
    hardener = ProctoringHardener(baseline_rate=0.2)
    result = hardener.harden([
        {"event_id": "e1", "confidence": 0.8},
        {"event_id": "e2", "confidence": 0.6},
        {"event_id": "e3", "confidence": 0.9},
    ])

    assert result.baseline_false_positive_rate == 0.2
    assert result.hardened_false_positive_rate == 0.15
    assert result.reduction_percent == 25.0
    assert result.flags == ["e1", "e3"]
