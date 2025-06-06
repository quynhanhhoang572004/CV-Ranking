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
        ☁️ HireX ☁️
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
    processor_normal = InputProcessor("tests/qanhtest.txt")
    jd_command = processor_normal.getParsedInput()
    print(jd_command)
    results =  interpreter.run_command(jd_command)
    print(interpreter.show_top(1))

    show_top = st.selectbox("Show Top Candidates", ("All", "Top 10", "Top 20", "Top 50"))

    with st.expander("📄 Formatted JD Text Output"):
        st.code(formatted_jd, language="text")
    queries= st.text_input("Query", placeholder="e.g show cv with")

    if not queries.strip():
            if show_top == "Top 10":
                filtered_results = interpreter.show_top(10)
            elif show_top == "Top 20":
                filtered_results = interpreter.show_top(20)
            elif show_top == "Top 50":
                filtered_results = interpreter.show_top(50)
            else:
                filtered_results = interpreter.show_top(len(interpreter.rankings))  
                
            show_output(filtered_results)

    elif queries and queries.strip():
        try:
            with open("./tests/ShowConditional.txt", "w", encoding="utf-8") as f:
                f.write(f"{queries}")
            
            query_processor = InputProcessor("./tests/ShowConditional.txt")
            custom_query = query_processor.getParsedInput()
            print(custom_query)
            
            if custom_query is None or "command" not in custom_query:
                st.error("Invalid query format. Please check your query syntax.")
                return
                
            custom_results = interpreter.run_command(custom_query)
            
            if custom_results is None or (isinstance(custom_results, list) and len(custom_results) == 0):
                st.warning(f"No candidates match the query: '{queries}'")

            else:
                show_output(custom_results)
                
        except Exception as e:
            st.error("Your input is wrong, please check again")
            
    else:
        show_output(results)

if __name__ == "__main__":
    main()
