import streamlit as st

def config_output(data):
    req = data["REQUIREMENTS"]
    pref = data["PREFERENCES"]

    st.subheader(" JD Requirements Output")

   
    with st.expander("REQUIREMENTS", expanded=True):
        st.markdown(f"**Position:** {req['position']}")
        st.markdown(f"**Level:** {req['level']}")
        
        st.markdown("**Stack:**")
        st.markdown(f"- Tools: {req['tools']}")
        st.markdown(f"- Programming Languages: {req['languages']}")
        st.markdown(f"- Framework Libraries: {req['frameworks']}")
        st.markdown(f"- Databases/Cloud Services: {req['cloud']}")

        st.markdown("**Education:**")
        st.markdown(f"- Major: {req['field']}")
        st.markdown(f"- Degree: {req['degree']}")
        st.markdown(f"- GPA: {req['gpa']}")

        st.markdown(f"**Experience:** {req['experience']}")
        st.markdown(f"**Language(s) Required:** {req['languages_required']}")

    with st.expander("PREFERENCES", expanded=True):
        st.markdown(f"- Tools: {pref['tools']}")
        st.markdown(f"- Programming Languages: {pref['languages']}")
        st.markdown(f"- Framework Libraries: {pref['frameworks']}")
        st.markdown(f"- Databases/Cloud Services: {pref['cloud']}")
        st.markdown(f"- Degree: {pref['degree']}")
        st.markdown(f"- GPA: {pref['gpa']}")
        st.markdown(f"- Experience: {pref['experience']}")
        st.markdown(f"- Language(s): {pref['languages_required']}")
        st.markdown(f"- Activities: {pref['activities']}")
