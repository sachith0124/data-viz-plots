import streamlit as st
import pandas as pd
import numpy as np

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title, add_vertical_space
from config import plt

set_sidebar()

#--- SCATTER PLOTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Scatter Plots')
header.write("---")

scatter_plots_tabs = st.tabs(["Scatter Plots", "Bubble Plots"])
with scatter_plots_tabs[0]:
    st.header('Scatter Plots')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with scatter_plots_tabs[1]:
    st.header('Bubble Plots')
    st.write('---')

    add_section_title('Beta Fish: Price vs Size by Sex and Color')
    source_filepath = 'datasets/beta-fish.csv'
    beta_fish = pd.read_csv(source_filepath)

    size_mapping = {'male': 250, 'female': 100}
    beta_fish['bubble_size'] = beta_fish['sex'].map(size_mapping)

    color_mapping = {'red': 'red', 'galaxy': 'green', 'blue': 'blue'}
    beta_fish['bubble_color'] = beta_fish['color'].map(color_mapping)

    cols = st.columns([0.8, 0.2], gap='small')
    with cols[0]:
        plt_space = st.empty()
    with cols[1]:
        st.write("Beta Fish Sex:")
        selected_sex = st.radio(
            label='Select Fish Sex:', 
            options=beta_fish['sex'].unique().tolist(), 
            horizontal=False, 
            key='selected_sex',
            label_visibility='hidden'
        )

        add_vertical_space(3)

        st.write("Beta Fish Color:")
        uniq_colors = beta_fish['color'].unique().tolist()
        selected_colors = pd.Series(uniq_colors)[[st.checkbox(color, value=True) for color in uniq_colors]]
        color_query = 'color in @selected_colors'
    
    with plt_space:
        beta_fish = beta_fish[beta_fish['sex'] == selected_sex].query(color_query)
        plt.scatter(beta_fish['size'], beta_fish['price'], s=beta_fish['bubble_size'], c=beta_fish['bubble_color'], alpha=0.5)
        plt.xlabel("Size of Beta Fish")
        plt.ylabel("Price")
        plt.xticks(np.arange(1.5, 6.5, 0.5), np.arange(1.5, 6.5, 0.5))
        st.pyplot(plt.gcf())
