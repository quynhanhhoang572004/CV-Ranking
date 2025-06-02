
from interpreter.JDProcessor import JDProcessor
from interpreter.CVRanker import CVRanker
from interpreter.CVExtractor import CVExtractor


if __name__ == "__main__":
    jd_file = "./tests/ExampleJD.txt"
    candidate_folder = "data"

    print(f"Parsing JD from {jd_file}...")
    jd_processor = JDProcessor(jd_file)
    parsed_jd = jd_processor.getParsedJD()
    all_extracted_cvs = CVExtractor(candidate_folder).extract_all_CVs()
    rankings = CVRanker(parsed_jd, all_extracted_cvs).run()
