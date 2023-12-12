import streamlit as st

from config import profile_pic
from config import NAME, EMAIL, DESCRIPTION

def set_sidebar():
    with st.sidebar:
        profile_container = st.container()
        profile_container.image(profile_pic, width=100)
        profile_container.title(NAME)
        profile_container.write("**Machine Learning | Artificial Intelligence | Data Science | Software Engineering | Web Development**")
        cols = profile_container.columns([0.49, 0.51], gap='small')
        with cols[0]:
            st.write(f"{EMAIL}")
        with cols[1]:
            st.link_button(f"Go to Website \t\t ↗️", f"https://sachith.streamlit.app", use_container_width=True)

def set_empty_sidebar():
    st.sidebar.write()

def st_lr_columns(lt_str, rt_str, cols=[0.5, 0.5], gap="large"):
    lt_col, rt_col = st.columns(cols, gap=gap)
    with lt_col:
        st.write(lt_str)
    with rt_col:
        st.write(rt_str)

def st_points(points):
    for point in points:
        st.write(f"- {point}")

def add_section_title(text):
    st.markdown(f"##### {text}")

def add_tab_before(text, width_adjust=[0.01, 0.99], gap='small'):
    cols = st.columns(width_adjust, gap=gap)
    with cols[1]:
        st.write(text)

def add_vertical_space(n_lines):
    for _ in range(n_lines):
        st.write("\n")
