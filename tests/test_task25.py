from meetmux.task25 import ProductionMonitor


def test_production_monitor_emits_alert_for_low_score():
    monitor = ProductionMonitor(alert_threshold=0.2)
    report = monitor.monitor([{"score": 0.15}])

    assert report["alert"] is True
    assert report["status"] == "alert"
