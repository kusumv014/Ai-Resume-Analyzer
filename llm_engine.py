import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyAASdFKKusjM-E0qtF8MNYUfelklM_eGV0"))

model = genai.GenerativeModel("gemini-pro")

def analyze_resume(text):
    try:
        response = model.generate_content(
            f"""
            Analyze this resume and provide:
            1. Key skills
            2. Improvements
            3. Rating out of 10

            Resume:
            {text}
            """
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"