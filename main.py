import streamlit as st
from streamlit_option_menu import option_menu

st.title('My project')
with st.sidebar:
    selected=option_menu(
        menu_title="Smart Screen",
        options=['Abstract','Task','System Requirements','Modules']
    )