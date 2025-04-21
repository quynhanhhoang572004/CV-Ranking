from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

# ✅ Load SentenceTransformer model (miniLM is fast and effective)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# 📝 Job Description input
jd = """
We are hiring a backend developer with at least 3 years of experience, strong Python skills, 
and some exposure to machine learning. A PhD is a big plus.
"""


with open("Hung.json", "r") as f:
    cv = json.load(f)

# 📄 Flatten CV content into a single text blob
cv_text = " ".join([
    cv.get("Profile", ""),
    cv["Education"].get("Degree", ""),
    " ".join(cv["TechnicalSkills"].get("ProgrammingLanguages", [])),
    " ".join(cv["TechnicalSkills"].get("FrameworksLibraries", [])),
    " ".join(cv["TechnicalSkills"].get("DatabasesCloudServices", [])),
    " ".join(cv["TechnicalSkills"].get("Tools", []))
])

#  Get embeddings
embeddings = model.encode([jd, cv_text])

# 📏 Compute cosine similarity
similarity_score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]

print(f"\n🔍 Cosine Similarity between JD and CV: {similarity_score:.4f}")
