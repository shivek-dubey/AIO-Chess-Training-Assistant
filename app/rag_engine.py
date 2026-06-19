from app.vector_store import SimpleTextStore


class RAGEngine:
    def __init__(self):
        self.store = SimpleTextStore(data_dir="data")

    def retrieve_context(self, question: str) -> str:
        results = self.store.search(question, top_k=3)
        if not results:
            return "No directly matching chess notes were found in the local knowledge base."

        chunks = []
        for path, text in results:
            chunks.append(f"Source: {path}\n{text}")
        return "\n\n---\n\n".join(chunks)
