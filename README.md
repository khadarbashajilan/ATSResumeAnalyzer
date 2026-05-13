# ATS Resume Analyzer

An advanced Applicant Tracking System (ATS) Resume Evaluator that analyzes resumes against job descriptions using strict ATS-style analysis. This component provides both a Python API and a Streamlit web interface for evaluating candidate resumes.

## Features

- **ATS Keyword Alignment**: Evaluates resume content against job description keywords
- **Technical Skill Matching**: Identifies matching and missing technical skills
- **Experience Analysis**: Assesses experience relevance to the job description
- **Resume Strengths and Weaknesses**: Identifies strong points and areas for improvement
- **Hiring Recommendations**: Provides final hiring recommendations
- **Interview Probability Estimation**: Estimates the likelihood of interview selection
- **Web Interface**: User-friendly Streamlit interface for easy resume analysis

## Installation

1. Ensure you have the required dependencies installed (see project root README.md for details).

2. Navigate to the ATSResumeAnalyzer directory:
   ```bash
   cd ATSResumeAnalyzer
   ```

## Usage

### Python API

1. Import the `analyze_resume` function from `core.py`:
   ```python
   from core import analyze_resume
   ```

2. Call the function with resume text and job description text:
   ```python
   result = analyze_resume(resume_text, job_description_text)
   ```

3. The function returns an `ATSResponse` object with the following fields:
   - `ats_score`: ATS compatibility score out of 100
   - `matching_skills`: List of skills matching the job description
   - `missing_skills`: List of important missing skills
   - `experience_alignment`: Summary of experience alignment
   - `resume_strengths`: List of strong points in the resume
   - `resume_weaknesses`: List of weak areas in the resume
   - `improvement_suggestions`: List of suggestions to improve ATS score
   - `final_recommendation`: Final hiring recommendation
   - `interview_probability`: Estimated interview selection probability

### Web Interface

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. The web interface will open in your default browser, allowing you to:
   - Paste resume content
   - Paste job description content
   - Analyze the resume against the job description
   - View detailed analysis results

## Important Rules

- ONLY analyzes information explicitly present in the resume
- NEVER invents or assumes skills, projects, certifications, experience, education, or achievements
- If information is missing, explicitly mentions it
- Does NOT create hypothetical resumes or example content
- Keeps all evaluations grounded strictly in provided resume content
- Be concise, professional, and evidence-based

## Response Schema

The analyzer returns responses in the following schema (defined in `schema.py`):

```python
class ATSResponse(BaseModel):
    ats_score: int
    matching_skills: List[str]
    missing_skills: List[str]
    experience_alignment: str
    resume_strengths: List[str]
    resume_weaknesses: List[str]
    improvement_suggestions: List[str]
    final_recommendation: str
    interview_probability: str
```

## Example

Here's an example of how to use the analyzer:

```python
from core import analyze_resume

resume_text = """
John Doe
Software Engineer

Skills:
- Python
- JavaScript
- SQL
- Machine Learning
- Data Analysis

Experience:
- Senior Software Engineer at Tech Corp (2018-Present)
- Software Engineer at Dev Solutions (2015-2018)
"""

job_description_text = """
We are looking for a Senior Software Engineer with expertise in:
- Python
- JavaScript
- Machine Learning
- Data Analysis

Experience with cloud platforms is a plus.
"""

result = analyze_resume(resume_text, job_description_text)
print(result)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.