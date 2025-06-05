DEGREE_LEVELS = {"bachelor": 1, "master": 2, "PhD": 3}
EXPERIENCE_LEVELS = {"intern": 0, "fresher": 1, "junior": 2, "senior": 3}

class CVScorer:
    def __init__(self, jd, candidate):
        self.jd = jd
        self.candidates = candidate
    

    def scoreCV(self, candidate):
        score = 0

        #GET ALL CANDIDATE INFO FOR SCORING
        cand_skills = (
                candidate.get("skills", {}).get("programmingLanguages", [])
                + candidate.get("skills", {}).get("frameworksLibraries", [])
                + candidate.get("skills", {}).get("databasesCloudServices", [])
                + candidate.get("skills", {}).get("tools", [])
        )
        cand_edu = candidate.get("education", {})
        cand_gpa = cand_edu.get("gpa", 0)
        cand_degree = cand_edu.get("degree", "").lower()
        cand_languages = candidate.get("languages", "")
        cand_exp_years = candidate.get("experience_years", 0)
        cand_activities = candidate.get("activities", [])
        cand_projects = candidate.get("projects", [])



        # GET ALL JD INFO FOR SCORING
        requirements = self.jd.get('requirements', {})
        preferences = self.jd.get("preferences", {})

        req_tech = requirements.get("technical skills", {})
        req_edu = requirements.get("education", {})
        req_gpa = float(req_edu.get("gpa", "GPA >= 0").split()[-1]) if req_edu.get("gpa") else 0
        req_degree = req_edu.get("degree", "").lower()
        req_languages = requirements.get("language", "")
        
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
        #Techincal skills
        if required_skills:
            matched_skills = sum(2 for req_skill in required_skills if req_skill in cand_skills)
            skill_percentage = matched_skills / len(required_skills)
            score += skill_percentage * 40
        else:
            score += 40  

   
        if req_edu.get("major", "").lower():
            if req_edu.get("major", "").lower() == cand_edu.get("major", "").lower():
                score += 10
            elif cand_edu.get("major", ""):  
                score += 5
        else:
            score += 8  

        cand_gpa = cand_edu.get("gpa", 0)
        if req_gpa > 0 and cand_gpa > 0:
            if cand_gpa >= req_gpa:
                score += 8
            else:
                gpa_ratio = cand_gpa / req_gpa
                score += max(gpa_ratio * 10, 2)
        else:
            score += 6

        
        if req_degree and hasattr(self, 'DEGREE_LEVELS'):
            req_level = DEGREE_LEVELS.get(req_degree, 0)
            candidate_level = DEGREE_LEVELS.get(candidate_degree, 0)
            
            if candidate_level >= req_level:
                score += 10 
            elif candidate_level > 0:
                
                score += max(candidate_level * 2, 3)
            else:
                score += 1  
        else:
            score += 10  

 
        req_exp_years = 0
        exp_requirement = requirements.get("experience", "0 years")
        if exp_requirement and isinstance(exp_requirement, str):
            try:
                req_exp_years = int(exp_requirement.split()[0])
            except:
                req_exp_years = 0
        
        if req_exp_years > 0:
            if int(cand_exp_years) >= req_exp_years:
                score += 15 
            else:
            
                exp_ratio = int(cand_exp_years) / req_exp_years
                score += max(exp_ratio * 15, 3)
        else:
            score += 15


        if req_languages:
            matched_languages = sum(2 for req_lang in req_languages if req_lang in cand_languages)
            lang_percentage = matched_languages / len(req_languages)
            score += lang_percentage * 5
        else:
            score += 5
     
        pref_skills = []
        if preferences:
            pref_skills = [
                skill.lower()
                for skill in (
                    preferences.get("programmingLanguages", [])
                    + preferences.get("tools", [])
                    + preferences.get("frameworksLibraries", [])
                    + preferences.get("databasescloudServices", [])
                )
                if isinstance(skill, str)
            ]
            
            pref_language = preferences.get("language", "")
            if pref_language and isinstance(pref_language, str):
                pref_skills.append(pref_language.lower())

        if pref_skills:
            matched_prefs = sum(1 for pref_skill in pref_skills if pref_skill in cand_skills)
            pref_percentage = matched_prefs / len(pref_skills)
            score += pref_percentage * 10
        else:
            score += 10  

        
     
        score += min(len(cand_activities), 5)
        
      
        score += min(len(cand_projects), 5)
 

        percentage = score / 100
        
       
        percentage = min(percentage, 1.0)

        passed = percentage >= 0.5
        
        return passed, percentage
