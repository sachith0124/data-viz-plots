import streamlit as st

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title
from config import plt

set_sidebar()

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
