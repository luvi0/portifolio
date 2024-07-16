from pathlib import Path
import streamlit as st 
from PIL import Image 


icon_base64 = "https://img.icons8.com/?size=100&id=37737&format=png&color=000000"  

st.set_page_config(
    page_icon=icon_base64,
    layout="centered",  
    initial_sidebar_state="auto" 
)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {'#003644'};
        color: white !important;
    
    }}
    a{{color: #9A6533 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
arquivo_pdf = diretorio / "arquivos" / "Profile.pdf"
arquivo_imagem = diretorio / "arquivos" / "foto_perfil.png"


NAME = "Otavio Viana"
Description = """
    I am mechatronics engineer, data scientist, developer for robot´s and automations,
    i’m currently working on DATA SCIENCE and RPA, currently learning more machine learning, mojo, cython, flask and deep lerning, 
    i’m looking for help with FastAPI and Mojo, regularly i write articles on Data ( with energy solar) and machine learning, 
    ask me about the grandfather, machine learning, systems control, dostoevsky and jorge amado
"""

EMAIL = "otavio.engenheiro.viana@outlook.com"
MEDIA_SOCIAL = {
    "Email" : "otavio.engenheiro.viana@outlook.com",
   "LinkedIn": "https://www.linkedin.com/in/otavio-viana-35b24325b/",
    "GitHub": "https://github.com/luvi0"
}
PROJETOS = {
     
    "Machine Learning Regression - SoLia" : "https://github.com/luvi0/SoLia",
    "Machine Learnign for Classification in AIDS": "https://github.com/luvi0/ML_AIDS",
    "Clustering NPS": "https://github.com/luvi0/NPS",    
    "Automation JuxBrasil": "https://github.com/luvi0/juxbrasil",
}
linkedin = "https://www.linkedin.com/in/otavio-viana-35b24325b/"
github =  "https://github.com/luvi0"

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfLeitura = arquivo_pdf.read()
imagem = Image.open(arquivo_imagem)

col1, col2, col3 = st.tabs(["Guide","Projects", "Skills"])
with col1:
    st.image(imagem, width=650)
    st.title(NAME)
    st.write(Description)
    st.write("E-mail : ", EMAIL)
    st.write("Linkedin :",linkedin)
    st.write("Github :",github)
    st.write(MEDIA_SOCIAL)
    st.download_button(
    label="Downlaod CV",
    data= pdfLeitura,
    file_name=arquivo_pdf.name,
    mime="application/octet-stream"
    )

with col2:
    st.title("PROJECTS")
    st.write(PROJETOS)
    coluna = st.columns(len(PROJETOS))
    for indi, (plataform, link) in enumerate(PROJETOS.items()):
            coluna[indi].write(f"[{plataform}]({link})")
with col3:
    st.title("SKILLS")

    html_content = """
    <h3>Programming</h3>
    <div style="display: flex; align-items: center;">
        <img src="https://img.icons8.com/?size=100&id=Ve5z6WN65Tg6&format=png&color=000000" alt="Python" style="width: 50px; height: 50px; margin-right: 50px;">
        <img src="https://img.icons8.com/?size=100&id=TpULddJc4gTh&format=png&color=000000" alt="C plus plus" style="width: 50px; height: 50px;">
    </div>
    <h3>Database</h3>
    <div style="display: flex; align-items: center;">
        <img src="https://img.icons8.com/?size=100&id=4ZM6CrdtsQVN&format=png&color=000000" alt="sql" style="width: 60px; height: 60px; margin-right: 50px;">
    </div>
    <h3>Frameworks</h3>
    <div style="display: flex; align-items: center;">
        <img src="https://img.icons8.com/?size=100&id=0HyDNss5DL1B&format=png&color=000000" alt="git"    style="width: 50px; height: 50px;margin-right: 50px;">
        <img src="https://img.icons8.com/?size=100&id=mUBILbYvUMq8&format=png&color=000000" alt="django" style="width: 50px; height: 50px;margin-right: 50px;">
        <img src="https://fastapi.tiangolo.com/img/icon-white.svg" alt="FastAPI"                         style="width: 50px; height: 50px;margin-right: 50px;">
        <img src="https://img.icons8.com/?size=100&id=MHcMYTljfKOr&format=png&color=000000" alt="flask"  style="width: 60px; height: 60px;margin-right: 50px;">   
    </div>
    <div>
    <h3>Machine Learning</h3>
    <img src="https://shap.readthedocs.io/en/latest/_static/shap_logo_white.png" alt="Shap" style="width: 50px; height: 70px; margin-right: 50px;">
    <img src="https://xgboost.ai/images/logo/xgboost-logo.png" alt="xgboost"                style="width: 100px; height: 50px; margin-right: 50px;">
    <img src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" alt="Scikit-Learn" style="width: 110px; height: 60px; margin-right: 50px;">
    <img src="https://www.statsmodels.org/stable/_static/statsmodels-logo-v2-bw.svg" alt="Stats models" style="width: 50px; height: 80px; margin-right: 50px;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/512px-Pandas_logo.svg.png" alt="Pandas" style="width: 110px; height: 80px; margin-right: 50px;">
        
    </div>
    <div>
    <h3>Container</h3>
     <img src="https://img.icons8.com/?size=100&id=22813&format=png&color=000000" alt="Docker" style="width: 50px; height: 50px; margin-right: 50px;">
    </div>
    """
    st.markdown(html_content, unsafe_allow_html=True)


if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

dark_mode_css = """
<style>
body, .stApp {
    background-color: #121212;
    color: white;
}
a {
    color: #FFFFFF !important;
}
</style>
"""

if st.session_state.dark_mode:
    st.markdown(dark_mode_css, unsafe_allow_html=True)
else:
 
    st.markdown(
        """
        <style>
        a {
            color: #9A6533 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.dark_mode

if st.button("Dark Mode"):
        toggle_dark_mode()

