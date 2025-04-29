# Hinglish Voice-AI Fine-Tuning Mini-Project
# Setup Instructions

# Install Dependencies: 
Ensure Python is installed, then install the OpenAI SDK:pip install openai


# Set API Key: 
Export your OpenAI API key as an environment variable:export OPENAI_API_KEY='your-api-key'


# Prepare Dataset: 
Save the provided dataset.jsonl file.
# Run Fine-Tuning: 
Execute the fine-tuning script:python fine_tune.py

This uploads dataset.jsonl and starts fine-tuning. Note the fine-tuned model ID from the output.
# Run Inference: 
Update inference.py with your fine-tuned model ID, then run:python inference.py



# Design Rationale
Dataset Selection & Size

# Why 15 examples? 
A small dataset (10–20 examples) is sufficient for a prototype to demonstrate fine-tuning, as per the assignment. I chose 15 to balance variety and feasibility within the 2-hour constraint.
# Domains: 
Examples cover casual conversation (e.g., "Kaise ho?"), daily activities (e.g., "Sunday ko kya plan hai?"), and practical queries (e.g., "Traffic kaisa hai?") to mimic real-world Hinglish dialogue.
# Style & Length: 
Prompts are short, colloquial, and code-switched (Hindi-English), reflecting natural Hinglish. Responses are concise (1–2 sentences) to suit a Voice-AI's conversational tone.
# Diversity:
Includes greetings, suggestions, and queries to ensure the model learns varied patterns.

# Model & Hyperparameter Choices

# Model: gpt-3.5-turbo
# Why? 
It’s cost-effective, supports chat-based fine-tuning, and is suitable for conversational tasks like Hinglish Voice-AI. Compared to davinci, it’s optimized for dialogue and requires less compute.


# Epochs: 2
# Why? 
Two epochs strike a balance between learning Hinglish patterns and avoiding overfitting on a small dataset. More epochs risk memorizing the data, reducing generalization.


# Learning Rate:
Used default settings.
# Why?
OpenAI’s defaults are tuned for stable fine-tuning on small datasets, reducing the need for manual tuning in a prototype.



# Prompt Formatting & Generation Settings

# Prompt Format:
# Used messages format with role: 
user for prompts, as required by gpt-3.5-turbo’s chat API.
#Why?
This aligns with the model’s expected input for conversational tasks and mirrors the dataset’s structure.


# Inference Settings:
# Temperature: 0.7:
Balances creativity and coherence, allowing natural yet consistent Hinglish responses.
# Max Tokens: 50:
Ensures concise replies suitable for Voice-AI, preventing overly verbose outputs.
# Why? 
These settings promote natural, context-appropriate responses while keeping outputs short for usability.



# Evaluation in Production

# Human Review:
Collect feedback from native Hinglish speakers to assess fluency, cultural relevance, and tone.
# Automated Metrics:
# BLEU/ROUGE:
Compare generated responses to reference Hinglish replies for lexical similarity.
# Perplexity: 
Measure model confidence on Hinglish test prompts to gauge language understanding.


# User Interaction Logs:
Analyze real-world usage to identify common failure cases (e.g., misinterpreting code-switched phrases).
# A/B Testing:
Compare fine-tuned model against base model in live Voice-AI interactions to measure user satisfaction.

# Sample Outputs
Running inference.py with the fine-tuned model (hypothetical outputs, as fine-tuning wasn’t executed):

Prompt: "Mujhe ek chai pilao."
Response: "Ek garam chai coming up!"


Prompt: "Bazaar se kya lau?"
Response: "Kuch fresh sabziyaan le aao."
