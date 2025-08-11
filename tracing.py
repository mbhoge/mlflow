"""
This is an example for leveraging MLflow's auto tracing capabilities for Anthropic.

For more information about MLflow Tracing, see: https://mlflow.org/docs/latest/llms/tracing/index.html
"""

import os
import dotenv

dotenv.load_dotenv()

import anthropic

import mlflow

# Turn on auto tracing for Anthropic by calling mlflow.anthropic.autolog()
mlflow.anthropic.autolog()

# Configure your API key.
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY environment variable is not set. Please set it with your Anthropic API key.")
client = anthropic.Anthropic(api_key=api_key)

# Use the create method to create new message.
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude"},
    ],
)
print(message.content)