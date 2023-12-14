import streamlit as st

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title
from config import plt

set_sidebar()

#--- GEOSPATIAL CHARTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Geospatial Charts')
header.write("---")

geospatial_charts_tabs = st.tabs(['Geospatial Charts'])
with geospatial_charts_tabs[0]:
    st.header('Geospatial Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
