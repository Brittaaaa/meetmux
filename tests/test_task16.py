from meetmux.task16 import RecommendationEngineV1


def test_recommendation_engine_v1_ranks_candidates():
    engine = RecommendationEngineV1()
    recommendations = engine.design([
        {"candidate_id": "c1", "match_score": 0.6, "strength": "python"},
        {"candidate_id": "c2", "match_score": 0.9, "strength": "sql"},
    ])

    assert recommendations[0].candidate_id == "c2"
    assert recommendations[0].score >= recommendations[1].score
    assert len(recommendations[1].reasons) == 2
