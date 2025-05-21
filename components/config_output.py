import streamlit as st

def config_output(data):
    config_str = f"""
REQUIREMENTS {{
    position: {data['role']}
    level: {data['level']}
    stack {{
        tools: {data['tools']}
        programming languages: {data['languages']}
        framework libraries: {data['frameworks']}
        databases cloud services: {data['cloud']}
    }}
    education {{
        major: {data['field']}
        degree: {data['degree']}
        gpa: {data['gpa']}
    }}
    experience: {data['experience']} years
    language: {data['languages_required']}
    activities: {data['activities']}
    references: {data['references']}
}}""".strip()

    st.subheader("📋 Structured JD Requirements")
    st.code(config_str, language="yaml")

    if st.button("✅ Submit JD"):
        st.success("JD submitted successfully!")

    return config_str
