from antlr4 import FileStream, CommonTokenStream
from parse.HireXLexer import HireXLexer
from parse.HireXParser import HireXParser
from parse.HireXProcessor import HireXProcessor

from interpreter.JDProcessor import JDProcessor
from interpreter.CVRanker import CVRanker
from interpreter.CVExtractor import CVExtractor
from interpreter.CVQuery import CVQuery

class Interpreter:
    def __init__(self, candidate_folder="data", inputFile="./tests/ShowConditional.txt", jd_file="./tests/qanhtest.txt"):
        self.cv_extractor = CVExtractor(candidate_folder)
        #CV HANDLING
        all_candidates = self.cv_extractor.load_candidates()

        input_stream = FileStream(inputFile)
        lexer = HireXLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = HireXParser(tokens)
        tree = parser.program()
        processor = HireXProcessor()
        self.input_tree = processor.visit(tree)

        if self.input_tree["command"] == "jd":
            print("JD Parsed Successfully:")
            print(self.rank_candidates())
        elif self.input_tree["command"] == "show_cv_with":
            print(self.show_cv_with(self.input_tree["condition"]))



    #Tra ve all rows voi moi row la filename, parsed_cv, pass/fail, percentage, rank
    def rank_candidates(self):
        results = []  
        for candidate in self.all_candidates:
            extracted_cv = self.cv_extractor.extractCV(candidate)
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
    def show_cv_with(self, candidate_folder, condition: tuple):
        print(f"Showing CVs with condition: {condition}")
        filtered_cv = CVQuery(candidate_folder, condition).run()
        return filtered_cv.pop(1)

    def run(self):
        if self.input_tree["command"] == "jd":
            print("JD Parsed Successfully:")
            print(self.rank_candidates())
        elif self.result["command"] == "show_cv_with":
            print(self.show_cv_with(self.result["condition"]))
        
if __name__ == "__main__":
    interpreter = Interpreter()
    # interpreter.run()
    # sorted_results = interpreter.rank_candidates()
    # print(sorted_results)
    # # Print the shortened results
    # for res in sorted_results:
    #     print(f"[Rank {res['rank']}] {res['cv'].get('FullName')}: {res['percentage']}% Pass: {res['pass']}")

    # # Get ranking of 1 candidate by filename
    # print("Candidate ranking by filename:")
    # print(interpreter.get_candidate_by_filename("Carly_Barnes.json"))  

    # print("SHOW TOP")
    # print(interpreter.show_top(3))  

