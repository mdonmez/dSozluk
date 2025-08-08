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
├── app.py                  # Entry point to run the Flask application
├── src                     # Source code
│   ├── __init__.py
│   ├── main.py             # Flask application logic
│   └── services            # Business logic and API clients
│       ├── __init__.py
│       ├── api_clients.py
│       └── sentence_service.py
├── dictionaries
│   ├── de.txt              # German word list
│   └── tr.txt              # Turkish word list
├── static
│   ├── css
│   │   └── style.css       # Stylesheet
│   ├── js
│   │   ├── api.js          # API handling
│   │   ├── main.js         # Main script
│   │   └── ui.js           # UI handling
│   └── favicon.png
├── templates
│   └── index.html          # HTML template
├── .env                    # Environment variables (API keys)
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata
├── LICENSE                 # GPL v3.0 License
└── README.md
```

## Architecture

The application is built with a simple client-server architecture:

-   **Backend**: A Flask application that serves the frontend and provides an API for sentence generation and translation. The backend is structured into services to separate concerns:
    -   `main.py`: Handles the Flask routes and main application logic.
    -   `services/api_clients.py`: Manages the clients for the Groq and DeepL APIs.
    -   `services/sentence_service.py`: Contains the business logic for generating and translating sentences.
-   **Frontend**: A single-page application built with vanilla JavaScript, HTML, and CSS. The frontend is responsible for displaying the word list, handling user input, and making API calls to the backend. The JavaScript is modularized for better maintainability:
    -   `api.js`: Handles all communication with the backend.
    -   `ui.js`: Manages DOM manipulation and UI updates.
    -   `main.js`: The main script that ties everything together.

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
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file and add your API keys:**

    ```
    GROQCLOUD_API_KEY="YOUR_GROQ_API_KEY"
    DEEPL_API_KEY="YOUR_DEEPL_API_KEY"
    ```

4.  **Run the application:**

    ```bash
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature`).
6.  Open a pull request.

## License

This project is licensed under the GPL v3.0 License. See the [LICENSE](LICENSE) file for details.