from .api_clients import groq_client, deepl_translator

def generate_german_sentence(level: str, word: str):
    """
    Generates a German sentence using the Groq API.
    """
    try:
        completion = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """Generate a single short-medium German sentence at the provided level using the provided word. The provided word will be in the format 'GermanWord|TurkishWord(s)'. Ensure the German word fits the language level and choose the meaning most relevant to the context of the word in the target language. For ambiguous words with multiple meanings, prioritize less general contexts (e.g., use *spielen* for "çalmak (enstrüman)" rather than "oynamak" unless explicitly referring to sports). Include only one sentence without additional text or explanations."""
                },
                {
                    "role": "user",
                    "content": f"Level: {level}, Word: {word}"
                }
            ],
            temperature=1,
            top_p=1,
            stream=False,
        )
        sentence = completion.choices[0].message.content
        print(f"Generated sentence: {sentence}")
        return sentence
    except Exception as e:
        print(f"Error generating sentence: {e}")
        return "Error generating sentence."

def translate_to_turkish(sentence: str):
    """
    Translates a sentence to Turkish using the DeepL API.
    """
    try:
        result = deepl_translator.translate_text(sentence, target_lang="TR")
        print(f"Translated sentence: {result.text}")
        return result.text
    except Exception as e:
        print(f"Error translating sentence: {e}")
        return "Error translating sentence."
