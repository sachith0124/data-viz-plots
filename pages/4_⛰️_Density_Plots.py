import streamlit as st

import sys
sys.path.append('../')

from util import set_sidebar, add_section_title, add_plot_title, add_vertical_space
from config import plt

from config import PAGE_TITLE, PAGE_ICON
st.set_page_config(page_icon=PAGE_ICON, page_title=f'{PAGE_TITLE} - Density Plots', layout='wide')
set_sidebar()

import seaborn as sns
sns.set()

#--- DENSITY PLOTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Density Plots')
density_plots_tabs = st.tabs(['Histograms', 'Density Plots'])

with density_plots_tabs[0]:
    st.header('Histograms')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with density_plots_tabs[1]:
    st.header('Density Plots')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
