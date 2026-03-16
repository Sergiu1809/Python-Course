import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def chat():
    conversation_history = []

    print("Chat with Claude! (type: 'quit' to exit, 'history' to print full conversation)")

    while True:
        user_input = input("You: ")

        if (user_input.lower() == "quit"):
            print("Goodbye!\n")
            break

        if (user_input.lower() == "history"):
            if (conversation_history):
                for message in conversation_history:
                    print(f"{message['role']}: {message['content']}\n")
            else:
                print("Conversation history is empty.")
            # continue ← skips everything below, go back to the next iteration"
            continue

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system="You're role is to be a Python tutor",
            messages=conversation_history,
        )

        assistant_message = response.content[0].text

        conversation_history.append({
            "role": "assistant",
            "content": assistant_message,
        })

        print(f"\nClaude: {assistant_message}\n")
        print(
            f"Token usage for input: {response.usage.input_tokens}\nToken usage for output: {response.usage.output_tokens}\n")


chat()
