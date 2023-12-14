import streamlit as st
import pandas as pd
import collections

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title
from config import plt

set_sidebar()

#--- BAR CHARTS ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.markdown('# Bar Charts')
header.write("---")

bar_charts_tabs = st.tabs(['Vertical', 'Horizontal', 'Grouped'])
with bar_charts_tabs[0]:
    st.header('Vertical Bar Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")

with bar_charts_tabs[1]:
    st.header('Horizontal Bar Charts')
    st.write('---')
    add_section_title('Popular Programming Languages: Frequency Plot')
    source_filepath = 'datasets/prog-langs.csv'
    prog_langs_df = pd.read_csv(source_filepath)

    language_counter = collections.Counter()
    update_language_counter = lambda reponse: language_counter.update(reponse.split(';'))
    prog_langs_df['LanguagesWorkedWith'].apply(update_language_counter)

    popular_prog_langs = pd.DataFrame(columns=['Prog Language', 'Frequency'])
    for item in language_counter.most_common():
        popular_prog_langs.loc[len(popular_prog_langs)] = item

    cols = st.columns([0.2, 0.8], gap='small')
    with cols[0]:
        with st.expander('Programming Langugages', expanded=True):
            values = [st.checkbox(language, value=True) for language in popular_prog_langs['Prog Language']]
            # add_checkboxes_in_cols(list(popular_prog_langs['Prog Language']), n_columns=4)
            css='''
            <style>
                [data-testid="stExpander"] {
                    overflow: scroll;
                    height: 550px;
                }
            </style>
            '''
            st.markdown(css, unsafe_allow_html=True)
    with cols[1]:
        plot_spot = st.empty()

    with plot_spot:
        popular_prog_langs = popular_prog_langs[values]
        popular_prog_langs = popular_prog_langs.sort_values('Frequency')
        plt.figure(figsize=(10, 8))
        plt.barh(popular_prog_langs['Prog Language'], popular_prog_langs['Frequency'])
        plt.tight_layout()
        st.pyplot(plt.gcf())

with bar_charts_tabs[2]:
    st.header('Grouped Bar Charts')
    st.write('---')
    
    add_section_title("Coming Soon... 🔜")
