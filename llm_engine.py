from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def analyze_resume(text):
    prompt = f"""
    Analyze this resume:
    {text}

    Give:
    - Skills
    - Improvements
    - Rating out of 10
    """

    result = generator(prompt, max_length=200, num_return_sequences=1)

    return result[0]['generated_text']

