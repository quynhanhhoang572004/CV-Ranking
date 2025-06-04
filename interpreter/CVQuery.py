from interpreter.CVExtractor import CVExtractor
import os

class CVQuery:
    def __init__(self, query):
        extractor = CVExtractor("data")
        candidates = extractor.load_candidates()
        self.all_cv_data = extractor.extract_all_CVs()
        self.query = query

    def run(self):
        results = []
        for cv_data in self.all_cv_data:
            if self.match_condition(cv_data, self.query):
                results.append(cv_data)
        return results

    def match_condition(self, cv_data, condition):
    
        field, value = condition
        field = field.lower()
        value = value.lower() if isinstance(value, str) else value

        if field == "degree":
            return cv_data["education"]["degree"] == value

        elif field == "major":
            return value in cv_data["education"]["major"]

        elif field == "gpa":
            # Assume value is a string like ">=3.2" or ">3.0"
            if isinstance(value, str) and value.startswith((">=", ">")):
                if value.startswith(">="):
                    threshold = float(value[2:])
                    return cv_data["education"]["gpa"] >= threshold
                elif value.startswith(">"):
                    threshold = float(value[1:])
                    return cv_data["education"]["gpa"] > threshold
            else:
                return cv_data["education"]["gpa"] == float(value)

        elif field == "experience":
            # Assume value is like ">=2" or ">1"
            if isinstance(value, str) and value.startswith((">=", ">")):
                if value.startswith(">="):
                    threshold = int(value[2:])
                    return cv_data["experience_years"] >= threshold
                elif value.startswith(">"):
                    threshold = int(value[1:])
                    return cv_data["experience_years"] > threshold
            else:
                return cv_data["experience_years"] == int(value)

        elif field == "skills":
            return value in cv_data["skills"]

        elif field == "language":
            return value in [lang.lower() for lang in cv_data.get("languages", [])]

        elif field == "activities":
            return value in [act.lower() for act in cv_data.get("activities", [])]

        else:
            return False

if __name__ == "__main__":
    # query = ("gpa", ">= 3.0") 

    query = ("skills", "Git")  
    cv_query = CVQuery(query)
    results = cv_query.run()
    print(f"Looking for candidates with: {query}")
    if results:
        for cv in results:
            print(f"Found CV: {cv['__filename__']}")
            print(f"Education: {cv['education']}")
            print(f"Skills: {cv['skills']}")
            print(f"Experience Years: {cv['experience_years']}")
            print("-" * 40)
    else:
        print("No matching CVs found.")