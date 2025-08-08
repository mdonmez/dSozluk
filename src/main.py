from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import logging
from .services.sentence_service import generate_german_sentence, translate_to_turkish

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Define base directory and dictionary path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DICTIONARY_PATH = os.path.join(BASE_DIR, "..", "dictionaries")

# Endpoint to serve dictionary files
@app.route("/dictionary/<filename>")
def get_dictionary(filename):
    return send_from_directory(DICTIONARY_PATH, filename)

# Main route for sentence generation and translation
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word_pair = request.form.get("word")
        level = request.form.get("level")

        logging.info(f"Received word pair: {word_pair}, level: {level}")

        if not word_pair or not level:
            return jsonify({"error": "Missing 'word' or 'level' in request."}), 400

        try:
            german_word, turkish_word = word_pair.split("|")
            if not german_word or not turkish_word:
                raise ValueError("Both German and Turkish words must be non-empty.")
        except ValueError:
            logging.error(f"Invalid word pair format: {word_pair}")
            return jsonify({"error": "Invalid word pair format. Expected 'German|Turkish' with both parts non-empty."}), 400

        # Generate German sentence
        sentence = generate_german_sentence(level, german_word)
        if "Error" in sentence:
            return jsonify({"error": sentence}), 500

        # Translate the sentence to Turkish
        translated_sentence = translate_to_turkish(sentence)
        if "Error" in translated_sentence:
            return jsonify({"error": translated_sentence}), 500

        return jsonify({"sentence": sentence, "translated_sentence": translated_sentence})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
