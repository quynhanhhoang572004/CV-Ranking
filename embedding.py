import json
from sentence_transformers import SentenceTransformer, util

# Load resume JSON
with open("Hung.json") as f:
    resume_data = json.load(f)

# Convert resume to plain text
resume_text = f"""
{resume_data['FullName']} is a candidate aiming to become an AI Engineer.
Education: {resume_data['Education']['Degree']} at {resume_data['Education']['Institution']} with GPA {resume_data['Education']['GPA']}.
Skills:
Tools: {', '.join(resume_data['TechnicalSkills']['Tools'])}
Languages: {', '.join(resume_data['TechnicalSkills']['ProgrammingLanguages'])}
Frameworks: {', '.join(resume_data['TechnicalSkills']['FrameworksLibraries'])}
Databases & Cloud: {', '.join(resume_data['TechnicalSkills']['DatabasesCloudServices'])}

Projects:
""" + "\n".join([f"{p['Name']} – {p['Role']}: " + " | ".join(p['Details']) for p in resume_data['Projects']])

# Sample job description
jd_text = """
We are hiring an AI Engineer with experience in Docker, Pytorch, and cloud databases.
Preferred: Experience with semantic retrieval and vector search systems like Pinecone or FAISS.
"""

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Embed resume and JD
resume_embedding = model.encode(resume_text, convert_to_tensor=True)
jd_embedding = model.encode(jd_text, convert_to_tensor=True)

# Compute similarity
score = util.cos_sim(resume_embedding, jd_embedding).item() * 100
print(f"Semantic Match Score: {score:.2f}")