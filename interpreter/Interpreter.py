from antlr4 import FileStream, CommonTokenStream
from parse.JDLexer import JDLexer
from parse.JDParser import JDParser
from parse.JDValidator import JDValidator
from pprint import pprint
import os
import json


DEGREE_LEVELS = {"bachelor": 1, "master": 2, "PhD": 3}
EXPERIENCE_LEVELS = {"intern": 0, "fresher": 1, "junior": 2, "senior": 3}

class JDProcessor:
    def __init__(self, jd_file_path):
        self.jd_file_path = jd_file_path
        self.requirements = {}
        self.preferences = {}

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
        self.preferences = jd_output.get("preferences", {})


class CandidateMatcher:
    def __init__(self, jd_processor: JDProcessor, candidate_dir: str):
        self.requirements = jd_processor.requirements
        self.preferences = jd_processor.preferences
        self.candidate_dir = candidate_dir
        self.candidates = []

    def load_candidates(self):
        for filename in os.listdir(self.candidate_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.candidate_dir, filename), "r") as f:
                    profile = json.load(f)
                    profile["__filename__"] = filename
                    self.candidates.append(profile)

    def CVScorce(self, candidate, requirements, preferences):

        def extractCV(candidate):
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

            experience_years = EXPERIENCE_LEVELS.get(candidate.get("Level", "").lower(), 0)
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

        def score_CV(requirements, preferences, candidate):
            score = 0
            max_score = 0
            fail = False

            skills = candidate["skills"]
            education = candidate["education"]
            experience_years = candidate["experience_years"]
            leaderships = candidate["leaderships"]
            projects = candidate["projects"]
            references = candidate["references"]

            # Required technical skills
            req_tech = requirements.get("technical skills", {})
            req_lan = requirements.get("language", "")
            required_skills = [
                skill.lower()
                for skill in (
                    req_tech.get("tools", [])
                    + req_tech.get("programmingLanguages", [])
                    + req_tech.get("frameworksLibraries", [])
                    + req_tech.get("databasescloudServices", [])
                    + [req_lan]
                    if req_lan
                    else []
                )
                if isinstance(skill, str)
            ]

            for req_skill in required_skills:
                max_score += 2
                if req_skill not in skills:
                    fail = True
                else:
                    score += 2
                    # print(req_skill)

            # Required education
            req_edu = requirements.get("education", {})
            max_score += 2
            if (
                req_edu.get("major", "").lower() != ""
                and req_edu.get("major", "").lower() != education["major"]
            ):
                fail = True
            else:
                score += 2
                # print("Pass education")

            max_score += 2
            req_gpa = float(req_edu.get("gpa", "GPA >= 0").split()[-1])
            if education["gpa"] < req_gpa:
                fail = True
            else:
                score += 2
                # print("Pass GPA")

            max_score += 2
            if DEGREE_LEVELS.get(education["degree"], 0) < DEGREE_LEVELS.get(
                req_edu["degree"].lower(), 0
            ):
                fail = True
            else:
                score += 2
                # print("Pass Degree")

            # Required experience
            max_score += 2
            req_exp_years = int(requirements.get("experience", "0 years").split()[0])
            if experience_years < req_exp_years:
                fail = True
            else:
                score += 2
                # print("Pass exp")

            # Preferences
            pref_skills = [
                skill.lower()
                for skill in (
                    preferences.get("programmingLanguages", [])
                    + preferences.get("tools", [])
                    + preferences.get("frameworksLibraries", [])
                    + preferences.get("databasescloudServices", [])
                    + preferences.get("language", "")
                    if preferences.get("langugage", "")
                    else []
                )
                if isinstance(skill, str)
            ]
            for pref_skill in pref_skills:
                max_score += 1
                if pref_skill in skills:
                    score += 1

            pref_gpa = float(req_edu.get("gpa", "").split()[-1])
            if pref_gpa:
                max_score += 1
                if education["gpa"] >= pref_gpa:
                    score += 1

            pref_degree = preferences.get("degree", "").lower()
            if pref_degree:
                max_score += 1
                if DEGREE_LEVELS.get(education["degree"], 0) >= DEGREE_LEVELS.get(
                    pref_degree, 0
                ):
                    score += 1

            pref_exp_years = int(requirements.get("experience", "0").split()[0])
            if pref_exp_years:
                max_score += 1
                if experience_years >= req_exp_years:
                    score += 1

            # leaderships, projects, references
            max_score_leaderships = 2
            max_score_projects = 2
            max_score_references = 2

            max_score += (
                max_score_leaderships + max_score_projects + max_score_references
            )

            score += min(len(leaderships) * 1, max_score_leaderships)
            score += min(len(projects) * 1, max_score_projects)
            score += min(len(references) * 1, max_score_references)

            # matched_skills = sum(
            #     1 for skill in required_skills if skill.lower() in skills
            # )
            # # max_skills = len(required_skills)
            # # skill_score = (matched_skills / max_skills) * 4 if max_skills > 0 else 0
            # score += matched_skills

            # extra_required = [
            #     requirements.get("language", ""),
            #     requirements.get("activities", ""),
            #     requirements.get("references", ""),
            # ]
            # for item in extra_required:
            #     if item and item.lower() not in skills:
            #         score -= 1

            # edu = requirements.get("education", {})
            # if candidate.get("education.degree", "") == edu.get("degree", "").lower():
            #     score += 2

            # if candidate.get("education.major", "") == edu.get("major", "").lower():
            #     score += 2

            # gpa_required = float(edu.get("gpa", "GPA >= 0").split()[-1])
            # if candidate.get("education.gpa", 0) >= gpa_required:
            #     score += 2

            # required_experience = int(
            #     requirements.get("experience", "0 years").split()[0]
            # )
            # if candidate.get("experience.years", 0) >= required_experience:
            #     score += 2

            return fail, score, max_score

        candidate_structured = extractCV(candidate)
        fail, score, max_score = score_CV(
            requirements, preferences, candidate_structured
        )

        return not fail, score / max_score

    def rank_candidates(self):
        results = []
        for candidate in self.candidates:
            is_pass, percentage = self.CVScorce(
                candidate, self.requirements, self.preferences
            )
            results.append(
                {
                    "name": candidate.get("PersonalInfo", {}).get(
                        "Name", candidate.get("__filename__", "Unknown")
                    ),
                    "contact": candidate.get("Contact", {}),
                    "pass": is_pass,
                    "percentage": round(percentage * 100, 2),
                }
            )
        return sorted(results, key=lambda x: (not x["pass"], -x["percentage"]))

    def run(self):

        self.load_candidates()
        rankings = self.rank_candidates()

        for r in rankings:
            # print(f"{r['name']}: {r['score']} / {r['total']} ({r['percentage']}%)")
            print(f"{r['name']}: {r['percentage']}% Pass: {r['pass']}")


if __name__ == "__main__":
    jd_file = "./tests/ExampleJD.txt"
    candidate_folder = "data"

    print(f"Parsing JD from {jd_file}...")
    jd_processor = JDProcessor(jd_file)
    jd_processor.parse()

    matcher = CandidateMatcher(jd_processor, candidate_folder)
    matcher.run()
