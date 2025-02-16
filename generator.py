import google.generativeai as genai

# Configure Gemini API
# genai.configure(api_key="AIzaSyCQkmt7LZKp_BHTd05DtIkJEFQD3V1Usqw")
API_KEY = st.secrets["GOOGLE_API_KEY"]

# Initialize Gemini model
llm = genai.GenerativeModel("gemini-pro")

def generate_resume(name, job_desc, similar_resumes):
    prompt = f"Generate a professional resume for {name} applying for:\n{job_desc}\n\nReference these resumes:\n{similar_resumes}"
    response = llm.generate_content(prompt)
    return response.text

def generate_cover_letter(name, job_desc, similar_resumes):
    prompt = f"Write a tailored cover letter for {name} based on:\n{job_desc}\n\nReference resumes:\n{similar_resumes}"
    response = llm.generate_content(prompt)
    return response.text

