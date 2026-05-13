from pydantic import BaseModel, Field
from typing import List


class ATSResponse(BaseModel):

    ats_score: int = Field(
        description="ATS compatibility score out of 100"
    )

    matching_skills: List[str] = Field(
        description="Skills matching the job description"
    )

    missing_skills: List[str] = Field(
        description="Important missing skills"
    )

    experience_alignment: str = Field(
        description="Experience alignment summary"
    )

    resume_strengths: List[str] = Field(
        description="Strong points in the resume"
    )

    resume_weaknesses: List[str] = Field(
        description="Weak areas in the resume"
    )

    improvement_suggestions: List[str] = Field(
        description="Suggestions to improve ATS score"
    )

    final_recommendation: str = Field(
        description="Final hiring recommendation"
    )

    interview_probability: str = Field(
        description="Estimated interview selection probability"
    )