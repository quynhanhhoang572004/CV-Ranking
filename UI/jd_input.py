import streamlit as st

st.title(" Job Description Input")

with st.form("Require JD"):

    position_input = st.text_input("Position", placeholder="Please input the job position ")

    level = st.text_input("Level", placeholder="Please input canidate level")

    st.markdown("### Tech Stack Requirements")
    with st.container():
        tools = st.text_input("Tools", placeholder="Please input tools canidate require to have")

        programming_language = st.text_input("Programming language", placeholder="Please input candinates require programming language")

        frame_work = st.text_input("Framework libraries", placeholder="Please input the user require framework ")

        database_service = st.text_input("Databases cloud service", placeholder="Please input the cloud service require canidates")

    st.markdown("### Education Requirement ")
    with st.container():

        major = st.text_input("Major", placeholder="Please input the major require")

        degree = st.text_input("Degree", placeholder="Please input dgree require candinate")

        gpa = st.text_input("GPA", placeholder="Please input the GPA requirement e.g >=3.5")

    st.markdown("### Other requirement ")
    with st.container():
        experience= st.text_input("Experience",placeholder="Please input the year of experience require")



    st.markdown(
    """
    <style>
    text_input {
        font-size: 2rem !important;
    }
    input {
        font-size: 1.1rem !important;
    }
    label {
        font-size: 1.5rem !important;
        font-weight: bold !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
    
    submitted = st.form_submit_button("Submit")
    

  




