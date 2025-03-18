# openai_service.py
import openai

class OpenAIService:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, prompt):
        """Generates a response from OpenAI's GPT-3."""
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Adjust according to your model
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return str(e)
