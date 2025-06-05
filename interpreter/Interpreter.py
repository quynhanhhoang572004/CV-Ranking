
from interpreter.CVScorer import CVScorer
from interpreter.CVExtractor import CVExtractor
from interpreter.CVQuery import CVQuery

class Interpreter:
    def __init__(self, candidate_folder="data"):
        self.cv_extractor = CVExtractor(candidate_folder)
        self.all_candidates = self.cv_extractor.load_candidates()
        self.parsed_jd = None
        self.rankings = {}


    def run_command(self, command_dict: dict):
        if command_dict["command"] == "jd":
            self.parsed_jd = command_dict
            result = self.rank_candidates()
            return result
        elif command_dict["command"] == "show_cv_with":
            if not self.parsed_jd:
                raise ValueError("You must load a JD before running query commands.")
            if not self.rankings:
                self.rank_candidates()

            result = self.show_cv_with(command_dict["condition"])
            return result
            
        else:
            raise ValueError(f"Unknown command: {command_dict['command']}")
        
       


    #Tra ve all rows voi moi row la filename, parsed_cv, pass/fail, percentage, rank
    def rank_candidates(self):
        print("ALL CANDIDATES RANKED")
        results = []  
        for candidate in self.all_candidates:
            extracted_cv = self.cv_extractor.extractCV(candidate)
            is_pass, percentage = CVScorer(self.parsed_jd, extracted_cv).scoreCV(extracted_cv)
            results.append({
                "filename": candidate["__filename__"],
                "cv": candidate,
                "pass": is_pass,
                "percentage": round(percentage * 100, 2),
            })

        sorted_results = sorted(results, key=lambda x: (not x["pass"], -x["percentage"]))
        for i, result in enumerate(sorted_results, start=1):
            result["rank"] = i

        self.rankings = {res["filename"]: res for res in sorted_results}
        return sorted_results
    
        
    #Tra ve candidate + rank theo ten file
    def get_candidate_by_filename(self, filename):
        return self.rankings.get(filename, None)

    def show_top(self, n):
        if not self.rankings:
            self.rank_candidates()
        print(f"Showing top {n} candidates:")
        return sorted(self.rankings.values(), key=lambda r: r["rank"])[:n]

    # Example usage in show_cv_with condition <- CHUA HOAN THIEN
    def show_cv_with(self, condition: tuple):
        if not self.rankings:
            self.rank_candidates()
        print("QUERIED CANDIDATES FOR CONDITION:", condition)
        matches = []
        for candidate_data in self.rankings.values():
            cv = candidate_data["cv"]
            extracted_cv = self.cv_extractor.extractCV(cv)
            if CVQuery().match_condition(extracted_cv, condition):
                matches.append({
                    "filename": candidate_data["filename"],
                    "cv": candidate_data["cv"],
                    "pass": candidate_data["pass"],
                    "percentage": candidate_data["percentage"],
                    "rank": candidate_data["rank"]
                })
        print(matches)
        return matches

