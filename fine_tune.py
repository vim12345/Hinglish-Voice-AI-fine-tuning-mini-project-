# import openai
# import os

# # Set OpenAI API key from environment variable
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Upload the dataset file
# with open("dataset.jsonl", "rb") as file:
#     upload_response = openai.File.create(
#         file=file,
#         purpose="fine-tune"
#     )
# file_id = upload_response["id"]

# # Start the fine-tuning job
# fine_tune_response = openai.FineTuningJob.create(
#     training_file=file_id,
#     model="gpt-3.5-turbo",
#     hyperparameters={
#         "n_epochs": 2
#     }
# )
# print(fine_tune_response)
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Upload the dataset file
with open("dataset.jsonl", "rb") as file:
    upload_response = client.files.create(
        file=file,
        purpose="fine-tune"
    )
file_id = upload_response.id

# Start the fine-tuning job
fine_tune_response = client.fine_tuning.jobs.create(
    training_file=file_id,
    model="gpt-3.5-turbo",
    hyperparameters={
        "n_epochs": 2
    }
)
print(fine_tune_response)