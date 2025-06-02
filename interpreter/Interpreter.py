from antlr4 import FileStream, CommonTokenStream
from parse.HireLexer import HireLexer
from parse.HireParser import HireParser
from parse.HireProcessor import HireProcessor

from interpreter.JDProcessor import JDProcessor
from interpreter.CVScorer import CVRanker
from interpreter.CVExtractor import CVExtractor

class Interpreter:
    def __init__(self, candidate_folder="data", inputFile="./tests/ShowTop.txt", jd_file="./tests/ExampleJD.txt"):
        self.candidate_folder = candidate_folder

        input_stream = FileStream(inputFile)
        lexer = HireLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = HireParser(tokens)
        tree = parser.program()

        self.result = HireProcessor().visit(tree)
        
        # Parse JD
        self.parsed_jd = JDProcessor(jd_file).getParsedJD()
        self.rankings = {}

    #Tra ve all rows voi moi row la filename, parsed_cv, pass/fail, percentage, rank
    def rank_candidates(self):
        results = []  #
        all_candidates = CVExtractor(self.candidate_folder).load_candidates()

        for candidate in all_candidates:
            extracted_cv = CVExtractor(self.candidate_folder).extractCV(candidate)
            is_pass, percentage = CVRanker(self.parsed_jd, extracted_cv).scoreCV(extracted_cv)
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
        print(f"Showing top {n} candidates:")
        ranked_candidates = self.rank_candidates() 
        return sorted(ranked_candidates, key=lambda r: r["rank"])[:n]


    # Example usage in show_cv_with condition <- CHUA HOAN THIEN
    def show_cv_with(self, condition: tuple):
        def lower_keys(d):
            return {k.lower(): v for k, v in d.items()}
        if not self.rankings:
            self.rank_candidates()

        key, val = condition
        key = key.lower()
        val = val.lower() if isinstance(val, str) else val

        filtered = []
        for res in self.rankings.values():
            cv_lower = lower_keys(res["cv"])
            cv_val = cv_lower.get(key)
            if isinstance(cv_val, str):
                cv_val = cv_val.lower()
            if cv_val == val:
                filtered.append(res)
        return filtered

    
    def run(self, inputFile):
        if self.result["command"] == "show_top":
            print(self.result)
            print(interpreter.show_top(self.result["number"]))
        elif self.result["command"] == "jd":
            print(interpreter.rank_candidates())
        elif self.result["command"] == "show_cv_with":
            print(interpreter.show_cv_with(self.result["condition"]))
        
if __name__ == "__main__":
    interpreter = Interpreter()
    
    sorted_results = interpreter.rank_candidates()
    print(sorted_results)
    # Print the shortened results
    # for res in sorted_results:
    #     print(f"[Rank {res['rank']}] {res['cv'].get('FullName')}: {res['percentage']}% Pass: {res['pass']}")

    # Get ranking of 1 candidate by filename
    print("Candidate ranking by filename:")
    print(interpreter.get_candidate_by_filename("Carly_Barnes.json"))  

    print("SHOW TOP")
    print(interpreter.show_top(3))  

