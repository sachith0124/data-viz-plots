import streamlit as st

import sys
sys.path.append('../')

from util import set_sidebar, add_section_title, add_plot_title, add_vertical_space
from config import plt

from config import PAGE_TITLE, PAGE_ICON
st.set_page_config(page_icon=PAGE_ICON, page_title=f'{PAGE_TITLE} - Line Plots', layout='wide')
set_sidebar()

import seaborn as sns
sns.set()

#--- LINE PLOTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Line Plots')
header.write("---")

line_plots_tabs = st.tabs(['Line Plots', 'Multi Line Graphs', 'Area Charts', 'Stacked Area Plots'])
with line_plots_tabs[0]:
    st.header('Line Plots')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with line_plots_tabs[1]:
    st.header('Multi Line Graphs')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with line_plots_tabs[2]:
    st.header('Area Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
    
with line_plots_tabs[3]:
    st.header('Stacked Area Plots')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
