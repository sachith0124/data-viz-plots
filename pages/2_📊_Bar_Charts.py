import streamlit as st
import pandas as pd
import collections

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title, add_checkboxes_in_cols
from config import plt

set_sidebar()

#--- BAR CHART ---
header = st.container()
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)
header.header('Bar Charts')
header.write("---")

bar_charts_tabs = st.tabs(["Vertical", "Horizontal", "Grouped"], )
with bar_charts_tabs[1]:
    st.header('Horizontal Bar Charts')
    st.write('---')
    add_section_title('Popular Programming Languages')
    source_filepath = 'datasets/prog_langs.csv'
    prog_langs_df = pd.read_csv(source_filepath)

    language_counter = collections.Counter()

    update_language_counter = lambda reponse: language_counter.update(reponse.split(';'))
    prog_langs_df['LanguagesWorkedWith'].apply(update_language_counter)

    popular_prog_langs = pd.DataFrame(columns=['Prog Language', 'Frequency'])

    for item in language_counter.most_common():
        popular_prog_langs.loc[len(popular_prog_langs)] = item

    plot_spot = st.empty()

    with st.expander('Select Programming Langugages'):
        values = add_checkboxes_in_cols(list(popular_prog_langs['Prog Language']), n_columns=4)

    with plot_spot:
        popular_prog_langs = popular_prog_langs[values]
        popular_prog_langs = popular_prog_langs.sort_values('Frequency')
        plt.barh(popular_prog_langs['Prog Language'], popular_prog_langs['Frequency'])
        plt.tight_layout()

        # st.bar_chart(popular_prog_langs[values], x='Prog Language', y='Frequency')
        st.pyplot(plt.gcf())