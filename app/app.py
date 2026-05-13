import streamlit as st

from ..src.core import analyze_resume


# Page Config
st.set_page_config(
    page_title="ATS Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 ATS Resume Analyzer")

st.markdown(
    """
AI-powered ATS evaluation system using LangChain,
Pydantic schema validation, and LLM structured analysis.
"""
)

# Layout
col1, col2 = st.columns(2)

# Resume Input
with col1:

    st.subheader("Resume")

    resume_text = st.text_area(
        "Paste Resume Content",
        height=400,
        placeholder="Paste full resume here..."
    )

# JD Input
with col2:

    st.subheader("Job Description")

    job_description_text = st.text_area(
        "Paste Job Description",
        height=400,
        placeholder="Paste full job description here..."
    )

# Analyze Button
if st.button("Analyze Resume", use_container_width=True):

    with st.spinner("Analyzing resume..."):

        result = analyze_resume(
            resume_text,
            job_description_text
        )

    # Error Handling
    if isinstance(result, dict):

        if "error" in result:
            st.error(result["error"])

    else:

        st.success("Analysis Complete")

        st.divider()

        # ATS Score
        st.metric(
            label="ATS Score",
            value=f"{result.ats_score}/100"
        )

        # Skills Columns
        col3, col4 = st.columns(2)

        # Matching Skills
        with col3:

            st.subheader("✅ Matching Skills")

            if result.matching_skills:
                for skill in result.matching_skills:
                    st.write(f"- {skill}")
            else:
                st.write("No matching skills found.")

        # Missing Skills
        with col4:

            st.subheader("❌ Missing Skills")

            if result.missing_skills:
                for skill in result.missing_skills:
                    st.write(f"- {skill}")
            else:
                st.write("No missing skills identified.")

        # Experience Alignment
        st.subheader("📌 Experience Alignment")
        st.write(result.experience_alignment)

        # Strengths
        st.subheader("💪 Resume Strengths")

        if result.resume_strengths:
            for strength in result.resume_strengths:
                st.write(f"- {strength}")

        # Weaknesses
        st.subheader("⚠ Resume Weaknesses")

        if result.resume_weaknesses:
            for weakness in result.resume_weaknesses:
                st.write(f"- {weakness}")

        # Suggestions
        st.subheader("🚀 Improvement Suggestions")

        if result.improvement_suggestions:
            for suggestion in result.improvement_suggestions:
                st.write(f"- {suggestion}")

        # Recommendation
        st.subheader("📋 Final Recommendation")
        st.info(result.final_recommendation)

        # Interview Probability
        st.subheader("🎯 Interview Probability")
        st.write(result.interview_probability)