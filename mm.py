import streamlit as st

def main():
    st.title("The Resume Project")

    # Personal Information
    st.header("Personal Information")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_area("Address")

    # Other Profiles
    with st.expander("Other Profiles"):
        website_url_linkedin = st.text_input("LinkedIn URL")
        website_url_github = st.text_input("GitHub URL")

    # Education
    st.header("Education")
    with st.expander("Add Education"):
        education_12th_grade = st.text_area("12th Grade")
        education_graduation = st.text_area("Graduation")
        education_post_graduation = st.text_area("Post Graduation")

    # Skills
    st.header("Skills")
    with st.expander("Add Skills"):
        technical_skills = st.text_area("Technical Skills")
        personal_skills = st.text_area("Personal Skills")
        software_skills = st.text_area("Software Skills")

    # Certificates
    st.header("Certificates")
    with st.expander("Add Certificates"):
        certificate_1 = st.text_input("Name of Course/Competition 1")
        certificate_2 = st.text_input("Name of Course/Competition 2")
        certificate_3 = st.text_input("Name of Course/Competition 3")

    #Work Experience
    st.header("Work Experience")
    with st.expander("Add Work Experience"):
        work_1 = st.text_area("what was role and objectives for work experience 1")
        work_2 = st.text_area("what was role and objectives for work experience 2")

    # Projects
    st.header("Projects")
    with st.expander("Add Project 1"):
        project_title = st.text_input("Project Title")
        project_description = st.text_area("Description")

    # Display Resume
    if st.button("Preview Resume"):
        st.subheader("Resume Preview")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Phone:** {phone}")
        st.markdown(f"**Address:** {address}")

        st.write("## Other Profiles")
        st.write(f"- **LinkedIn:** {website_url_linkedin}")
        st.write(f"- **GitHub:** {website_url_github}")

        st.write("## Education")
        st.write(f"- **12th Grade:** {education_12th_grade}")
        st.write(f"- **Graduation:** {education_graduation}")
        st.write(f"- **Post Graduation:** {education_post_graduation}")

        st.write("## Skills")
        st.write(f"- **Technical Skills:** {technical_skills}")
        st.write(f"- **Personal Skills:** {personal_skills}")
        st.write(f"- **Software Skills:** {software_skills}")

        st.write("## Certificates")
        st.write(f"- **Name of Course/Competition 1:** {certificate_1}")
        st.write(f"- **Name of Course/Competition 2:** {certificate_2}")
        st.write(f"- **Name of Course/Competition 3:** {certificate_3}")

        st.write("## Work Experience")
        st.write(f"- **what was role and objectives for work experience 1:** {work_1}")
        st.write(f"- **what was role and objectives for work experience 2:** {work_2}")
      

        st.write("## Projects")
        st.write(f"- **{project_title}:** {project_description}")

if __name__ == "__main__":
    main()