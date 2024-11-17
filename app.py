from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from dotenv import load_dotenv
import deepl
from openai import OpenAI

# Load environment variables
load_dotenv()
GROQCLOUD_API_KEY = os.getenv("GROQCLOUD_API_KEY")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

# Ensure API keys are available
if not GROQCLOUD_API_KEY or not DEEPL_API_KEY:
    raise ValueError("API keys are missing. Please check the .env file.")

client = OpenAI(api_key=GROQCLOUD_API_KEY, base_url="https://api.groq.com/openai/v1")
translator = deepl.Translator(DEEPL_API_KEY)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_PATH = os.path.join(BASE_DIR, "dictionaries")

# Function to generate German sentence based on level and word
def sentencegenerate(level: str, word: str):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """Generate a single short-medium German sentence at the provided level using the provided word. The provided word will be in the format 'GermanWord|TurkishWord(s)'. Ensure the German word fits the language level and choose the meaning most relevant to the context of the word in the target language. For ambiguous words with multiple meanings, prioritize less general contexts (e.g., use *spielen* for "çalmak (enstrüman)" rather than "oynamak" unless explicitly referring to sports). Include only one sentence without additional text or explanations."""
                },
                {
                    "role": "user",
                    "content": "Level: A2, Word: schlecht|kötü"
                },
                {
                    "role": "assistant",
                    "content": "Die Suppe war gestern Abend schlecht."
                },
                {
                    "role": "user",
                    "content": "Level: A1, Word: der Freund|erkek arkadaş"
                },
                {
                    "role": "assistant",
                    "content": "Ich habe einen Freund."
                },
                {
                    "role": "user",
                    "content": "Level: B1, Word: das Instrument|enstrüman"
                },
                {
                    "role": "assistant",
                    "content": "Mein Schwager spielt das Instrument sehr gut."
                },
                {
                    "role": "user",
                    "content": "Level: A2, Word: die Klasse|sınıf"
                },
                {
                    "role": "assistant",
                    "content": "Ich bin in der ersten Klasse."
                },
                {
                    "role": "user",
                    "content": "Level: C1, Word: das Blatt|yaprak"
                },
                {
                    "role": "assistant",
                    "content": "Vor einigen Jahren habe ich auf einem Blatt Papier eine sehr persönliche Geschichte meiner Großmutter aufgeschrieben."
                },
                {
                    "role": "user",
                    "content": "Level: A1, Word: die Sprache|dil"
                },
                {
                    "role": "assistant",
                    "content": "Ich lerne gerade eine neue Sprache."
                },
                {
                    "role": "user",
                    "content": "Level: B1, Word: spielen|oynamak, çalmak (enstrüman)"
                },
                {
                    "role": "assistant",
                    "content": "Ich spiele jeden Abend Gitarre, weil es mich entspannt."
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

# Function to translate generated sentence to target language
def sentencetranslate(sentence: str, target_language: str):
    try:
        result = translator.translate_text(sentence, target_lang=target_language)
        print(f"Translated sentence: {result.text}")
        return result.text
    except Exception as e:
        print(f"Error translating sentence: {e}")
        return "Error translating sentence."

# Endpoint to serve dictionary files
@app.route("/dictionary/<filename>")
def get_dictionary(filename):
    return send_from_directory(DICTIONARY_PATH, filename)

# Main route for sentence generation and translation
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word_pair = request.form.get("word")  # Example: "Haus|Ev"
        level = request.form.get("level")
        
        # Debug logs
        print(f"Received word pair: {word_pair}, level: {level}")

        try:
            # Split the word pair into German and Turkish words
            german_word, turkish_word = word_pair.split("|")
        except ValueError:
            return jsonify({"error": "Invalid word pair format. Expected format: 'German|Turkish'."}), 400

        # Generate sentence
        sentence = sentencegenerate(level, german_word)
        
        # Translate the sentence into Turkish
        translated_sentence = sentencetranslate(sentence, "TR")
        
        return jsonify({"sentence": sentence, "translated_sentence": translated_sentence})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
