from crewai import Agent, Task
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ResumeAnalyzerAgent:
    def __init__(self):
        self.agent = Agent(
            role="Resume Analyzer",
            goal="Analyze resume relevance to job description and provide strengths and weaknesses",
            backstory="Expert in HR, ATS systems, and GPT-powered matching tools.",
            allow_delegation=False
        )

    def analyze_task(self, resume_text, jd_text):
        prompt = f"""
You are an ATS resume evaluator.
Compare the resume and job description below and perform the following:
1. Provide a **Relevance Score** out of 100.
2. List 3 **Strengths** from the resume that align with the JD.
3. List 3 **Weaknesses** or missing areas.
Return the output in this format:

Relevance Score: ?/100

Strengths:
- ...
- ...
- ...

Weaknesses:
- ...
- ...
- ...

Resume:
{resume_text}

Job Description:
{jd_text}
"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are an expert ATS evaluator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    def get_agent(self):
        return self.agent


# Uses OpenAI API to:

# Compare resume text and JD
# Give a relevancy score out of 100
# List 3 strengths
# List 3 weaknesses