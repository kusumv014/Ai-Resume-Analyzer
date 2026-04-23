import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("AIzaSyAASdFKKusjM-E0qtF8MNYUfelklM_eGV0"))

def analyze_resume(text):
    try:
       model = genai.GenerativeModel("models/text-bison-001")

        response = model.generate_content(
            f"""
            Analyze this resume and provide:
            - Key skills
            - Improvements
            - Rating out of 10

            Resume:
            {text}
            """
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"