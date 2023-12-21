import streamlit as st
import pandas as pd
import collections
import seaborn as sns

import sys
sys.path.append('../')
from util import set_sidebar, add_section_title, add_plot_title, add_vertical_space
from config import plt

set_sidebar()

sns.set()

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
    
    add_plot_title(
        plot_title='OECD Population by Year',
        dataset_url='https://stats.oecd.org/Index.aspx?DataSetCode=EDU_DEM#',
        notebook_url='https://github.com/sachith0124/data-viz-plots/blob/main/notebooks/groupedBarChart_OECDPopulation.ipynb'
    )

    #Load data
    source_filepath = 'datasets/oecd-population.csv'
    target_filepath = '../plots'
    oecd_pop_df = pd.read_csv(source_filepath)
    cols_of_interest = ['Country', 'Gender', 'Age', 'Year', 'Value']
    oecd_pop_df = oecd_pop_df[cols_of_interest]

    def create_age_groups(group_age_by):
        reference_age = 65
        ages_dict = dict()

        get_age_label = lambda *args: \
            f'{args[0]} years' if args[0] == args[1] else f'{age-group_age_by} years to {age-1} years'

        age = reference_age
        if age >= 65: 
            ages_label = ages_inds = '65 years or over'
            ages_dict[ages_inds] = ages_label
        while (age > 50):
            ages_label = get_age_label(age-group_age_by, age-1)
            ages_inds = []
            for init_age in range(age-group_age_by, age, 5):
                if init_age+5 > 50:
                    ages_inds.insert(0, f'From {init_age} to {init_age+5-1} years')
                else:
                    ages_inds.extend([f'{i} years' for i in range(init_age, init_age+5)])
            ages_dict[tuple(ages_inds)] = ages_label
            age -= group_age_by
        while(age > 0 and age >= group_age_by):
            ages_inds = [f'{i} years' for i in range(age-group_age_by, age)]
            ages_label = f'{get_age_label(age-group_age_by, age-1)}'
            ages_dict[tuple(ages_inds)] = ages_label
            age -= group_age_by
        if age > 0:
            ages_label = f'below {age} years'
            ages_inds = [f'{i} years' for i in range(0, age)]
            ages_dict[tuple(ages_inds)] = ages_label

        return ages_dict
    
    def replace_column_names(col_name, group_age_by):
        ref_dict = create_age_groups(group_age_by)
        for key, label in ref_dict.items():
            if col_name in key:
                return label

    cols = st.columns([0.2, 0.2, 0.6], gap='medium')
    with cols[0]:
        #Add st.selectbox to select country
        countries = oecd_pop_df['Country'].unique()
        country = st.selectbox('**Country:**', countries)
        oecd_pop_df = oecd_pop_df.query('Country == @country').drop(['Country'], axis=1)
    with cols[1]:
        add_vertical_space(2)
        #Add st.toogle to show gender ratio within each bars
        show_gender = st.toggle('**Gender**', value=True)
        genders = ['Male', 'Female'] if show_gender else ['Total']
        oecd_pop_df = oecd_pop_df.query('Gender in @genders')
    with cols[2]:
        #Add st.slider to set age group bin width: 1 to max(age)
        ages = range(0, 75)
        group_age_by = st.select_slider('**Group Age by Yrs:**', value=15, options=[5, 10, 15, 20])
        age_groups = list(create_age_groups(group_age_by).values())
        oecd_pop_df['Age'] = oecd_pop_df['Age'].apply(replace_column_names, group_age_by=group_age_by)
        oecd_pop_df = oecd_pop_df.loc[oecd_pop_df['Age'].isin(age_groups)]
        oecd_pop_df = oecd_pop_df.groupby(['Year', 'Age'])['Value'].sum()

    # oecd_pop_df.unstack().plot(type='bar')
    fig, ax = plt.subplots()

    oecd_pop_df.unstack().plot(kind='bar', width=0.9, figsize=(10, 6), ax=ax)

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Value')
    fig.set_figheight(10)
    fig.set_figwidth(15)

    st.pyplot(fig)
