from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ['GEMINI_API_KEY']

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model="gemini-1.5-flash-8b",
        api_key=api_key
    )
    return openai_model_client

    