DEGREE_LEVELS = {"bachelor": 1, "master": 2, "PhD": 3}
EXPERIENCE_LEVELS = {"intern": 0, "fresher": 1, "junior": 2, "senior": 3}

class CVScorer:
    def __init__(self, jd, candidate):
        self.jd = jd
        self.candidates = candidate
    

    def scoreCV(self, candidate):
        score = 0
        skills = [skill.lower() for skill in candidate.get("skills", [])]
        education = candidate.get("education", {})
        experience_years = candidate.get("experience_years", 0)
        leaderships = candidate.get("leaderships", [])
        projects = candidate.get("projects", [])
        references = candidate.get("references", [])

        requirements = self.jd.get('requirements', {})
        preferences = self.jd.get("preferences", {})

        req_tech = requirements.get("technical skills", {})
        req_edu = requirements.get("education", {})
        req_gpa = float(req_edu.get("gpa", "GPA >= 0").split()[-1]) if req_edu.get("gpa") else 0
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

    
        if required_skills:
            matched_skills = sum(2 for req_skill in required_skills if req_skill in skills)
            skill_percentage = matched_skills / len(required_skills)
            score += skill_percentage * 40
        else:
            score += 40  

   
        if req_edu.get("major", "").lower():
            if req_edu.get("major", "").lower() == education.get("major", "").lower():
                score += 10
            elif education.get("major", ""):  
                score += 5
        else:
            score += 8  

     
        candidate_gpa = education.get("gpa", 0)
        if req_gpa > 0 and candidate_gpa > 0:
            if candidate_gpa >= req_gpa:
                score += 8 
            else:
                
                gpa_ratio = candidate_gpa / req_gpa
                score += max(gpa_ratio * 10, 2)
        else:
            score += 6 

    
        req_degree = req_edu.get("degree", "").lower()
        candidate_degree = education.get("degree", "").lower()
        
        if req_degree and hasattr(self, 'DEGREE_LEVELS'):
            req_level = self.DEGREE_LEVELS.get(req_degree, 0)
            candidate_level = self.DEGREE_LEVELS.get(candidate_degree, 0)
            
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
            if int(experience_years) >= req_exp_years:
                score += 15 
            else:
            
                exp_ratio = int(experience_years) / req_exp_years
                score += max(exp_ratio * 15, 3)
        else:
            score += 15

     
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
            matched_prefs = sum(1 for pref_skill in pref_skills if pref_skill in skills)
            pref_percentage = matched_prefs / len(pref_skills)
            score += pref_percentage * 10
        else:
            score += 10  

        
     
        score += min(len(leaderships), 5)
        
      
        score += min(len(projects), 5)
        
    
        score += min(len(references), 5)

        percentage = score / 100
        
       
        percentage = min(percentage, 1.0)

        passed = percentage >= 0.5
        
        return passed, percentage
