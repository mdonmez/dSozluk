from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from dotenv import load_dotenv
import deepl
from openai import OpenAI

# Load environment variables
load_dotenv()
GROQCLOUD_API_KEY = os.getenv("GROQCLOUD_API_KEY")
DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
client = OpenAI(api_key=GROQCLOUD_API_KEY, base_url="https://api.groq.com/openai/v1")
translator = deepl.Translator(DEEPL_API_KEY)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_PATH = os.path.join(BASE_DIR, "dictionaries")

# Function to generate German sentence based on level and word
def sentencegenerate(level: str, word: str):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
        {
            "role": "system",
            "content": "Generate a single short-medium German sentence at the provided level using the provided word. Ensure it fits the language level and contains only one sentence with no additional text or explanations."
        },
        {
            "role": "user",
            "content": "Level: A2, Word: schlecht"
        },
        {
            "role": "assistant",
            "content": "Die Suppe war gestern Abend schlecht."
        },
        {
            "role": "user",
            "content": "Level: A1, Word: der Freund"
        },
        {
            "role": "assistant",
            "content": "Ich habe einen Freund."
        },
        {
            "role": "user",
            "content": "Level: B1, Word: das Instrument"
        },
        {
            "role": "assistant",
            "content": "Mein Schwager spielt das Instrument sehr gut."
        },
        {
            "role": "user",
            "content": "Level: A2, Word: die Klasse"
        },
        {
            "role": "assistant",
            "content": "Ich bin in der ersten Klasse."
        },
        {
            "role": "user",
            "content": "Level: C1, Word: das Blatt"
        },
        {
            "role": "assistant",
            "content": "Vor einigen Jahren habe ich auf einem Blatt Papier eine sehr persönliche Geschichte meiner Großmutter aufgeschrieben."
        },
        {
            "role": "user",
            "content": f"Level: {level}, Word: {word}"
        }
        ],
            temperature=0.9,
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
        word = request.form.get("word")
        level = request.form.get("level")
        
        # Debug logs
        print(f"Received word: {word}, level: {level}")

        sentence = sentencegenerate(level, word)
        translated_sentence = sentencetranslate(sentence, "TR")
        
        return jsonify({"sentence": sentence, "translated_sentence": translated_sentence})
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
