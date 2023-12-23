import streamlit as st
import pandas as pd
import numpy as np
import collections
import seaborn as sns
import re

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
    #Add Title
    add_plot_title(
        plot_title='International Trade: \nTrade Balance as Imports and Exports from 1988 to 2021', 
        dataset_url='https://wits.worldbank.org/CountryProfile/en/Country/WLD/Year/2021/TradeFlow/EXPIMP/Partner/all/Product/Total#', 
        notebook_url='https://github.com/sachith0124/data-viz-plots/blob/main/notebooks/bar-chart_vertical_wits-imports-exports.ipynb'
    )

    #Load Data
    wits_imports_exports = pd.read_csv('datasets/wits-imports-exports.csv')
    

    cols = st.columns([0.3, 0.4, 0.3], gap='medium')
    with cols[0]:
        #Add st.selectbox to select country
        countries = wits_imports_exports['Country'].unique()
        selected_country = st.selectbox('**Country:**', countries, index=3)
        country_imports_exports = wits_imports_exports.query('Country == @selected_country').drop('Country', axis=1)
    
    with cols[2]:
        add_vertical_space(2)
        show_imports_exports = st.toggle('Show Imports / Exports', value=False)

    thousand_to_million_round2 = lambda n: np.round(n / 1000, 2)
    country_imports_exports['Export in US$ Millions'] = country_imports_exports['Export (US$ Thousand)'].apply(thousand_to_million_round2)
    country_imports_exports.drop('Export (US$ Thousand)', axis=1, inplace=True)
    country_imports_exports['Import in US$ Millions'] = country_imports_exports['Import (US$ Thousand)'].apply(thousand_to_million_round2)
    country_imports_exports.drop('Import (US$ Thousand)', axis=1, inplace=True)

    new_df = pd.DataFrame(columns=['Year', 'Export or Import', 'Value in US$ Millions'])
    for year in country_imports_exports['Year']:
        export_value = country_imports_exports.query('Year == @year')['Export in US$ Millions'].iloc[0]
        import_value = -country_imports_exports.query('Year == @year')['Import in US$ Millions'].iloc[0]
        trade_value = export_value + import_value

        export_row = {'Year': year, 'Export or Import': 'Export', 'Value in US$ Millions': export_value, 'Trade Balance':trade_value}
        import_row = {'Year': year, 'Export or Import': 'Import', 'Value in US$ Millions': import_value, 'Trade Balance':trade_value}
        
        new_df = pd.concat([new_df, pd.DataFrame([export_row, import_row])])

    if show_imports_exports:
        st.bar_chart(new_df, x='Year', y='Value in US$ Millions', color='Export or Import', use_container_width=True)
    else:
        st.bar_chart(new_df, x='Year', y='Trade Balance')


with bar_charts_tabs[1]:
    st.header('Horizontal Bar Charts')
    st.write('---')

    add_plot_title(
        plot_title= 'Popular Programming Languages: Frequency Plot',
        dataset_url='https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/02-BarCharts/data.csv', 
        notebook_url='https://github.com/sachith0124/data-viz-plots/blob/main/notebooks/bar-chart_horizontal_prog-languages.ipynb'
    )
    
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
        notebook_url='https://github.com/sachith0124/data-viz-plots/blob/main/notebooks/bar-chart_grouped_oecd-population.ipynb'
    )

    #Load data
    source_filepath = 'datasets/oecd-population.csv'
    target_filepath = '../plots'
    oecd_pop_df = pd.read_csv(source_filepath)
    cols_of_interest = ['Country', 'Gender', 'Age', 'Year', 'Value']
    oecd_pop_df = oecd_pop_df[cols_of_interest]
    oecd_pop_df = oecd_pop_df[oecd_pop_df['Gender'] == 'Total']

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

    cols = st.columns([0.2, 0.6, 0.2], gap='medium')
    with cols[0]:
        #Add st.selectbox to select country
        countries = oecd_pop_df['Country'].unique()
        selected_country = st.selectbox('**Country:**', countries, index=3)
        oecd_pop_df = oecd_pop_df.query('Country == @selected_country').drop(['Country'], axis=1)
    with cols[1]:
        #Add st.slider to set age group bin width: 1 to max(age)
        ages = range(0, 75)
        group_age_by = st.select_slider('**Group Age by Yrs:**', value=10, options=[5, 10, 15, 20, 25])
        
        #preprocessing for groupby step
        age_groups = list(create_age_groups(group_age_by).values())
        oecd_pop_df['Age'] = oecd_pop_df['Age'].apply(replace_column_names, group_age_by=group_age_by)
        oecd_pop_df = oecd_pop_df.loc[oecd_pop_df['Age'].isin(age_groups)]

        get_nums = lambda str: tuple([int(match) for match in re.findall(r'\d+', str)])
        oecd_pop_df['tempAge'] = oecd_pop_df['Age'].apply(get_nums)
    with cols[2]:
        #Add st.toogle to enable or disable population before 65 years
        add_vertical_space(2)
        include_65_above = st.toggle('**65 yrs above**', value=False)
        if not include_65_above:
            oecd_pop_df = oecd_pop_df[oecd_pop_df['tempAge'] != (65,)]
        oecd_pop_df = oecd_pop_df.sort_values(['Year', 'tempAge'])

        ages_list = oecd_pop_df['Age'].unique()

    oecd_pop_df = oecd_pop_df.groupby(['Year', 'tempAge', 'Age'])['Value'].sum()
    oecd_pop_df = oecd_pop_df.sort_index(level=[0, 1]).droplevel('Age')
    df_plot = oecd_pop_df.unstack().sort_index(level=1, axis=1)

    # Plotting
    fig, ax = plt.subplots()
    ax = df_plot.plot(kind='bar', width=0.9, figsize=(10, 6), rot=45)

    ax.set_ylabel('Population')
    ax.set_title(f'Population by Year and Age Group for {selected_country}')
    y_ticks = ['1,000,000', '2,000,000', '3,0000,00', '4,000,000', '5,000,000', '6,000,000', '7,000,000', '8,000,000', '9,000,000', '10,000,000']
    ax.set_yticklabels(y_ticks)

    # Adding legend
    plt.legend(title='Age Group', bbox_to_anchor=(1, 1), labels=ages_list)

    st.pyplot(plt)
