from app.rag_engine import RAGEngine


def test_retrieve_context():
    engine = RAGEngine()
    context = engine.retrieve_context("opposition endgame")
    assert "opposition" in context.lower()
