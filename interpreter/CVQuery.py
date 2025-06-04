from CVExtractor import CVExtractor

class CVQuery:
    def __init__(self, query):
        self.query = query
    
    def execute(self, candidates):
        all_candidates = CVExtractor(candidates).extract_all_CVs()
        
