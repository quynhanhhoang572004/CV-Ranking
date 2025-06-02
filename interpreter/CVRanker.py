
DEGREE_LEVELS = {"bachelor": 1, "master": 2, "PhD": 3}
EXPERIENCE_LEVELS = {"intern": 0, "fresher": 1, "junior": 2, "senior": 3}

class CVRanker:
    def __init__(self, jd, candidates):
        self.jd = jd
        self.candidates = candidates


    def scoreCV(self, candidate):
            score = 0
            max_score = 0
            fail = False
            # Extract candidate info
            skills = candidate["skills"]
            education = candidate["education"]
            experience_years = candidate["experience_years"]
            leaderships = candidate["leaderships"]
            projects = candidate["projects"]
            references = candidate["references"]

            # Extract JD info
            requirements = self.jd.get('requirements', {})
            preferences = self.jd.get("preferences", {})

            req_tech = requirements.get("technical skills", {})
            req_edu = requirements.get("education", {})
            req_gpa = float(req_edu.get("gpa", "GPA >= 0").split()[-1])
            req_lan = requirements.get("language", "")
            required_skills = [
                skill.lower()
                for skill in (
                    req_tech.get("tools", [])
                    + req_tech.get("programmingLanguages", [])
                    + req_tech.get("frameworksLibraries", [])
                    + req_tech.get("databasescloudServices", [])
                )
                if isinstance(skill, str)
            ]

            #SCORING RULES
            #Rule for Technical Skills
            for req_skill in required_skills:
                max_score += 2
                if req_skill not in skills:
                    fail = True
                else:
                    score += 2
                   

            #Rule for education
            max_score += 2
            if (
                req_edu.get("major", "").lower() != ""
                and req_edu.get("major", "").lower() != education["major"]
            ):
                fail = True
            else:
                score += 2
                # print("Pass education")

            #Rule for GPA
            max_score += 2
            if education["gpa"] < req_gpa:
                fail = True
            else:
                score += 2
                # print("Pass GPA")

            #Rule for Degree
            max_score += 2
            if DEGREE_LEVELS.get(education["degree"], 0) < DEGREE_LEVELS.get(
                req_edu["degree"].lower(), 0
            ):
                fail = True
            else:
                score += 2
                # print("Pass Degree")

            # Rule for experience
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

            return not fail, score / max_score 

    def rank_candidates(self):
        results = []
        for candidate in self.candidates:
            is_pass, percentage = self.scoreCV(
                candidate
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

        rankings = self.rank_candidates()

        for r in rankings:
            # print(f"{r['name']}: {r['score']} / {r['total']} ({r['percentage']}%)")
            print(f"{r['name']}: {r['percentage']}% Pass: {r['pass']}")
