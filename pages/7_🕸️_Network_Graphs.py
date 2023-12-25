import streamlit as st

import sys
sys.path.append('../')

from util import set_sidebar, add_section_title, add_plot_title, add_vertical_space
from config import plt

from config import PAGE_TITLE, PAGE_ICON
st.set_page_config(page_icon=PAGE_ICON, page_title=f'{PAGE_TITLE} - Network Graphs', layout='wide')
set_sidebar()

import seaborn as sns
sns.set()

#--- NETWORK GRAPHS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Network Graphs')
network_graphs_tabs = st.tabs(['Network Graphs'])

with network_graphs_tabs[0]:
    st.header('Network Graphs')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
