import streamlit as st
import json
import os

DATA_DIR = "data"

st.title(":blossom: View CV")
st.markdown("Select a CV to see it detail.")

cv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]

selected_file = st.selectbox("Choose a candidate file", cv_files)

with open(os.path.join(DATA_DIR, selected_file), "r", encoding="utf-8") as f:
    cv_data = json.load(f)

st.header(f"{cv_data.get('FullName', 'Unknown Name')} ({cv_data.get('Level', '')})")
st.write(cv_data.get("Profile", ""))

st.subheader("Contact")
for key, value in cv_data.get("Contact", {}).items():
    st.write(f"**{key}:** {value}")

st.subheader("Education")
edu = cv_data.get("Education", {})
st.write(f"**{edu.get('Degree', '')}**, {edu.get('Institution', '')}")
st.write(f"{edu.get('Duration', '')} | GPA: {edu.get('GPA', '')}")


st.subheader("Technical Skills")
skills = cv_data.get("TechnicalSkills", {})
for section, items in skills.items():
    if isinstance(items, dict):
        st.write(f"**{section}:**")
        for lang, level in items.items():
            st.write(f"- {lang}: {level}")
    else:
        st.write(f"**{section}:** {', '.join(items)}")


st.subheader("Projects")
for proj in cv_data.get("Projects", []):
    st.markdown(f"**{proj['Name']}** ({proj['Duration']})")
    st.write(f"Role: {proj['Role']}")
    for d in proj['Details']:
        st.markdown(f"- {d}")


if cv_data.get("Leadership",[]):
    st.subheader("Leadership")
    for lead in cv_data["Leadership"]:
        st.markdown(f"**{lead["Organization"]}** ({lead["Duration"]})")
        st.write(f"{lead['Role']} ")
      
        for a in lead["Activities"]:
            st.markdown(f"- {a}")
  

if cv_data.get("References"):
    st.subheader("References")
    for ref in cv_data["References"]:
        st.markdown(f"**{ref["Name"]}**")
        st.write(f" Insitution{ref["Institution"]}")
        st.write(f" Email: {ref["Email"]}")
