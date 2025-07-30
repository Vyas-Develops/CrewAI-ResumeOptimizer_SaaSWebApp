import streamlit as st
from crews.resume_crew import ResumeOptimizerCrew

st.set_page_config(page_title="Agentic Resume Optimizer", layout="centered")
st.title("Resume Optimizer - Powered by CrewAI Agents")

# Upload section
st.header("Upload Your Files")
resume_file = st.file_uploader("Upload your Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_file = st.file_uploader("Upload Job Description (PDF or DOCX)", type=["pdf", "docx"])

# Proceed if both files are uploaded
if resume_file and jd_file:
    st.success("Files uploaded successfully ✅")

    if st.button("Run Resume Optimizer"):
        with st.spinner("🤖 CrewAI MultiAgents working on your resume..."):

            # Run the CrewAI system
            try:
                crew = ResumeOptimizerCrew()
                report = crew.run(resume_file, jd_file)

                st.subheader("📋 Final Report")
                st.markdown(report)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# Optional footer
st.markdown("---")
st.caption("Built with CrewAI + OpenAI by VK")
