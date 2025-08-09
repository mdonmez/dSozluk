import os
import deepl
from openai import OpenAI
from dotenv import load_dotenv
import instructor

# Load environment variables
load_dotenv()
GROQCLOUD_API_KEY = os.getenv("GROQCLOUD_API_KEY")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

# Ensure API keys are available
if not GROQCLOUD_API_KEY or not DEEPL_API_KEY:
    raise ValueError("API keys are missing. Please check the .env file.")

client = OpenAI(
    api_key=GROQCLOUD_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

# Initialize clients
groq_client = instructor.patch(
    client,
    mode=instructor.Mode.JSON,
)
deepl_translator = deepl.Translator(DEEPL_API_KEY)
