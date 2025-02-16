import faiss
import numpy as np
from embeddings import generate_embeddings



dimension = 384
index = faiss.IndexFlatL2(dimension)
resume_db = {}

def store_resume_embedding(filename, vector, text):
    global resume_db
    index.add(np.array([vector]))
    resume_db[len(resume_db)] = {"filename": filename, "text": text}

def search_similar_resumes(job_description):
    job_vector = generate_embeddings(job_description)
    D, I = index.search(np.array([job_vector]), k=3)
    return [resume_db[i]["text"] for i in I[0] if i in resume_db]
