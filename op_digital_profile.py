import streamlit as st

Page_Config = {"page_title": 'OP Digital Profile', 
               "page_icon": "op_logo.PNG",
               "layout": 'wide',}
st.set_page_config(**Page_Config)

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

st.image("op_photo.PNG")
st.write(""" # Omprakash Mishra | **_Student_** """)
st.write(""" ### Hello World! :sunglasses: \n ##### Welcome to my online home. \
        This is my personal website, designed, built, and edited entirely by me. \
        I have created this in order to connect with people.""")

st.sidebar.code("Life is what You make it.")

def menubar():
    option = st.selectbox(
        "",
        ["Contact", "Internships", "Education", "Skills and Certifications", "Projects"]
    )
    
    if option == "Internships":
        internships()
    
    elif option == "Education":
        education()

    elif option == "Skills and Certifications":
        skills_and_certification()

    elif option == "Projects":
        Projects()
    
    else:
        contact()

def contact():
    st.balloons()
    ll_link  ="[Linkedin](https://www.linkedin.com/in/omprakash-mishra-b10779172)"
    sololearn = "[SoloLearn]()"
    github = "[Github]()"
    with st.expander("Gmail"):
        st.markdown("_omprakash36mishra@gmail.com_")
    
    col1, col2 = st.columns([1, 6])
    col1.image("linkedin_logo_rs.png")
    col2.write("")
    col2.write("")
    col2.markdown(ll_link)
    col1, col2 = st.columns([1, 6])
    col1.image("sololearn_rs.jpg")
    col2.write("")
    col2.write("")
    col2.markdown(sololearn)
    col1, col2 = st.columns([1, 6])
    col1.image("github_logo.png")
    col2.write("")
    col2.write("")
    col2.markdown(github)

def internships():
    st.balloons()
    col1, col2 = st.columns([1, 6])
    col1.write("")
    col1.write("")
    col1.write("")
    col1.image("chercher_tech_logo.jfif")
    col2.header("CherCher Tech")
    col2.write(""" #### Technical Content Developer, # \n 
    Currently working here.""")
    link = "[My work](https://pythonwife.com/author/om-prakash/)"
    col2.markdown(link)

    col1, col2 = st.columns([1, 6])
    col1.write("")
    col1.write("")
    col1.image("velvish_digital_logo.jfif")
    col2.header("Velvish Digital")
    col2.write(""" #### Web Developer, # \n 
    Worked with Bootstrap, PHP, SQL.""")    
    

def education():
    st.balloons()

    col1, col2 = st.columns([1, 7])
    col1.write("")
    col1.image("format.PNG")
    col2.header("B Tech, Computer Science And Engineering")
    col2.write(""" #### Rewa Engineering College, # \n 
    2018-2022, CGPA 8.4""")

    col1, col2 = st.columns([1, 7])
    col1.write("")
    col1.image("format.PNG")
    col2.header("High School, PCM,")
    col2.write(""" #### Gurukul Sr. Sec. School - CBSE, # \n 
    2017-2018, Passed with 84.2%""")

    col1, col2 = st.columns([1, 7])
    col1.write("")
    col1.image("format.PNG")
    col2.header("10th,")
    col2.write(""" #### Gurukul Sr. Sec. School - CBSE, # \n 
    2015-2016, Passed with 9.0 CGPA""")    

def skills_and_certification():
    st.balloons()
    col1, col2 = st.columns([1, 7])
    col1.image("python_rs.png")
    col2.write("")
    with col2.expander("Python"):
        link = "[Verify Credentials](https://www.hackerrank.com/certificates/7a4e8de613bb)"
        st.image("python_certificate_rs.PNG")
        st.markdown(link, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 7])
    col1.image("cpp_rs.png")
    col2.write("")
    with col2.expander("C++"):
        link = "[Verify Credentials](https://www.hackerrank.com/certificates/9cde7985e59f)"
        st.image("cpp_certificate_rs.PNG")
        st.markdown(link, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 7])
    col1.image("c_rs.png")
    col2.write("")
    with col2.expander("C"):
        link = "[Verify Credentials](https://www.sololearn.com/Certificate/1089-14905430/jpg/)"
        st.image("c_certificate_rs.jpg")
        st.markdown(link, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 7])
    col1.image("sql_rs.png")
    col2.write("")
    with col2.expander("SQL"):
        link = "[Verify Credentials](https://www.hackerrank.com/certificates/5d84ba908650)"
        st.image("sql_certificate_rs.PNG")
        st.markdown(link, unsafe_allow_html=True)

def Projects(): 
    st.balloons()   
    st.subheader("Vision based Human action detection.")
    st.subheader("Streamlit Web App.")
    st.subheader("GUI chatting applcation, with tkinter and socket programming.")
    st.subheader("Voice asstiant for Windows-OS.")

menubar()
