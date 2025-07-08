# dSözlük

dSözlük is a simple German-Turkish dictionary application with a sentence generator. It allows users to search for words, view their translations, and generate example sentences at different language levels (A1-C2).

## Features

- **German-Turkish Dictionary**: Basic translation of 150 common German words.
- **Sentence Generation**: Generate example sentences for a given word and language level using the Groq API with LLaMA 3.1.
- **Sentence Translation**: Translate the generated German sentence into Turkish using the DeepL API.
- **Web Interface**: A simple and intuitive web interface built with Flask and vanilla JavaScript.

## Project Structure

```
.
├── app.py                # Flask application
├── dictionaries
│   ├── de.txt            # German word list
│   └── tr.txt            # Turkish word list
├── static
│   ├── script.js         # Frontend JavaScript
│   └── style.css         # CSS styles
├── templates
│   └── index.html        # HTML template
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Python dependencies
├── pyproject.toml        # Project metadata
├── LICENSE               # GPL v3.0 License
└── README.md
```

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/mdonmez/dSozluk.git
    cd dSozluk
    ```

2.  **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    uv add -r requirements.txt
    ```

3.  **Create a `.env` file and add your API keys:**

    ```
    GROQCLOUD_API_KEY="YOUR_GROQ_API_KEY"
    DEEPL_API_KEY="YOUR_DEEPL_API_KEY"
    ```

4.  **Run the application:**

    ```bash
    uv run app.py
    ```

    The application will be available at `http://127.0.0.1:5000`.

## How it Works

1.  The user selects a word from the list or searches for a word.
2.  The user selects a language level (A1-C2).
3.  The user clicks the "Cümle Oluştur" (Generate Sentence) button.
4.  The Flask backend receives the request and calls the `sentencegenerate` function.
5.  The `sentencegenerate` function sends a request to the Groq API with the word and level to generate a German sentence.
6.  The generated sentence is then passed to the `sentencetranslate` function, which calls the DeepL API to translate the sentence into Turkish.
7.  The German sentence and its Turkish translation are returned to the frontend and displayed to the user.

## Technologies Used

-   **Backend**: Flask
-   **Frontend**: HTML, CSS, JavaScript
-   **APIs**:
    -   Groq API (for sentence generation)
    -   DeepL API (for translation)
-   **Python Libraries**:
    -   `flask`
    -   `python-dotenv`
    -   `deepl`
    -   `openai` (used with Groq)

## License

This project is licensed under the GPL v3.0 License. See the [LICENSE](LICENSE) file for details.