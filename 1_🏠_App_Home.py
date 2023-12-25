import streamlit as st
import util
from config import PAGE_TITLE, PAGE_ICON

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

util.set_sidebar()

st.title("Data Vizualization Projects")
st.subheader("A set of data vizualization mini projects showcased as a Streamlit app, visualizations made to practice Statistical and Data Analysis, Data Visualizaition and Interactive Dashboards development.")