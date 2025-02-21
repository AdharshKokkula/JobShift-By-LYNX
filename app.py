import streamlit as st
from embeddings import generate_embeddings
from resume_generator import generate_resume, generate_cover_letter
from parser import extract_text_from_pdf
from vector_store import store_resume_embedding, search_similar_resumes
import pdfkit

# Streamlit App
st.title("JobSwift: Accelerating Careers with AI-Powered Applications")
st.title("Resume and Cover Letter Generator")

# Upload Resume File
uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
if uploaded_file:
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(uploaded_file.read())
    # Generate embeddings for the uploaded resume
    vector = generate_embeddings(text)
    # Store the resume embedding for future searches
    store_resume_embedding(uploaded_file.name, vector, text)
    st.success("Resume uploaded successfully!")

# Form to generate documents
with st.form("generate_documents"):
    name = st.text_input("Your Name")
    job_description = st.text_area("Job Description")
    submit_button = st.form_submit_button("Generate Resume and Cover Letter")

if submit_button:
    if not name or not job_description:
        st.error("Please fill in both fields.")
    else:
        # Search for similar resumes based on job description
        similar_resumes = search_similar_resumes(job_description)
        # Generate resume and cover letter
        resume_html = generate_resume(name, job_description, similar_resumes)
        cover_letter_html = generate_cover_letter(name, job_description, similar_resumes)
        
        # Convert HTML to PDF
        resume_pdf = pdfkit.from_string(resume_html, False)
        cover_letter_pdf = pdfkit.from_string(cover_letter_html, False)
        
        # Display the generated resume and cover letter
        st.subheader("Generated Resume")
        st.markdown(resume_html, unsafe_allow_html=True)
        
        # Add a horizontal line to separate the resume and cover letter
        st.markdown("<hr>", unsafe_allow_html=True)
        
        st.subheader("Generated Cover Letter")
        st.markdown(cover_letter_html, unsafe_allow_html=True)
        
        # Add download buttons for the resume and cover letter
        st.download_button(
            label="Download Resume",
            data=resume_pdf,
            file_name="resume.pdf",
            mime="application/pdf"
        )
        
        st.download_button(
            label="Download Cover Letter",
            data=cover_letter_pdf,
            file_name="cover_letter.pdf",
            mime="application/pdf"
        )