from dotenv import load_dotenv
import os
from google import genai
from config import *

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def get_response(contents):
	client = genai.Client(api_key=api_key)
	config = {
		'temperature' : TEMPERATURE,
		'topP' : TOP_P,
		'topK' : TOP_K,
		'maxOutputTokens': MAX_OUTPUT_TOKENS,
		'frequencyPenalty' : FREQUENCY_PENALTY,
		'presencePenalty': PRESENCE_PENALTY}
	
	response = client.models.generate_content(
		model=MODEL_NAME,
		contents=contents,
		config=config)
	return response.text
