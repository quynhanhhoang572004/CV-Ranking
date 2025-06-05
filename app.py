import streamlit as st
from components.jd_input import jd_input
from components.config_output import config_output
from components.output import show_output
from interpreter.Interpreter import Interpreter
from interpreter.InputProcessor import InputProcessor

st.set_page_config(layout="wide")
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
    <h1 style='
        text-align: center;
        font-size: 3em;
        font-family: "Poppins", sans-serif;
        font-weight: 600;
        color: white;
        margin-bottom: 20px;
    '>
        ☁️ JD Prompt Builder + CV Matcher
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

    <style>

    * {
        font-family: 'Poppins', sans-serif !important;
    }

    
    .stApp {
        background: linear-gradient(135deg, #bbdefb, #1565c0) !important;
        background-attachment: fixed !important;
        min-height: 100vh !important;
        color: white !important;
    }

    header[data-testid="stHeader"] {
        background: linear-gradient(135deg, #bbdefb, #1565c0) !important;
        background-attachment: fixed !important;
    }

    header[data-testid="stHeader"]::before {
        box-shadow: none !important;
    }

    .block-container {
        background-color: transparent !important;
    }

    .main .block-container {
        box-shadow: none !important;
    }

  
    label, .stTextInput label, .stSelectbox label, .stNumberInput label,
    .stTextArea label, .stMultiselect label, .stRadio label, .stCheckbox label {
        color: white !important;
    }


    .st-emotion-cache-10trblm.e1nzilvr1 {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 600;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)




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

        required_fields = jd_data.get("REQUIREMENTS", {})
        missing_fields = [
            key for key, value in required_fields.items()
            if isinstance(value, str) and not value.strip()
        ]

    with col_right:
        config_output(jd_data)

    if missing_fields:
        st.warning(
            "Please complete all required fields to generate the JD: "
            + ", ".join(missing_fields)
        )
        return

    formatted_jd = format_jd_data(jd_data)

    with open("tests/qanhtest.txt", "w", encoding="utf-8") as f:
        f.write(formatted_jd)

    interpreter = Interpreter(candidate_folder="data")
    processor = InputProcessor("tests/qanhtest.txt")
    jd_command = processor.getParsedInput()
    interpreter.run_command(jd_command)
    results = interpreter.show_top(100)

    with st.expander("📄 Formatted JD Text Output"):
        st.code(formatted_jd, language="text")

    show_output(results)



if __name__ == "__main__":
    main()
