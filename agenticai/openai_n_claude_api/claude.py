from anthropic import Anthropic
from dotenv import load_dotenv
import os

def interact_with_model():
    load_dotenv()  # Load environment variables from .env file
    client = Anthropic(
        api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    response = client.messages.create(
        max_tokens = 100,
        messages = [{
            "role": "user",
            "content": "What is the capital of France?"
        }],
        model = "claude-haiku-4-5"
    )
    print(response)  # Print the response from the model