from meetmux.task12 import ResumeParser


def test_resume_parser_extracts_structured_skills():
    parser = ResumeParser()
    profile = parser.parse("Experienced Python developer with SQL and machine learning skills")

    assert [skill.skill for skill in profile.skills] == ["python", "sql", "machine learning"]
    assert profile.skills[0].confidence >= 0.8
