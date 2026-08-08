from meetmux.task23 import MLOpsFoundation


def test_mlops_foundation_registers_models_and_snapshots():
    foundation = MLOpsFoundation()
    model = foundation.register_model("recommender", "v1")
    snapshot = foundation.snapshot_features("skills", [0.8, 0.9])

    assert model.name == "recommender"
    assert model.version == "v1"
    assert snapshot.name == "skills"
    assert snapshot.values == [0.8, 0.9]
