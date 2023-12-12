from matplotlib import pyplot as plt

import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_ICON = Image.open(profile_pic)
NAME = "Sachith Kumar Janjirala"
EMAIL = "sachith@tamu.com"
DESCRIPTION = """
    A recent Data Science Grad from Texas A&M University, College Station; 
    with an undergraduate Computer Science degree and 3+ years of work experience in Data Science and Software Engineering. Passionate about working with data to build and deploy scalable AI/ML models.
"""
def set_css():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- PROFILE PIC ---
profile_pic = Image.open(profile_pic)

# -- SET PLOT STYLE --
plt.style.use('seaborn-v0_8')
