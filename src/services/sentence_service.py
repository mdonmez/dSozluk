from .api_clients import groq_client, deepl_translator
from pydantic import BaseModel


class GermanSentence(BaseModel):
    sentence: str


def generate_german_sentence(level: str, word: str) -> str:
    """
    Generates a German sentence using the Groq API.
    """
    try:
        completion = groq_client.chat.completions.create(  # type: ignore
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """Generate a single short-medium German sentence at the provided level using the provided word. The provided word will be in the format 'GermanWord|TurkishWord(s)'. Ensure the German word fits the language level and choose the meaning most relevant to the context of the word in the target language. For ambiguous words with multiple meanings, prioritize less general contexts (e.g., use *spielen* for \"çalmak (enstrüman)\" rather than \"oynamak\" unless explicitly referring to sports). Include only one sentence without additional text or explanations.""",
                },
                {"role": "user", "content": f"Level: {level}, Word: {word}"},
            ],
            response_model=GermanSentence,
        )
        sentence = completion.sentence
        if sentence is None:
            return "Error: No content generated."
        print(f"Generated sentence: {sentence}")
        return sentence
    except Exception as e:
        print(f"Error generating sentence: {e}")
        return "Error generating sentence."


def translate_to_turkish(sentence: str) -> str:
    """
    Translates a sentence to Turkish using the DeepL API.
    """
    try:
        result = deepl_translator.translate_text(sentence, target_lang="TR")
        if not result:
            return "Error: No translation generated."
        # Handle both single TextResult and list of TextResult
        if isinstance(result, list):
            if len(result) == 0:
                return "Error: No translation generated."
            translation = result[0].text
        else:
            translation = result.text

        print(f"Translated sentence: {translation}")
        return translation
    except Exception as e:
        print(f"Error translating sentence: {e}")
        return "Error translating sentence."
