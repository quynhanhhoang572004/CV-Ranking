import streamlit as st

def jd_input():
    st.subheader("✍️ JD Prompt Input")

    col1, col2, col3, col4 = st.columns([1.5, 2, 1.2, 2])
    with col1:
        st.markdown("**We are hiring a/an**", unsafe_allow_html=True)
    with col2:
        role = st.text_input("Role", placeholder="e.g. AI engineer", label_visibility="collapsed")
    with col3:
        st.markdown("**with level**", unsafe_allow_html=True)
    with col4:
        level = st.selectbox("Level", ["junior", "mid", "senior", "lead"], index=2, label_visibility="collapsed")

    st.markdown("**Whose stack is:**")
    col1, col2 = st.columns(2)
    with col1:
        tools = st.text_input("🧰 Tools", "docker, git")
        frameworks = st.text_input("📚 Framework Libraries", "react, django")
    with col2:
        languages = st.text_input("💻 Programming Languages", "python, react")
        cloud = st.text_input("☁️ Database & Cloud Services", "mysql, aws")

    st.markdown("**Education Level:**")
    col1, col2, col3 = st.columns([1.5, 1.5, 1])
    with col1:
        field = st.text_input("Field of Study", "computer science")
    with col2:
        degree = st.text_input("Degree", "bachelor")
    with col3:
        gpa = st.text_input("GPA", ">= 3.2")

    st.markdown("**Language & Activities:**")
    col1, col2, col3 = st.columns([2, 1.2, 2])
    with col1:
        languages_required = st.text_input("Language(s) Required", "english")
    with col2:
        experience = st.number_input("Years of Experience", min_value=0, value=2)
    with col3:
        activities = st.text_input("Desired Activities", "open-source, hackathon")

    return {
        "role": role.strip(),
        "level": level,
        "tools": tools,
        "languages": languages,
        "frameworks": frameworks,
        "cloud": cloud,
        "field": field,
        "degree": degree,
        "gpa": gpa,
        "languages_required": languages_required,
        "experience": experience,
        "activities": activities,
        "references": "dr. smith"
    }
