# This library is a wrapper — it hides all the complex HTTP request code
import anthropic

# You're importing one specific function — `load_dotenv` — from the `python-dotenv` library you installed.
# This function's only job is to find your `.env` file and read it.
from dotenv import load_dotenv

# This actually **executes** that function. When it runs it:
# 1. looks for a `.env` file in your current folder
# 2. reads every line
# 3. injects each variable into your system's environment
load_dotenv()

# This creates an instance of the Anthropic class
client = anthropic.Anthropic()


def ask(question, system="You are a helpful assistant."):
    response = client.messages.create(
        # fastest and cheapest model, perfect for learning
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": question}],
    )
    return response.content[0].text

# print(response)
# response.content          # list of content blocks
# response.content[0].text  # the actual text response
# response.model            # which model responded
# response.stop_reason      # why it stopped (end_turn = finished naturally)
# response.usage            # how many tokens were used (affects cost)


# to get just the text:
# print(response.content[0].text)

# Same question, different system prompts → completely different answers
print(ask("What is Python?"))

print(ask("What is Python?",
          system="You are a pirate. Answer everything like a pirate."))

print(ask("What is Python?",
          system="You are a teacher explaining to a 5 year old."))
