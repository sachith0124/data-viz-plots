import streamlit as st

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title
from config import plt

set_sidebar()

#--- DENSITY PLOTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Density Plots')
header.write("---")

density_plots_tabs = st.tabs(['Histograms', 'Density Plots'])
with density_plots_tabs[0]:
    st.header('Histograms')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with density_plots_tabs[1]:
    st.header('Density Plots')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
