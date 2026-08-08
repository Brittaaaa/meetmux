from meetmux.task24 import FairnessReview


def test_fairness_review_signs_off_models():
    review = FairnessReview()
    report = review.review({"summary": "Fairness audit underway"})

    assert report["signed_off"] is True
    assert report["result"] == "Models signed off"
    assert "recommender" in report["models"]
