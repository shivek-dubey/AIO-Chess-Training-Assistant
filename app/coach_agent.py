from app.rag_engine import RAGEngine
from app.prompt_templates import build_coach_prompt


class ChessCoachAgent:
    def __init__(self):
        self.rag = RAGEngine()

    def answer(self, question: str) -> str:
        context = self.rag.retrieve_context(question)

        # Demo response without external LLM dependency.
        # In production, send build_coach_prompt(question, context) to OpenAI/Claude.
        prompt = build_coach_prompt(question, context)

        return self._generate_demo_answer(question, context, prompt)

    def _generate_demo_answer(self, question: str, context: str, prompt: str) -> str:
        return f"""
Concept:
This answer is generated using the local chess knowledge base related to your question: "{question}".

Explanation:
The assistant retrieved the most relevant notes below and uses them as coaching context.

Retrieved Context:
{context}

Practical Example:
Convert the idea into a board exercise. Set up one example position and ask the player to explain the plan before moving.

Training Task:
1. Read the retrieved note once.
2. Solve 3 related positions.
3. Play one practice game focusing only on this theme.
4. Write one mistake and one improvement point after the game.

Developer Note:
To connect a real LLM, replace this demo generator with an OpenAI/Claude API call using the prepared coach prompt.
""".strip()
