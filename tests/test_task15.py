from meetmux.task15 import TrustLayer


def test_trust_layer_signs_off_when_required_checks_present():
    layer = TrustLayer()
    report = layer.summarize(["proctoring", "parsing", "ontology"])

    assert report["signed_off"] is True
    assert report["summary"] == "AI trust features signed off"
