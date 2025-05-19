from antlr4 import FileStream, CommonTokenStream
from parse.JDLexer import JDLexer
from parse.JDParser import JDParser
from parse.JDValidator import JDValidator
from pprint import pprint
import os
import json

class JDProcessor:
    def __init__(self, jd_file_path):
        self.jd_file_path = jd_file_path
        self.requirements = {}

    def parse(self):
        input_stream = FileStream(self.jd_file_path)
        lexer = JDLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = JDParser(tokens)
        tree = parser.program()

        validator = JDValidator()
        jd_output = validator.visit(tree)

        print("Validator result:")
        pprint(jd_output, indent=2, width=100, sort_dicts=False)
        self.requirements = jd_output.get("requirements", {})

class CandidateMatcher:
    def __init__(self, jd_processor: JDProcessor, candidate_dir: str):
        self.requirements = jd_processor.requirements
        self.candidate_dir = candidate_dir
        self.candidates = []

    def load_candidates(self):
        for filename in os.listdir(self.candidate_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.candidate_dir, filename), "r") as f:
                    profile = json.load(f)
                    profile["__filename__"] = filename
                    self.candidates.append(profile)

    def CVScorce(self, candidate, requirements):

        def extractCV(candidate):
            skills = (
                candidate.get("TechnicalSkills", {}).get("ProgrammingLanguages", []) +
                candidate.get("TechnicalSkills", {}).get("FrameworksLibraries", []) +
                candidate.get("TechnicalSkills", {}).get("DatabasesCloudServices", []) +
                candidate.get("TechnicalSkills", {}).get("Tools", [])
            )

            degree = candidate.get("Education", {}).get("Degree", "")
            major = candidate.get("Education", {}).get("Degree", "").split(" in ")[-1].strip().lower()
            gpa = float(candidate.get("Education", {}).get("GPA", 0))

            experience_years = candidate.get("Experience", {}).get("Years", 0)

        
            extra_values = [
                candidate.get("Language", ""),
                candidate.get("Activities", "")
            ]

           
            references = candidate.get("References", [])
            for ref in references:
                extra_values.extend([
                    ref.get("Name", ""),
                    ref.get("Institution", ""),
                    ref.get("Email", "")
                ])

            return {
                "skills": set([s.lower() for s in skills + extra_values if isinstance(s, str)]),
                "education.degree": degree.lower(),
                "education.major": major,
                "education.gpa": gpa,
                "experience.years": experience_years
            }

        def score_CV(requirements, candidate):
            score = 0
            total = 10  
            skills = candidate["skills"]

            req_tech = requirements.get("technical skills", {})
            required_skills = (
                req_tech.get("tools", []) +
                req_tech.get("programmingLanguages", []) +
                req_tech.get("frameworksLibraries", []) +
                req_tech.get("databasescloudServices", [])
            )

          
            matched_skills = sum(1 for skill in required_skills if skill.lower() in skills)
            max_skills = len(required_skills)
            skill_score = (matched_skills / max_skills) * 4 if max_skills > 0 else 0
            score += skill_score


            extra_required = [
                requirements.get("language", ""),
                requirements.get("activities", ""),
                requirements.get("references", "")
            ]
            for item in extra_required:
                if item and item.lower() not in skills:
                    score -=1

          
            edu = requirements.get("education", {})
            if candidate.get("education.degree", "") == edu.get("degree", "").lower():
                score += 2
            if candidate.get("education.major", "") == edu.get("major", "").lower():
                score += 2

            gpa_required = float(edu.get("gpa", "GPA >= 0").split()[-1])
            if candidate.get("education.gpa", 0) >= gpa_required:
                score += 2

            required_experience = int(requirements.get("experience", "0 years").split()[0])
            if candidate.get("experience.years", 0) >= required_experience:
                score += 2

            return score

        candidate_structured = extractCV(candidate)
        final_score = score_CV(requirements, candidate_structured)

        return round(final_score,2), 10

    def rank_candidates(self):
        results = []
        for candidate in self.candidates:
            score, total = self.CVScorce(candidate, self.requirements)
            results.append({
                "name": candidate.get("PersonalInfo", {}).get("Name", candidate.get("__filename__", "Unknown")),
                "score": score,
                "total": total,
                "percentage": round((score / total) * 100, 2) if total > 0 and score >= 0 else 0
            })
        return sorted(results, key=lambda x: x["score"], reverse=True)

    def run(self):
       
        self.load_candidates()
        rankings = self.rank_candidates()

        print("\n--- Candidate Rankings ---")
        for r in rankings:
            print(f"{r['name']}: {r['score']} / {r['total']} ({r['percentage']}%)")


if __name__ == "__main__":
    jd_file = "./tests/ExampleJD.txt"
    candidate_folder = "data"

    print(f"Parsing JD from {jd_file}...")
    jd_processor = JDProcessor(jd_file)
    jd_processor.parse()

    matcher = CandidateMatcher(jd_processor, candidate_folder)
    matcher.run()
