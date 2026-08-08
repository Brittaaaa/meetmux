from meetmux.task19 import WeakItemFlagger


def test_weak_item_flagger_marks_low_quality_items():
    flagger = WeakItemFlagger(threshold=0.4)
    flagged = flagger.flag([
        {"item_id": "i1", "quality_score": 0.3},
        {"item_id": "i2", "quality_score": 0.8},
    ])

    assert flagged[0]["flagged"] is True
    assert flagged[1]["flagged"] is False
