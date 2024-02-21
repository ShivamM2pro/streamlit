import streamlit as st
from fpdf import FPDF

def generate_pdf(name, email, phone, address, about_me, website_url_linkedin, website_url_github,
                 education_12th_grade, education_graduation, education_post_graduation,
                 technical_skills, personal_skills, software_skills,
                 certificate_1, certificate_2, certificate_3,
                 hobbies, work_1, work_2, project_title, project_description):
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Garamond", size=12)

    #pdf.cell(200, 10, txt="Resume", ln=True, align="C")
    #pdf.ln(10)
    
    pdf.cell(200, 10, txt="Personal Information", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Phone: {phone}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Address: {address}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"About Me: {about_me}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"LinkedIn: {website_url_linkedin}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"GitHub: {website_url_github}", ln=True, align="L")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Education", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"12th Grade: {education_12th_grade}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Graduation: {education_graduation}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Post Graduation: {education_post_graduation}", ln=True, align="L")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Skills", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Technical Skills: {technical_skills}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Personal Skills: {personal_skills}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Software Skills: {software_skills}", ln=True, align="L")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Certificates", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Name of Course/Competition 1: {certificate_1}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Name of Course/Competition 2: {certificate_2}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Name of Course/Competition 3: {certificate_3}", ln=True, align="L")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Hobbies", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"My Hobbies are: {hobbies}", ln=True, align="L")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Work Experience", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"What was role and objectives for work experience 1: {work_1}", ln=True, align="L")
    pdf.cell(200, 10, txt=f"What was role and objectives for work experience 2: {work_2}", ln=True, align="L")
    pdf.ln(10)
    
    pdf.cell(200, 10, txt="Projects", ln=True, align="L")
    pdf.ln(5)
    pdf.cell(200, 10, txt=f"{project_title}: {project_description}", ln=True, align="L")

    return pdf.output(dest="S").encode("latin1")

def main():
    st.title("The Resume Project")

    # Personal Information
    st.header("Personal Information")
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    address = st.text_area("Address")

    # About Me
    st.header("About Me")
    about_me = st.text_area("About Me")

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

    # Hobbies
    st.header("Hobbies")
    hobbies = st.text_area("My Hobbies are")

    #Work Experience
    st.header("Work Experience")
    with st.expander("Add Work Experience"):
        work_1 = st.text_area("what was role and objectives for work experience 1")
        work_2 = st.text_area("what was role and objectives for work experience 2")

    # Projects
    st.header("Projects")
    with st.expander("Add Project 1"):
        project_title = st.text_input("Project Title")
        project_description = st.text_area(" The Project Description")

    # Display Resume
    if st.button("Preview Resume"):
        st.subheader("Resume Preview")
        st.markdown(f"**Name:** {name}")
        st.markdown(f"**Email:** {email}")
        st.markdown(f"**Phone:** {phone}")
        st.markdown(f"**Address:** {address}")

        st.write("## About Me")
        st.write(f"- **About Me:** {about_me}")

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

        st.write("## Hobbies")
        st.write(f"- **My Hobbies are:** {hobbies}")

        st.write("## Work Experience")
        st.write(f"- **What was role and objectives for work experience 1:** {work_1}")
        st.write(f"- **What was role and objectives for work experience 2:** {work_2}")
      
        st.write("## Projects")
        st.write(f"- **{project_title}:** {project_description}")

    if st.button("Download PDF"):
        pdf_bytes = generate_pdf(name, email, phone, address, about_me, website_url_linkedin, website_url_github,
                                 education_12th_grade, education_graduation, education_post_graduation,
                                 technical_skills, personal_skills, software_skills,
                                 certificate_1, certificate_2, certificate_3,
                                 hobbies, work_1, work_2, project_title, project_description)
        st.download_button(label="Download Resume PDF", data=pdf_bytes, file_name="resume.pdf", mime="application/pdf")

if __name__ == "__main__":
    main()
