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
        field = field.lower()
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
            return value in cv_data["skills"]["tools"]
        elif field == "programming languages":
            return value in cv_data["skills"]["programmingLanguages"]
        elif field == "framework libraries":
            return value in cv_data["skills"]["frameworksLibraries"]
        elif field == "databases cloud services":
            return value in cv_data["skills"]["databasesCloudServices"]
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