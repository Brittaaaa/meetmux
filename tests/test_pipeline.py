from meetmux.pipeline import MeetMuxPipeline, TaskResult


def test_pipeline_summarizes_results():
    pipeline = MeetMuxPipeline()
    pipeline.add_result(TaskResult(task_id=11, status="PASS", summary="Implemented"))
    pipeline.add_result(TaskResult(task_id=12, status="PASS", summary="Parsed skills"))

    summary = pipeline.summarize()

    assert "Task 11" in summary
    assert "Task 12" in summary
    assert "Implemented" in summary
