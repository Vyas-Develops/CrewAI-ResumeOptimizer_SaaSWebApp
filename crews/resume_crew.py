from crewai import Agent, Task, Crew
from agents.file_parser_agent import FileParserAgent
from agents.resume_analyzer_agent import ResumeAnalyzerAgent
from agents.ats_scorer_agent import ATSScorerAgent
from agents.section_fixer_agent import SectionFixerAgent
from agents.report_agent import ReportAgent

class ResumeOptimizerCrew:
    def __init__(self):
        # 1. Instantiate each agent
        self.file_parser = FileParserAgent()
        self.resume_analyzer = ResumeAnalyzerAgent()
        self.ats_scorer = ATSScorerAgent()
        self.section_fixer = SectionFixerAgent()
        self.report_agent = ReportAgent()

    def run(self, resume_file, jd_file):
        # 2. Run file parsing step
        resume_text, jd_text = self.file_parser.parse_files(resume_file, jd_file)

        # 3. Run analysis
        relevance_report = self.resume_analyzer.analyze_task(resume_text, jd_text)
        ats_score, missing_keywords = self.ats_scorer.calculate_ats_score(resume_text, jd_text)
        section_feedback = self.section_fixer.suggest_section_improvements(resume_text, jd_text)

        # Use ReportAgent to generate the report
        report = self.report_agent.generate_report(relevance_report, ats_score, missing_keywords)
        # Optionally, append section_feedback if needed
        report += f"\n\n🔧 Section-wise Feedback:\n{section_feedback}"
        return report

# Initializes each agent with its role, goal, tools (functions)
# Defines a Task for each agent
# Assembles the full Crew (team of agents)
# Runs the Crew().kickoff() method