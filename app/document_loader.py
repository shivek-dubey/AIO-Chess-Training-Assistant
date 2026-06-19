from pathlib import Path
from typing import List, Dict

SUPPORTED_EXTENSIONS = {".txt", ".md", ".pgn"}

def load_documents(data_dir: str = "data") -> List[Dict[str, str]]:
    base = Path(data_dir)
    documents: List[Dict[str, str]] = []

    if not base.exists():
        return documents

    for path in base.rglob("*"):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            text = path.read_text(encoding="utf-8", errors="ignore")
            documents.append({
                "source": str(path),
                "content": text
            })
    return documents
