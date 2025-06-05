import streamlit as st

def show_output(results):

    seen = set()
    unique_results = []
    for r in results:
        identifier = (r["cv"].get("FullName"), r.get("percentage"))
        if identifier not in seen:
            seen.add(identifier)
            unique_results.append(r)

    st.success("Candidates ranked successfully!")
    st.markdown("### Ranked List:")

    for idx, result in enumerate(unique_results, 1):
        cv = result.get("cv", {})
        full_name = cv.get("FullName", f"Candidate {idx}")
        percentage = result.get("percentage", 0)
        passed = result.get("pass", False)

        with st.expander(f"#{idx} — {full_name} — Matching Score: {percentage:.2f}% {'✅ Pass' if passed else '❌ Fail'}"):
            st.markdown("####  Basic Info")
            st.markdown(f"- **Name:** {full_name}")
            st.markdown(f"- **Position:** {cv.get('Position','N/A')}")
            st.markdown(f"- **Level:** {cv.get('Level', 'N/A')}")
            st.markdown(f"- **Experience:** {cv.get('Experience', 'N/A')} years")
            st.markdown(f"- **Profile:** {cv.get('Profile', 'N/A')}")

            contact = cv.get("Contact", {})
            st.markdown("#### Contact")
            st.markdown(f"- **Email:** {contact.get('Email', 'N/A')}")
            st.markdown(f"- **Phone:** {contact.get('Phone', 'N/A')}")
            st.markdown(f"- **LinkedIn:** {contact.get('LinkedIn', 'N/A')}")
            st.markdown(f"- **GitHub:** {contact.get('GitHub', 'N/A')}")

            edu = cv.get("Education", {})
            st.markdown("####  Education")
            st.markdown(f"- **Degree:** {edu.get('Degree', 'N/A')}")
            st.markdown(f"- **Institution:** {edu.get('Institution', 'N/A')}")
            st.markdown(f"- **Duration:** {edu.get('Duration', 'N/A')}")
            st.markdown(f"- **GPA:** {edu.get('GPA', 'N/A')}")

            st.markdown("####  Technical Skills")
            tech = cv.get("TechnicalSkills", {})
            for key, items in tech.items():
                st.markdown(f"- **{key}:** {', '.join(items)}")

            st.markdown("#### Languages")
            langs = cv.get("Languages", {})
            for lang, level in langs.items():
                st.markdown(f"- {lang}: {level}")

            st.markdown("####  Projects")
            projects = cv.get("Projects", [])
            for proj in projects:
                st.markdown(f"**{proj.get('Name', 'Untitled')}** ({proj.get('Role', '')}) — *{proj.get('Duration', '')}*")
                for detail in proj.get("Details", []):
                    st.markdown(f"- {detail}")
