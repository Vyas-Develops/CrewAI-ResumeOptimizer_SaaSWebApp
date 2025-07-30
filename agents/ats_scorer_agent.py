from crewai import Agent
from agents.utils import extract_keywords

class ATSScorerAgent:
    def __init__(self):
        self.agent = Agent(
            role="ATS Scoring Agent",
            goal="Calculate ATS score by comparing resume content with JD keywords",
            backstory="A recruiter bot trained to understand keyword matching for Applicant Tracking Systems.",
            allow_delegation=False
        )

    def calculate_ats_score(self, resume_text, jd_text):
        jd_keywords = extract_keywords(jd_text)
        matched_keywords = [kw for kw in jd_keywords if kw in resume_text]
        score = int((len(matched_keywords) / len(jd_keywords)) * 100) if jd_keywords else 0
        missing_keywords = set(jd_keywords) - set(matched_keywords)

        return score, missing_keywords

    def get_agent(self):
        return self.agent


# Checks if key ATS keywords from JD are missing in resume
# Generates a score based on keyword match