from meetmux.task18 import ExplainabilityLayer


def test_explainability_layer_richens_recommendations():
    layer = ExplainabilityLayer()
    result = layer.explain([{"skill": "python", "evidence": "resume match"}])[0]

    assert "python" in result["explanation"]
    assert "resume match" in result["explanation"]
