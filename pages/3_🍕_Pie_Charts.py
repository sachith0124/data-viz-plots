import streamlit as st

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title
from config import plt

set_sidebar()

#--- PIE CHARTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Pie Charts')
header.write("---")

pie_charts_tabs = st.tabs(['Pie Charts', 'Donut Charts', 'Radial Charts', 'Sun Burst Charts'])
with pie_charts_tabs[0]:
    st.header('Pie Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with pie_charts_tabs[1]:
    st.header('Donut Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with pie_charts_tabs[2]:
    st.header('Radial Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
    
with pie_charts_tabs[3]:
    st.header('Sun Burst Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
