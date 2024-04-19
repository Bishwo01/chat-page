import os
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define the prompt for the request
prompt = "Once upon a time"

# Make a completion request to the OpenAI API
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=100
)

print(response.choices[0].text)