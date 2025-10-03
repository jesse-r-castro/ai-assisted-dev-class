# CSV Storyteller Dashboard - Software Requirements Document

## 1. Executive Summary

The CSV Storyteller Dashboard is a local-first Python/Streamlit web application designed for rapid data exploration and insight generation. Users upload CSV files to instantly receive descriptive statistics, interactive visualizations, and AI-generated natural language summaries of their data patterns. The application prioritizes simplicity, speed, and offline capability, making data analysis accessible to non-technical users while providing value to analysts seeking quick insights. Built with a 90-minute development timeline in mind, the MVP focuses on core functionality with clear extension points for future enhancements.

## 2. Target Users & Primary Use-Cases

### Target Users
- **Business analysts** needing quick data overviews
- **Data scientists** exploring new datasets
- **Managers** reviewing departmental metrics
- **Students/researchers** analyzing survey or experimental data
- **Anyone** with CSV data seeking immediate insights

### Primary Use-Cases
- Upload CSV file and get instant data profile
- Generate quick visualizations for presentations
- Understand data quality and completeness
- Get AI-powered narrative summaries of trends
- Export insights for reports or sharing
- Work offline when network/API access is limited

## 3. Functional Requirements

### 3.1 File Upload & Validation
- **CSV Upload**: Drag-and-drop or file picker interface
- **Format Validation**: Support standard CSV formats with common delimiters
- **Size Limits**: Handle files up to 50MB (configurable)
- **Error Handling**: Clear messaging for unsupported formats or corrupted files
- **Preview**: Show first 5 rows after successful upload

### 3.2 Descriptive Statistics
- **Basic Stats**: Count, mean, median, mode, std dev for numerical columns
- **Data Types**: Automatic detection (numeric, categorical, datetime, text)
- **Missing Data**: Count and percentage of null/empty values per column
- **Unique Values**: Count of distinct values for categorical columns
- **Distribution Summary**: Min, max, quartiles for numerical data

### 3.3 Visualization
- **Auto-Generated Charts**: 
  - Histograms for numerical columns
  - Bar charts for categorical columns (top 10 values)
  - Correlation heatmap for numerical columns
- **Interactive Elements**: Plotly-based charts with zoom, pan, hover
- **Export Options**: Download charts as PNG/SVG
- **Responsive Design**: Charts adapt to screen size

### 3.4 Natural-Language Summary
- **LLM Integration**: Generate narrative summary of key findings
- **Fallback Mode**: Template-based summary when LLM unavailable
- **Summary Sections**:
  - Dataset overview (rows, columns, completeness)
  - Key patterns and outliers
  - Notable correlations or trends
  - Data quality observations
- **Configurable Providers**: Support OpenAI, Anthropic, or local models

### 3.5 UI/UX Flow
1. **Landing Page**: Upload area with instructions and examples
2. **Processing**: Progress indicator during analysis
3. **Results Dashboard**: Tabbed interface showing stats, charts, summary
4. **Export Options**: Download results as PDF or JSON report
5. **Reset/New Analysis**: Clear current data and start fresh

## 4. Non-Functional Requirements

### Performance
- **Response Time**: Initial analysis completes within 10 seconds for typical files
- **Memory Usage**: Handle datasets up to 100k rows efficiently
- **Caching**: Cache analysis results during session

### Security
- **Local Processing**: All data analysis happens locally
- **No Data Persistence**: Clear uploaded data on session end
- **API Key Security**: Secure storage of LLM API credentials
- **Secret Detection**: Pre-commit hooks prevent credential commits
- **Input Sanitization**: Validate all uploaded content

### Portability
- **Cross-Platform**: Run on Windows, macOS, Linux
- **Container Support**: Single Dockerfile for deployment
- **Virtual Environment**: Standard Python venv setup
- **Minimal Dependencies**: Keep requirements.txt lean

### Offline Fallback
- **Template Summaries**: Generate insights without LLM when offline
- **Cached Models**: Option to use local/offline language models
- **Graceful Degradation**: Full functionality except AI summaries when disconnected

## 5. Technology Stack & Dependencies

### Core Framework
- **Python 3.9+**: Primary language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

### Visualization
- **Plotly**: Interactive charts and graphs
- **Matplotlib/Seaborn**: Fallback visualization options

### AI/LLM Integration
- **OpenAI API**: Primary LLM provider
- **Anthropic API**: Alternative LLM provider
- **Requests**: HTTP client for API calls
- **Python-dotenv**: Environment variable management

