import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def chat():
    conversation_history = []

    print("Chat with Claude (type 'quit' to exit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_input,
        })

        # Send entire history every time
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system="You are a helpful Python tutor.",
            messages=conversation_history,
        )

        assistant_message = response.content[0].text

        # Add assistant response to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message,
        })

        print(f"\nClaude: {assistant_message}\n")


chat()
