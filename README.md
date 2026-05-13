# ATS Resume Analyzer

AI-powered ATS Resume Analyzer built with Python, Streamlit, and NVIDIA AI endpoints to evaluate resumes against job descriptions using ATS-style scoring, skill matching, and hiring recommendations.

---

## Features

- ATS compatibility scoring
- Resume vs Job Description comparison
- Technical skill extraction
- Missing skill detection
- Experience alignment analysis
- Resume strengths & weaknesses
- AI-generated improvement suggestions
- Interview probability estimation
- Structured JSON schema responses
- Interactive Streamlit web interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- NVIDIA AI Endpoints
- Pydantic
- Prompt Engineering
- Pandas & NumPy

---

## Project Structure

```bash
ATSResumeAnalyzer/
│
├── app/
│   └── app.py                  # Streamlit frontend
│
├── src/
│   ├── core.py                 # ATS analysis engine
│   ├── schema.py               # Pydantic response schema
│   ├── promptTemplates.py      # Prompt templates
│   └── __init__.py
│
├── .env.example
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/khadarbashajilan/ATSResumeAnalyzer.git
cd ATSResumeAnalyzer
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```env
NVIDIA_API_KEY=your_api_key_here
```

You can use the provided `.env.example` file as reference.

---

## Run the Application

Start the Streamlit app:

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

## How It Works

1. User provides:
   - Resume content
   - Job description

2. The analyzer evaluates:
   - ATS keyword alignment
   - Technical skill relevance
   - Experience alignment
   - Resume strengths and weaknesses

3. The system generates:
   - ATS score
   - Missing skills
   - Hiring recommendation
   - Interview probability
   - Improvement suggestions

---

## Architecture

The application uses an LLM-powered ATS evaluation pipeline:

1. Resume and Job Description are provided as input
2. Prompt templates structure ATS evaluation tasks
3. NVIDIA AI endpoints process the analysis
4. Structured responses are validated using Pydantic
5. Streamlit displays the ATS evaluation dashboard

---

## Important Rules

- ONLY analyzes information explicitly present in the resume
- NEVER invents skills, certifications, or experience
- Keeps evaluations evidence-based
- Provides ATS-focused recommendations
- Maintains concise and professional output

---

## Future Improvements

- PDF resume upload
- Resume parsing using OCR
- Multi-resume comparison
- Export analysis to PDF
- Resume optimization assistant
- Skill gap visualization
- Advanced ATS scoring models
- Authentication system
- Resume history tracking

---

## Requirements

Main dependencies:

```txt
streamlit
pydantic
python-dotenv
langchain
langchain-community
langchain-core
langchain-nvidia-ai-endpoints
openrouter
pandas
numpy
```

---

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Author

Khadar Basha Jilan

GitHub: https://github.com/khadarbashajilan