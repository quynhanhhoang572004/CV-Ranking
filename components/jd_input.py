import streamlit as st

def jd_input():
    st.subheader(" JD Prompt Input")

    st.markdown("###  REQUIREMENTS")

    # Role & Level
    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input(label="position:", placeholder="e.g. ai engineer", label_visibility="visible")
    with col2:
        level = st.selectbox("level:", ["intern","junior", "mid", "senior", "lead"], index=2)

    # Experience & Languages Required
    col1, col2 = st.columns(2)
    with col1:
        experience = st.text_input("experience:", "5 years")
    with col2:
        languages_required = st.text_input("language:", "english, japanese")

    # Tech Stack
    st.markdown("**stack { ... }**")
    col1, col2 = st.columns(2)
    with col1:
        tools = st.text_input("tools:", "git, docker, github actions")
        frameworks = st.text_input("framework libraries:", "pytorch, tensorflow")
    with col2:
        languages = st.text_input("programming languages:", "python, c++")
        cloud = st.text_input("databases cloud services:", "postgresql, aws")

    # Education
    st.markdown("**education { ... }**")
    col1, col2, col3 = st.columns(3)
    with col1:
        field = st.text_input("major:", "artificial intelligence")
    with col2:
        degree = st.text_input("degree:", "master")
    with col3:
        gpa = st.text_input("gpa:", ">= 3.5")

    # PREFERENCES
    st.markdown("---")
    st.markdown("### PREFERENCES")

    col1, col2 = st.columns(2)
    with col1:
        pref_tools = st.text_input("tools:", "vscode, slack")
        pref_frameworks = st.text_input("framework libraries:", "flask")
    with col2:
        pref_languages = st.text_input("programming languages:", "java")
        pref_cloud = st.text_input("databases cloud services:", "mongodb")

    col1, col2, col3 = st.columns(3)
    with col1:
        pref_degree = st.text_input("degree:", "phd")
    with col2:
        pref_gpa = st.text_input("gpa:", "> 3.8")
    with col3:
        pref_experience = st.text_input("experience:", "2 years")

    col1, col2 = st.columns(2)
    with col1:
        pref_languages_required = st.text_input("language:", "korean")
    with col2:
        pref_activities = st.text_input("activities:", "kaggle winner")

    return {
        "REQUIREMENTS": {
            "position": role.strip(),
            "level": level.strip(),
            "tools": tools.strip(),
            "languages": languages.strip(),
            "frameworks": frameworks.strip(),
            "cloud": cloud.strip(),
            "field": field.strip(),
            "degree": degree.strip(),
            "gpa": gpa.strip(),
            "experience": experience.strip(),
            "languages_required": languages_required.strip()
        },
        "PREFERENCES": {
            "tools": pref_tools.strip(),
            "languages": pref_languages.strip(),
            "frameworks": pref_frameworks.strip(),
            "cloud": pref_cloud.strip(),
            "degree": pref_degree.strip(),
            "gpa": pref_gpa.strip(),
            "experience": pref_experience.strip(),
            "languages_required": pref_languages_required.strip(),
            "activities": pref_activities.strip()
        }
    }
