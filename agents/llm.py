import openai

def extract_symptoms_with_llm(user_input):
    prompt = f"""
You are a medical assistant. Extract all possible symptoms mentioned in the following text.
Return only a Python list of symptoms (all lowercase), e.g., ["fever", "cough"].

Text: "{user_input}"
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    # Extract content
    extracted_text = response.choices[0].message.content
    # Convert string to Python list safely
    try:
        symptoms = eval(extracted_text)
        if isinstance(symptoms, list):
            return [s.lower() for s in symptoms]
        return []
    except:
        return []
