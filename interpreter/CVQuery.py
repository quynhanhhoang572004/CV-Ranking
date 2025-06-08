from interpreter.CVExtractor import CVExtractor

class CVQuery:
    def __init__(self):
        self.extractor = CVExtractor("data")
        self.candidates = self.extractor.load_candidates()

    def run(self):
        results = []
        for candidate in self.candidates:
            cv_data = self.extractor.extractCV(candidate)
            if self.match_condition(cv_data, self.query):
                results.append(({
                    "filename": candidate["__filename__"],
                    "cv": candidate,
                }))
        return results

    def match_condition(self, cv_data, condition):

        field, value = condition
        field = field
        value = value.lower() if isinstance(value, str) else value
        if field == "name":
            return cv_data["full_name"].lower() == value
        
        if field == "degree":
            return cv_data["education"]["degree"] == value

        elif field == "major":
            return value in cv_data["education"]["major"]

        elif field == "gpa":
            # Assume value is a string like ">=3.2" or ">3.0"
            if isinstance(value, str) and value.startswith((">=", ">")):
                if value.startswith(">="):
                    threshold = float(value[2:])
                    return float(cv_data["education"]["gpa"]) >= threshold
                elif value.startswith(">"):
                    threshold = float(value[1:])
                    return float(cv_data["education"]["gpa"]) > threshold
            else:
                return float(cv_data["education"]["gpa"]) == float(value)

        elif field == "experience":
            # Assume value is like ">=2" or ">1"
            if isinstance(value, str) and value.startswith((">=", ">")):
                if value.startswith(">="):
                    threshold = int(value[2:])
                    return int(cv_data["experience_years"]) >= threshold
                elif value.startswith(">"):
                    threshold = int(value[1:])
                    return int(cv_data["experience_years"]) > threshold
            else:
                return int(cv_data["experience_years"]) == int(value)

        elif field == "tools":
            if isinstance(value, list):
            # Check if any tool in value is in the candidate's tools
                candidate_tools = [tool.lower() for tool in cv_data["skills"]["tools"]]
                
                # Check if at least one tool from value is in candidate_tools
                for tool in value:
                    if tool.lower() in candidate_tools:
                        return True
                return False
        
        elif field == "programmingLanguages":
            
            if isinstance(value, list):
                candidate_langs = [lang.lower() for lang in cv_data["skills"]["programmingLanguages"]]
                for lang in value:
                    if lang.lower() in candidate_langs:
                        return True
                return False
            else:
                return value.lower() in [lang.lower() for lang in cv_data["skills"]["programmingLanguages"]]
        elif field == "frameworksLibraries":
            
            if isinstance(value, list):
        
                candidate_frameworks = [lib.lower() for lib in cv_data["skills"]["frameworksLibraries"]]
                for lib in value:
                    if lib.lower() in candidate_frameworks:
                        return True
                return False
            else:
                return value.lower() in [lib.lower() for lib in cv_data["skills"]["frameworksLibraries"]]
        elif field == "databasescloudServices":
            if isinstance(value, list):
                candidate_databases = [db.lower() for db in cv_data["skills"]["databasesCloudServices"]]
                for db in value:
                    if db.lower() in candidate_databases:
                        return True
                return False
            else:
                return value.lower() in [db.lower() for db in cv_data["skills"]["databasesCloudServices"]]
        elif field == "language":
            return value in [lang.lower() for lang in cv_data.get("languages", [])]

        elif field == "activities":
            return value in [act.lower() for act in cv_data.get("activities", [])]

        else:
            return False

if __name__ == "__main__":
    #EXAMPLE QUERIES
    query = ("name", "Yolanda Nguyen")
     #query = ("tools", "vscode")  
    #query = ("programming languages", "python")
    #query = ("framework libraries", "react")
    #query = ("databases cloud services", "mongodb")

    #query = ("degree", "bachelor") 
    #query = ("major", "computer science")
    #query = ("gpa", ">= 3.0")

    #query = ("language", "english")

    #query = ("experience", ">= 5") 

    cv_query = CVQuery(query)
    results = cv_query.run()
    print(f"Looking for candidates with: {query}")
    if results:
        for cv in results:
            print(f"Found CV: {cv['__filename__']}")
            print(f"Education: {cv['education']}")
            print(f"Skills: {cv['skills']}")
            print(f"Experience Years: {cv['experience_years']}")
            print(f"Languages: {cv['languages']}")
            print("-" * 40)
    else:
        print("No matching CVs found.")