import json

with open("Hung.json", "r") as f:
    cv_data = json.load(f)


def extract_cv_info(cv_json):
    # Flatten and normalize key fields
    skills = (
        cv_json["TechnicalSkills"].get("ProgrammingLanguages", []) +
        cv_json["TechnicalSkills"].get("FrameworksLibraries", []) +
        cv_json["TechnicalSkills"].get("DatabasesCloudServices", []) +
        cv_json["TechnicalSkills"].get("Tools", [])
    )

    degree = cv_json.get("Education", {}).get("Degree", "")
    # Stub experience: assuming 2 years for demo (you can parse from Projects or Duration)
    experience_years = 2  

    return {
        "skills": set([s.lower() for s in skills]),
        "experience.years": experience_years,
        "education.degree": degree
    }


def evaluate_rules(rules, candidate_info):
    score = 0
    for rule in rules:
        if rule.type == "require":
            if rule.details["skill"].lower() not in candidate_info["skills"]:
                return -999  # Hard fail if required skill missing
        elif rule.type == "prefer":
            if rule.details["skill"].lower() in candidate_info["skills"]:
                score += rule.details["weight"]
        elif rule.type == "score":
            field, op, val = rule.details["condition"]
            actual = candidate_info.get(field)
            if isinstance(val, str):
                matched = eval(f'"{actual}" {op} "{val}"')
            else:
                matched = eval(f"{actual} {op} {val}")
            if matched:
                score += rule.details["delta"]
    return score


from parse_dsl import parse_dsl  # If in another file

# 1. Load DSL
dsl_code = '''
match {
  require skill "Python"
  prefer skill "Machine Learning" weight 2
  if experience.years >= 3 then score +5
  if education.degree == "Bsc" then score +10
}
'''
rules = parse_dsl(dsl_code)

# 2. Load CV
with open("Hung.json") as f:
    cv = json.load(f)

# 3. Match
info = extract_cv_info(cv)
score = evaluate_rules(rules, info)

print("Match Score:", score)
