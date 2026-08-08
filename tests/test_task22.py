from meetmux.task22 import DriftMonitor


def test_drift_monitor_detects_retraining_need():
    monitor = DriftMonitor(threshold=0.15)
    report = monitor.monitor(
        [{"score": 0.8}, {"score": 0.75}],
        [{"score": 0.5}, {"score": 0.6}],
    )

    assert report["drift_detected"] is True
    assert report["summary"] == "Retraining recommended"
