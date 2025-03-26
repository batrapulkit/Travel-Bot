import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Load API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(prompt: str, model="gpt-3.5-turbo", max_tokens=150):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return None
