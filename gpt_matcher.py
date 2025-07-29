from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_match_score(resume_text, jd_text):
    prompt = f"""
You are an ATS resume evaluator.
Compare the resume below against the job description and do the following:
1. Give a relevance score out of 100
2. List 3 strengths
3. List 3 improvements or missing areas

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an expert ATS evaluator."},
            {"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return (completion.choices[0].message.content)

#     https://platform.openai.com/docs/guides/text?api-mode=chat - used new sdk

#     Role	    Who is it?	            What it does
#     system	    Instructions to GPT	    Sets the behavior or tone
#     user	    You (the user)	        Asks the actual question/task
#     assistant	GPT (previous reply)	Adds memory of past GPT responses

#     | Temperature | Behavior                       | Use Case Example                           |
# | ----------- | ------------------------------ | ------------------------------------------ |
# | `0`         | 🔒 Fully deterministic         | Fact checking, scoring, structured replies |
# | `0.2`       | 🔍 Mostly focused              | Your resume analyzer – accurate + concise  |
# | `0.7`       | ✍️ Balanced creative           | Content writing, brainstorming             |
# | `1.0`+      | 🎨 Very creative/unpredictable | Poetry, story generation, wild ideas       |
# | `>1.3`      | ⚠️ May go off-topic            | Avoid for serious applications             |
