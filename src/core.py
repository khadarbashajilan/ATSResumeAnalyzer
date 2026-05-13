from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from .promptTemplates import system, human
from .schema import ATSResponse

load_dotenv()

# LLM
llm = ChatNVIDIA(
    model="meta/llama-4-maverick-17b-128e-instruct",
    temperature=0.2
)

# Parser
parser = PydanticOutputParser(
    pydantic_object=ATSResponse
)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", human)
    ]
)

# Chain
chain = prompt | llm | parser


def analyze_resume(
    resume_text: str,
    job_description_text: str
):

    # Validation
    if len(resume_text.strip()) < 50:
        return {
            "error": "Resume content insufficient."
        }

    if len(job_description_text.strip()) < 20:
        return {
            "error": "Job description insufficient."
        }

    try:

        response = chain.invoke(
            {
                "resume": resume_text,
                "job_description": job_description_text,
                "format_instructions": parser.get_format_instructions()
            }
        )

        return response

    except Exception as e:

        return {
            "error": str(e)
        }
        
    """https://chatgpt.com/s/t_6a033fc168ec8191ae3338603a6a2dc1
    """