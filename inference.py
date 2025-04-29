import openai
import os

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define test prompts
test_prompts = [
    "Mujhe ek chai pilao.",
    "Bazaar se kya lau?",
    "Aaj mood kaisa hai?"
]

# Generate responses using the fine-tuned model
for prompt in test_prompts:
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo:your-org:your-model-id",  # Replace with your fine-tuned model ID
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=50
    )
    print(f"Prompt: {prompt}")
    print(f"Response: {response.choices[0].message.content}\n")