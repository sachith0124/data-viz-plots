import streamlit as st
import util
from config import PAGE_TITLE, PAGE_ICON

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

util.set_sidebar()

st.title("Data Vizualization Projects")
util.add_section_title("A set of data vizualization mini projects showcased as a Streamlit app.", level=3)
st.write("**Statistical Analysis, Data Analysis, Data Visualizaition, Interactive Dashboards**")
st.write("using Pandas, Numpy, IPython, Maplotlib, Seaborn, Vega-Altair, Streamlit")
st.header('', divider='blue')