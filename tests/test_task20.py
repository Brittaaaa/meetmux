from meetmux.task20 import RecommendationValidator


def test_recommendation_validator_returns_validation_metrics():
    validator = RecommendationValidator()
    report = validator.validate([
        {"score": 0.8},
        {"score": 0.9},
    ])

    assert report["validated"] is True
    assert report["metrics"]["precision"] == 0.85
    assert report["metrics"]["coverage"] == 0.4
