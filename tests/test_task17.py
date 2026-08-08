from meetmux.task17 import RecommendationEngine


def test_recommendation_engine_produces_ranked_results():
    engine = RecommendationEngine()
    results = engine.recommend([
        {"candidate_id": "a", "match_score": 0.6, "role": "data analyst", "strength": "sql"},
        {"candidate_id": "b", "match_score": 0.9, "role": "data scientist", "strength": "python"},
    ])

    assert results[0].candidate_id == "b"
    assert results[0].score >= results[1].score
    assert "data scientist" in results[0].explanation
