from meetmux.task14 import OntologyBuilder


def test_ontology_builder_ingests_skills():
    builder = OntologyBuilder()
    nodes = builder.ingest_skills(["python", "sql"])

    assert [node.name for node in nodes] == ["python", "sql"]
    assert all(node.type == "skill" for node in nodes)
