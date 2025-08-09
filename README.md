# dSözlük - German-Turkish Dictionary with AI-Powered Sentence Generation

A modern German-Turkish dictionary web application that combines traditional vocabulary lookup with AI-powered sentence generation and translation capabilities.

## Features

- 🔍 **Dictionary Lookup**: Search German and Turkish words with instant results
- 🤖 **AI Sentence Generation**: Generate contextual German sentences using any word at different language levels (A1-C2)
- 🌐 **Automatic Translation**: Translate generated sentences from German to Turkish using DeepL
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🎯 **Language Levels**: Support for CEFR language levels (A1, A2, B1, B2, C1, C2)

## Technology Stack

- **Backend**: Flask (Python)
- **AI**: Groq API with Llama 3.1 model for sentence generation
- **Translation**: DeepL API for high-quality translations
- **Frontend**: HTML, CSS, JavaScript
- **Package Management**: uv (fast Python package installer)

## Prerequisites

- Python 3.12 or higher
- uv package manager
- API keys for:
  - Groq API (for AI sentence generation)
  - DeepL API (for translations)

## Installation


### 1. Clone the Repository

```bash
git clone https://github.com/mdonmez/dSozluk.git
cd dSozluk
```

### 2. Set Up Environment and Install Dependencies

```bash
uv sync
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQCLOUD_API_KEY=your_groq_api_key_here
DEEPL_API_KEY=your_deepl_api_key_here
```

**Getting API Keys:**

- **Groq API**: Sign up at [console.groq.com](https://console.groq.com/keys) for free API access
- **DeepL API**: Register at [deepl.com](https://www.deepl.com/en/your-account/keys) (free tier available)

## Usage

### Development Server

Run the application in development mode:

```bash
uv run -m app
```

The application will be available at `http://localhost:5000`

## How to Use

1. **Dictionary Search**: Type German or Turkish words in the search bar to find translations
2. **Sentence Generation**: 
   - Select a word pair from the dictionary
   - Choose your desired language level (A1-C2)
   - Click "Generate Sentence" to create a contextual German sentence
   - View the automatic Turkish translation

## Project Structure

```
dSozluk/
├── app.py                      # Main Flask application
├── pyproject.toml             # Project configuration and dependencies
├── uv.lock                    # Dependency lock file
├── src/
│   ├── services/
│   │   ├── api_clients.py     # API client configurations
│   │   └── sentence_service.py # Sentence generation logic
├── dictionaries/
│   ├── de.txt                 # German vocabulary
│   └── tr.txt                 # Turkish vocabulary
├── templates/
│   └── index.html             # Main web interface
├── static/
│   ├── style.css              # Application styling
│   ├── favicon.png            # Application icon
│   └── js/                    # JavaScript modules
└── README.md                  # This file
```

## Contributing

Contributions are welcome! Please submit a pull request.


## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Groq](https://groq.com/) for fast AI inference
- [DeepL](https://www.deepl.com/) for high-quality translations
- [uv](https://github.com/astral-sh/uv) for fast Python package management
- [Flask](https://flask.palletsprojects.com/) for the web framework

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/mdonmez/dSozluk/issues) on GitHub.