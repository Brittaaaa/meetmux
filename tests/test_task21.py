from meetmux.task21 import FairnessAudit


def test_fairness_audit_reports_group_rates():
    audit = FairnessAudit()
    report = audit.audit([
        {"group": "group_a", "accepted": True},
        {"group": "group_a", "accepted": False},
        {"group": "group_b", "accepted": True},
    ])

    assert report["audit_started"] is True
    assert report["group_rates"]["group_a"] == 0.5
    assert report["group_rates"]["group_b"] == 1.0
