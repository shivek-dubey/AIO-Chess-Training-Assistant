from pathlib import Path
from typing import List, Tuple


class SimpleTextStore:
    """A lightweight keyword-based store for demo submission.

    This keeps the project simple and runnable without paid APIs.
    It can later be replaced with FAISS, ChromaDB, Azure AI Search, etc.
    """

    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.documents = self._load_documents()

    def _load_documents(self) -> List[Tuple[str, str]]:
        docs = []
        for file_path in self.data_dir.rglob("*.txt"):
            docs.append((str(file_path), file_path.read_text(encoding="utf-8")))
        for file_path in self.data_dir.rglob("*.pgn"):
            docs.append((str(file_path), file_path.read_text(encoding="utf-8")))
        return docs

    def search(self, query: str, top_k: int = 3) -> List[Tuple[str, str]]:
        query_terms = set(query.lower().split())
        scored_docs = []

        for path, text in self.documents:
            text_lower = text.lower()
            score = sum(1 for term in query_terms if term in text_lower)
            if score > 0:
                scored_docs.append((score, path, text))

        scored_docs.sort(reverse=True, key=lambda item: item[0])
        return [(path, text) for _, path, text in scored_docs[:top_k]]
