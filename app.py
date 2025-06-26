from dotenv import load_dotenv         # Load variables from .env
import streamlit as st                # Web app framework
from streamlit_extras import add_vertical_space as avs  # UI spacing helper
import google.generativeai as genai  # Gemini Pro API
import os                             # OS operations
import PyPDF2                         # PDF text extraction
from PIL import Image                 # Image handling


from openai import OpenAI




# Load API key
load_dotenv()
api_key = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))

# Initialize Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash')

# Response function
def get_gemini_response(prompt):
    response = model.generate_content(prompt)
    return response.text



# # Read the API key from environment variable
# api_key = st.secrets["OPENROUTER_API_KEY"]

# client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=api_key,  # Replace with your own key
# )

# def get_openrouter_response(prompt):
#     response = client.chat.completions.create(
#         extra_headers={
#             "HTTP-Referer": "http://localhost",  # Or your deployed URL
#             "X-Title": "Resume ATS Tracker"
#         },
#         model="deepseek/deepseek-r1-0528-qwen3-8b:free",
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )
#     return response.choices[0].message.content



def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)  # Load PDF
    text = ''
    for page_num in range(len(reader.pages)):  # Loop through all pages
        page = reader.pages[page_num]
        text += str(page.extract_text())  # Extract and append text
    return text






input_prompt="""
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect, Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD (Job Description) and meticulously identify any missing keywords with utmost accuracy. 
resume: {text}
description: {jd}

I want the response in the following structure:
The first line indicates the percentage match with the job description (JD).
The second line presents a list of missing keywords.
The third section provides a profile summary.

Mention the title for all the three sections.
While generating the response put some space to separate all the three sections
"""



## streamlit UI
st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

avs.add_vertical_space(4)

col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the Job Market with Confidence!")
    st.markdown("""
    <p style='text-align: justify;'>
    Introducing CareerCraft, an ATS-Optimized Resume Analyzer 🧠— your ultimate solution for optimizing job applications and accelerating career growth. Our innovative platform leverages advanced ATS technology to provide job seekers with valuable insights into their resumes' compatibility with job descriptions. From resume optimization and skill enhancement to career progression guidance, CareerCraft empowers users to stand out in today's competitive job market. Streamline your job application process, enhance your skills, and navigate your career path with confidence. Join CareerCraft today and unlock new opportunities for professional success!
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.image('https://cdn.dribbble.com/userupload/12500996/file/original-b458fe398a6d7f4e9999ce66ec856ff9.gif', use_container_width=True)

avs.add_vertical_space(10)


col1, col2 = st.columns([3, 2])
with col2:
    
    st.header("Wide Range of Offerings")
    st.write('ATS-Optimized Resume Analysis')
    st.write('Resume Optimization')
    st.write('Skill Enhancement')
    st.write('Career Progression Guidance')
    st.write('Tailored Profile Summaries')
    st.write('Streamlined Application Process')
    st.write('Personalized Recommendations')
    st.write('Efficient Career Navigation')
    st.write('Job Description Alignment')
    st.write('Recruiter-Friendly Formatting')
    st.write('Real-Time Resume Scoring')

with col1:
    st.image('https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDVsOTkwMzEwYzh5OWY2ZHZ6aWZqbGsyYjNtb3Zmcmwxb2tyMnk5eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SpopD7IQN2gK3qN4jS/giphy.gif', use_container_width=True)

avs.add_vertical_space(10)



col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("<h1 style='text-align: center;'>Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
    jd = st.text_area("Paste the Job Description")
    uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

    submit = st.button("Submit")

    if submit:
        if uploaded_file is not None:
            resume_text = input_pdf_text(uploaded_file)
            input_prompt = f"Resume:\n{resume_text}\n\nJob Description:\n{jd}\n\nSuggest improvements and analyze match."
            response = get_gemini_response(input_prompt)
            st.subheader("🔎 AI Analysis Result:")
            st.write(response)
        else:
            st.warning("⚠️ Please upload your resume.")

with col2:
    st.image('https://cdn.dribbble.com/userupload/10705722/file/original-9d3f87765ad640af12d79ed8a6278cbf.gif', use_container_width=True)

avs.add_vertical_space(10)


# --- FAQ Section ---
col1, col2 = st.columns([2, 3])

with col2:
    st.markdown("<h1 style='text-align: center;'>📘 FAQ</h1>", unsafe_allow_html=True)

    st.write("**Question:** How does CareerCraft analyze resumes and job descriptions?")
    st.write("**Answer:** CareerCraft uses advanced AI algorithms to analyze resumes and job descriptions, identifying key keywords and assessing compatibility between the two.")
    avs.add_vertical_space(1)
    st.write("**Question:** Can CareerCraft suggest improvements for my resume?")
    st.write("**Answer:** Yes, CareerCraft provides personalized recommendations to optimize your resume for specific job openings, including suggestions for missing keywords and alignment with desired job roles.")
    avs.add_vertical_space(1)
    st.write("**Question:** Is CareerCraft suitable for both entry-level and experienced professionals?")
    st.write("**Answer:** Absolutely! CareerCraft caters to job seekers at all career stages, offering tailored insights and guidance to enhance their resumes and advance their careers.")

with col1:
    avs.add_vertical_space(2)
    st.image('https://cdn.dribbble.com/userupload/42641062/file/original-6bdd2ba6ddda269a5fde6f5025d43296.gif', use_container_width=True)
