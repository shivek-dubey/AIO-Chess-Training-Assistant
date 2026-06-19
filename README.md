# AIO Chess Training Assistant

A RAG-based AI chess coach for young players. It helps with opening preparation, endgame concepts, PGN review, mistake patterns, and tournament training plans.

## Features

- Ask questions from chess training notes
- Retrieve relevant opening/endgame/tournament material
- Coach-style answers with simple explanations
- Sample chess knowledge base included
- Easy to extend with your own PGNs, PDFs, and notes

## Project Structure

```text
AIO-Chess-Training-Assistant/
├── app/
│   ├── coach_agent.py
│   ├── embeddings.py
│   ├── prompt_templates.py
│   ├── rag_engine.py
│   └── vector_store.py
├── config/
│   └── settings.py
├── data/
│   ├── openings/
│   ├── endgames/
│   ├── pgn_games/
│   └── tournament_notes/
├── docs/
│   └── architecture.md
├── models/
│   └── player_profile.py
├── tests/
├── main.py
├── requirements.txt
└── .env.example
```

## Quick Start

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
python main.py
```

## Sample Questions

- Explain opposition in king and pawn endgames.
- What should I revise before a tournament?
- What are the main ideas against the Sicilian?
- Create a 7-day training plan for a young chess player.
- Review my PGN and suggest improvement areas.

## Use Case

This project is designed as a chess-focused RAG assistant. It can be expanded by adding:

- opening notes
- endgame manuals
- player PGNs
- tournament preparation checklists
- coach feedback notes

## Demo Flow

1. User asks a chess training question.
2. System searches local chess knowledge files.
3. Relevant notes are passed to the coach prompt.
4. Assistant returns a structured training answer.

## Future Enhancements

- Add vector database such as FAISS or ChromaDB
- Add PGN parser
- Add FastAPI endpoint
- Add Streamlit UI
- Add player-specific training dashboard
