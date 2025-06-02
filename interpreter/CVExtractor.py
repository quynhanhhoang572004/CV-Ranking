
import os
import json

class CVExtractor():
    def __init__(self, candidate_dir):
        self.candidate_dir = candidate_dir
        self.candidates = []
        self.extracted_CVs = []
        self.load_candidates()

    def load_candidates(self):
        for filename in os.listdir(self.candidate_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.candidate_dir, filename), "r") as f:
                    profile = json.load(f)
                    profile["__filename__"] = filename
                    self.candidates.append(profile)
        return self.candidates
    
    def load_a_candidate(self, filename):
        with open(os.path.join(self.candidate_dir, filename), "r") as f:
            profile = json.load(f)
            profile["__filename__"] = filename
        return profile
    
    def extract_all_CVs(self):
        for candidate in self.candidates:
            cv = self.extractCV(candidate)
            cv["__filename__"] = candidate["__filename__"]
            self.extracted_CVs.append(cv)
        return self.extracted_CVs
         
    # Utitlity function
    def extractCV(self,candidate):
            skills = (
                candidate.get("TechnicalSkills", {}).get("ProgrammingLanguages", [])
                + candidate.get("TechnicalSkills", {}).get("FrameworksLibraries", [])
                + candidate.get("TechnicalSkills", {}).get("DatabasesCloudServices", [])
                + candidate.get("TechnicalSkills", {}).get("Tools", [])
                + list(candidate.get("TechnicalSkills", {}).get("Languages", {}).keys())
            )

            education = {
                "degree": candidate.get("Education", {})
                .get("Degree", "")
                .split("of")[0]
                .strip()
                .lower(),
                "major": candidate.get("Education", {})
                .get("Degree", "")
                .split(" in ")[-1]
                .strip()
                .lower(),
                "gpa": float(candidate.get("Education", {}).get("GPA", 0)),
            }

            experience_years = candidate.get("Experience", 0)
            leaderships = candidate.get("Leadership", [])
            projects = candidate.get("Projects", [])
            references = candidate.get("References", [])

            return {
                "skills": set([s.lower() for s in skills if isinstance(s, str)]),
                "education": education,
                "experience_years": experience_years,
                "leaderships": leaderships,
                "projects": projects,
                "references": references,
            }