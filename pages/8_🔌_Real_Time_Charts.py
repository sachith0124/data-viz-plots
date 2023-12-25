import streamlit as st

import sys
sys.path.append('../')

from util import set_sidebar, add_section_title, add_plot_title, add_vertical_space
from config import plt

from config import PAGE_TITLE, PAGE_ICON
st.set_page_config(page_icon=PAGE_ICON, page_title=f'{PAGE_TITLE} - Real Time Charts', layout='wide')
set_sidebar()

import seaborn as sns
sns.set()

#--- REAL TIME CHARTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Real Time Charts')
header.write("---")

real_time_charts_tabs = st.tabs(['Real Time Charts'])
with real_time_charts_tabs[0]:
    st.header('Real Time Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
