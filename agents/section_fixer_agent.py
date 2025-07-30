from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class SectionFixerAgent:
    def suggest_section_improvements(self, resume_text, jd_text):
        prompt = f"""
You are an ATS expert specializing in improving resumes for maximum match with job descriptions.

Analyze the following resume and job description, and return a section-wise improvement plan.
Each section should include:
- 🔧 Missing keywords or content
- 📌 Suggested improvements
- ✅ Skip if no issues

Expected format:
📊 ATS Score: (estimate if needed)
Sections That Need Improvement:

🔧 Skills
- Missing keywords: ...
- Suggested action: ...

💼 Experience
...

🎓 Education
...

📈 Formatting
...

Resume:
{resume_text}

Job Description:
{jd_text}
"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that improves resumes section-by-section for better ATS performance."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

# This agent:

# Takes the resume and JD as input

# Identifies weaknesses or missing areas section-wise:
# Skills
# Experience
# Education
# Formatting
# Suggests what changes to make in each section to improve the ATS score.