# CSV Storyteller Dashboard

A local-first Python/Streamlit web application for rapid CSV data exploration and AI-powered insights.

## Quick Start

### Prerequisites
- Python 3.9 or higher
- Git

### Local Development Setup

1. **Clone and navigate to project**:
   ```bash
   git clone <repository-url>
   cd CLASS4
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   pre-commit install  # Setup git hooks
   ```

4. **Configure environment** (optional for AI features):
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the application**:
   ```bash
   streamlit run src/streamlit_app.py
   ```

### Docker Deployment

```bash
docker build -t csv-storyteller .
docker run -p 8501:8501 csv-storyteller
```

Then open http://localhost:8501 in your browser.

## Features

- **File Upload**: Drag-and-drop CSV files for instant analysis
- **Descriptive Statistics**: Automatic data profiling and statistics
- **Interactive Visualizations**: Plotly-powered charts and graphs
- **AI Summaries**: Natural language insights powered by LLMs
- **Export Options**: Download results as PDF or JSON reports
- **Offline Mode**: Template-based summaries when AI is unavailable

## Project Structure

```
csv-storyteller/
├── src/                          # Source code
│   ├── streamlit_app.py         # Main application
│   ├── data_processor.py        # Data analysis logic
│   ├── visualizer.py            # Chart generation
│   ├── summarizer.py            # AI integration
│   └── config.py                # Configuration
├── tests/                       # Test suite
├── requirements.txt             # Dependencies
├── Dockerfile                   # Container definition
├── .env.example                 # Environment template
└── README.md                    # This file
```

## Development

This project follows a test-driven development approach. See `LLM_INSTRUCTIONS.md` for detailed development workflow.

### Running Tests

```bash
pytest tests/ -v                 # Run all tests
pytest --cov=src tests/          # Run with coverage
```

### Code Quality

```bash
pre-commit run --all-files       # Run all quality checks
black .                          # Format code
ruff check .                     # Lint code
```

## Contributing

1. Create a feature branch: `git checkout -b task/NNNN-description`
2. Write tests first, then implement features
3. Ensure all tests pass and code quality checks pass
4. Submit a pull request against the `dev` branch

## License

[Add appropriate license information]

## Support

[Add support/contact information]