### Development & Deployment
- **pytest**: Unit testing framework
- **Docker**: Containerization
- **Black**: Code formatting
- **Ruff**: Linting and code quality
- **detect-secrets**: Pre-commit hook for secret detection
- **pre-commit**: Git hook management

## 6. API/Module Sketch

### Core Modules

```python
# data_processor.py
def load_csv(file_path: str, delimiter: str = ',') -> pd.DataFrame
def validate_data(df: pd.DataFrame) -> dict[str, Any]
def generate_statistics(df: pd.DataFrame) -> dict[str, Any]

# visualizer.py
def create_histogram(df: pd.DataFrame, column: str) -> plotly.Figure
def create_bar_chart(df: pd.DataFrame, column: str, top_n: int = 10) -> plotly.Figure
def create_correlation_heatmap(df: pd.DataFrame) -> plotly.Figure

# summarizer.py
def generate_llm_summary(stats: dict, provider: str = 'openai') -> str
def generate_template_summary(stats: dict) -> str
def configure_llm_client(provider: str, api_key: str) -> object

# streamlit_app.py
def main() -> None
def render_upload_interface() -> pd.DataFrame | None
def render_analysis_dashboard(df: pd.DataFrame) -> None
def export_results(data: dict, format: str) -> bytes
```

### Configuration

```python
# config.py
@dataclass
class AppConfig:
    max_file_size_mb: int = 50
    llm_provider: str = 'openai'
    api_key: str = ''
    enable_offline_mode: bool = True
    chart_theme: str = 'plotly_white'
```

## 7. Stretch Goals

- **Multi-file Analysis**: Compare multiple CSV files side-by-side
- **Data Cleaning Suggestions**: Recommend data quality improvements
- **Custom Chart Builder**: User-defined visualizations
- **Scheduled Reports**: Email summaries on schedule
- **Advanced Statistics**: Hypothesis testing, regression analysis
- **Data Export**: Clean/processed CSV download
- **Collaboration Features**: Share analysis links
- **Jupyter Notebook Export**: Generate analysis notebooks

## 8. Out-of-Scope Items

- **Database Integration**: No connection to external databases
- **Real-time Data**: No streaming or live data processing
- **User Authentication**: No login/user management system
- **Advanced ML**: No predictive modeling or machine learning
- **Complex Joins**: No multi-table operations
- **Cloud Storage**: No direct cloud service integration
- **Mobile App**: Web-only interface
- **Enterprise SSO**: No corporate authentication systems

## 9. Acceptance Criteria & Quick Test Plan

### Core Functionality Tests
- [ ] Upload valid CSV file (≤50MB) successfully
- [ ] Display correct row/column counts and data types
- [ ] Generate appropriate charts for sample datasets
- [ ] Produce readable summary (LLM or template-based)
- [ ] Handle malformed CSV with clear error message
- [ ] Export analysis results in multiple formats

### Performance Tests
- [ ] Process 10k row dataset within 10 seconds
- [ ] Handle missing/null data gracefully
- [ ] Maintain responsive UI during processing

### Offline/Fallback Tests
- [ ] Generate template summary when LLM unavailable
- [ ] Continue analysis without internet connection
- [ ] Graceful API failure handling

### Sample Test Datasets
```csv
# test_sales.csv - 1000 rows with sales data
# test_survey.csv - 500 rows with Likert scale responses  
# test_malformed.csv - Invalid CSV for error testing
```

## 10. Deliverables & Folder Structure

### Expected Outputs
- Working Streamlit application
- Docker container with one-command startup
- README with setup and usage instructions
- Requirements.txt with pinned dependencies
- Basic test suite covering core functions

### Project Structure
```
csv-storyteller/
├── src/
│   ├── __init__.py
│   ├── streamlit_app.py          # Main Streamlit app
│   ├── data_processor.py         # CSV processing logic
│   ├── visualizer.py             # Chart generation
│   ├── summarizer.py             # LLM integration
│   └── config.py                 # App configuration
├── tests/
│   ├── __init__.py
│   ├── test_data_processor.py
│   ├── test_visualizer.py
│   └── sample_data/              # Test CSV files
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container definition
├── .env.example                  # Environment template
├── .pre-commit-config.yaml       # Pre-commit hook configuration
├── README.md                     # Setup instructions
└── .gitignore                    # Git exclusions
```

### Startup Commands
```bash
# Local development
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pre-commit install  # Setup git hooks
streamlit run src/streamlit_app.py

# Docker deployment
docker build -t csv-storyteller .
docker run -p 8501:8501 csv-storyteller
```