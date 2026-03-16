import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()


def code_reviewer():
    conversation_history = []
    print("Chat with Claude: Code Reviewer (press 'quit' to exit)")

    while True:
        user_input = input("You: ")

        if (user_input.lower() == 'quit'):
            print("Goodbye!")
            break

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system="You get a python function as input and your role is to explain: what it does, suggest improvements, identify any bugs",
            messages=conversation_history,
        )

        assistant_message = response.content[0].text

        conversation_history.append({
            'role': 'assistant',
            'content': assistant_message
        })

        print(f"\nClaude: {assistant_message}\n")


code_reviewer()
