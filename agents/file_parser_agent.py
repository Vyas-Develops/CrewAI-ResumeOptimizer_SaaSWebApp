from crewai import Agent, Task
import fitz  # PyMuPDF
import docx

class FileParserAgent:
    def __init__(self):
        self.agent = Agent(
            role="File Parser",
            goal="Extract raw text from resumes and job descriptions",
            backstory="You specialize in parsing structured documents and preparing them for further analysis.",
            allow_delegation=False,
        )

    def parse_resume(self, file):
        return self._extract_text(file)

    def parse_jd(self, file):
        return self._extract_text(file)

    def _extract_text(self, file):
        if file.name.endswith(".pdf"):
            return self._extract_text_from_pdf(file)
        elif file.name.endswith(".docx"):
            return self._extract_text_from_docx(file)
        else:
            return ""

    def _extract_text_from_pdf(self, uploaded_file):
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            return "\n".join([page.get_text() for page in doc])

    def _extract_text_from_docx(self, uploaded_file):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    
    def parse_files(self, resume_file, jd_file):
        return self.parse_resume(resume_file), self.parse_jd(jd_file)

    # def parse_task(self, resume_file, jd_file):
    #     return Task(
    #         description="Extract text from the uploaded resume and job description files (PDF or DOCX format).",
    #         expected_output="Clean plain text from both the resume and job description.",
    #         agent=self.agent,
    #         async_execution=False,
    #         output=lambda: {
    #             "resume_text": self.parse_resume(resume_file),
    #             "jd_text": self.parse_jd(jd_file),
    #         }
    #     )



# This agent’s job is to:

# Accept resume and JD files (PDF or DOCX)
# Extract clean text using PyMuPDF and python-docx
# Pass the parsed content to other agents like analyzer and scorer