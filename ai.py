import pathlib
import textwrap
import os

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if GOOGLE_API_KEY is None:
    print("Google API key not found")
    exit()
    
genai.configure(api_key=GOOGLE_API_KEY)
    
model = genai.GenerativeModel('gemini-1.0-pro-latest')

response = model.generate_content("What is the meaning of life?")

if response.candidates:
    generated_text = response.candidates[0].content.parts[0]
    print(generated_text)
else:
    print("No candidates found in the response.")

