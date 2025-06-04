import streamlit as st
from components.jd_input import jd_input
from components.config_output import config_output
from components.output import show_output
from interpreter.Interpreter import Interpreter

st.set_page_config(layout="wide")
st.title("🧩 JD Prompt Builder + CV Matcher")

def format_jd_data(data):
    req = data["REQUIREMENTS"]
    pref = data["PREFERENCES"]

    return f"""REQUIREMENTS {{
  position: {req['position']}
  level: {req['level']}
  stack {{
    tools: {req['tools']}
    programming languages: {req['languages']}
    framework libraries: {req['frameworks']}
    databases cloud services: {req['cloud']}
  }}
  education {{
    major: {req['field']}
    degree: {req['degree']}
    gpa: {req['gpa']}
  }}
  experience: {req['experience']}
  language: {req['languages_required']}
}}

PREFERENCES {{
  tools: {pref['tools']}
  programming languages: {pref['languages']}
  framework libraries: {pref['frameworks']}
  databases cloud services: {pref['cloud']}
  degree: {pref['degree']}
  gpa: {pref['gpa']}
  experience: {pref['experience']}
  language: {pref['languages_required']}
  activities: {pref['activities']}
}}"""

def main():
    col_left, col_right = st.columns(2)

    with col_left:
        jd_data = jd_input()
        st.info("Please enter a role to generate the JD.")

    if jd_data:
        formatted_jd = format_jd_data(jd_data)

        with open("tests/qanhtest.txt", "w", encoding="utf-8") as f:
            f.write(formatted_jd)

        interpreter = Interpreter(jd_file="tests/qanhtest.txt")
        results = interpreter.rank_candidates()

        with col_right:
            config_output(jd_data)

        with st.expander("📄 Formatted JD Text Output"):
            st.code(formatted_jd, language="text")

       
        show_output(results)

if __name__ == "__main__":
    main()
