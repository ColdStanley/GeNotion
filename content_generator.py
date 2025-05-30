import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_content(prompt_text):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        print("❌ Gemini 返回错误：", e)
        return "[Gemini Error] " + str(e)
