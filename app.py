import streamlit as st
from components.jd_input import jd_input
from components.config_output import config_output

st.set_page_config(layout="wide")
st.title("🧩 JD Prompt Builder + CV Matcher")

def main():
    col_left, col_right = st.columns(2)

    with col_left:
        jd_data = jd_input()
        st.info("Please enter a role to generate the JD.")

    with col_right:
        config_str = config_output(jd_data)

if __name__ == "__main__":
    main()
