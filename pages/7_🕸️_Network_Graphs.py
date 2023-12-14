import streamlit as st

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title
from config import plt

set_sidebar()

#--- NETWORK GRAPHS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Network Graphs')
header.write("---")

network_graphs_tabs = st.tabs(['Network Graphs'])
with network_graphs_tabs[0]:
    st.header('Network Graphs')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
