from crewai import Agent

class ReportAgent:
    def __init__(self):
        self.agent = Agent(
            role="Report Generator",
            goal="Compile analysis and ATS results into a structured, human-readable report",
            backstory="An expert in summarizing data and presenting resume evaluation in a clean format.",
            allow_delegation=False
        )

    def generate_report(self, analysis_output, ats_score, missing_keywords):
        report = f"""
📊 **Relevance Score**: {self._extract_score(analysis_output)}/100

✅ **Strengths:**
{self._extract_list(analysis_output, "Strengths")}

⚠️ **Weaknesses:**
{self._extract_list(analysis_output, "Weaknesses")}

📈 **ATS Score**: {ats_score}/100

🔍 **Missing Keywords for ATS**:
{', '.join(missing_keywords) if missing_keywords else 'None'}

🛠️ **Recommendation**:
Add missing keywords and align experience to job description for higher ATS ranking.
"""
        return report

    def _extract_score(self, text):
        import re
        match = re.search(r"Relevance Score[:\s]*([0-9]{1,3})", text)
        return match.group(1) if match else "N/A"

    def _extract_list(self, text, section_name):
        import re
        pattern = rf"{section_name}:\s*((?:- .+\n?)+)"
        match = re.search(pattern, text)
        return match.group(1).strip() if match else "None listed"

    def get_agent(self):
        return self.agent


# Gathers:

# ResumeAnalyzer’s output
# ATSScorer’s score
# SectionFixer’s suggestions
# Compiles a single structured markdown/text output for user