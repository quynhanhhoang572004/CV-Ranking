import streamlit as st

def jd_input():
    st.subheader("💼 JD Prompt Input")

    st.markdown("## 📌 REQUIREMENTS")

    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input(" Position", placeholder="e.g. AI Engineer")
    with col2:
        level = st.selectbox(" Level", ["intern", "junior", "medium", "senior", "fresher", "lead", "manager", "director"], index=0)

    col1, col2 = st.columns(2)
    with col1:
        experience = st.text_input(" Experience", placeholder="e.g. 5 years")
    with col2:
        languages_required = st.text_input(" Required Language(s)", placeholder="e.g. English, Japanese")

    st.markdown("### 🧰 Stack")
    col1, col2 = st.columns(2)
    with col1:
        tools = st.text_input(" Tools", placeholder="e.g. Git, Docker, GitHub Actions")
        frameworks = st.text_input(" Framework Libraries", placeholder="e.g. PyTorch, TensorFlow")
    with col2:
        languages = st.text_input(" Programming Languages", placeholder="e.g. Python, C++")
        cloud = st.text_input(" Databases / Cloud Services", placeholder="e.g. PostgreSQL, AWS")

    st.markdown("###  Education")
    col1, col2, col3 = st.columns(3)
    with col1:
        field = st.text_input("🧪 Major", placeholder="e.g. Artificial Intelligence")
    with col2:
        degree = st.text_input(" Degree", placeholder="e.g. Master")
    with col3:
        gpa = st.text_input(" GPA", placeholder="e.g. >= 3.5")

    st.markdown("---")
    st.markdown("## 🌟 PREFERENCES")

    col1, col2 = st.columns(2)
    with col1:
        pref_tools = st.text_input(" Tools (Preferred)", placeholder="e.g. VSCode, Slack")
        pref_frameworks = st.text_input(" Frameworks (Preferred)", placeholder="e.g. Flask")
    with col2:
        pref_languages = st.text_input(" Programming Languages (Preferred)", placeholder="e.g. Java")
        pref_cloud = st.text_input(" Cloud/Database (Preferred)", placeholder="e.g. MongoDB")

    col1, col2, col3 = st.columns(3)
    with col1:
        pref_degree = st.text_input(" Degree (Preferred)", placeholder="e.g. PhD")
    with col2:
        pref_gpa = st.text_input(" GPA (Preferred)", placeholder="e.g. > 3.8")
    with col3:
        pref_experience = st.text_input(" Experience (Preferred)", placeholder="e.g. 2 years")

    col1, col2 = st.columns(2)
    with col1:
        pref_languages_required = st.text_input(" Language(s) (Preferred)", placeholder="e.g. Korean")
    with col2:
        pref_activities = st.text_input(" Activities", placeholder="e.g. Kaggle Winner")

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
