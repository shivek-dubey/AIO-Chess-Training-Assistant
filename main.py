from app.coach_agent import ChessCoachAgent


def main():
    print("Welcome to AIO Chess Training Assistant")
    print("Ask a chess training question. Type 'exit' to quit.\n")

    agent = ChessCoachAgent()

    while True:
        question = input("You: ")
        if question.lower().strip() in {"exit", "quit"}:
            print("Good luck with your training!")
            break

        answer = agent.answer(question)
        print("\nAIO Coach:\n")
        print(answer)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
