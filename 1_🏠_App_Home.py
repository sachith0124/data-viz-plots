import streamlit as st
import util
from config import PAGE_TITLE, PAGE_ICON

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

util.set_sidebar()

header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)

header.title("Data Vizualization Projects")
header.markdown("### A set of data vizualization mini projects showcased as a Streamlit app.")
header.write("**Statistical Analysis, Data Analysis, Data Visualizaition, Interactive Dashboards**")
header.write("using Pandas, Numpy, IPython, Maplotlib, Seaborn, Vega-Altair, Streamlit")
header.header('', divider='blue')

st.write('\n\n')
st.subheader("Overview")
st.write("---")

st.markdown("##### Bar Charts:")
