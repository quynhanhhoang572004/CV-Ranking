import json

with open("Hung.json") as f:
    resume_data = json.load(f)

resume_text = f"""
{resume_data['FullName']} is a candidate aiming to become an AI Engineer.
Education: {resume_data['Education']['Degree']} at {resume_data['Education']['Institution']} with GPA {resume_data['Education']['GPA']}.

Skills:
Tools: {', '.join(resume_data['TechnicalSkills']['Tools'])}
Languages: {', '.join(resume_data['TechnicalSkills']['ProgrammingLanguages'])}
Frameworks: {', '.join(resume_data['TechnicalSkills']['FrameworksLibraries'])}
Databases & Cloud: {', '.join(resume_data['TechnicalSkills']['DatabasesCloudServices'])}

Projects:
""" + "\n".join([f"{p['Name']} – {p['Role']}: " + " | ".join(p['Details']) for p in resume_data['Projects']])
