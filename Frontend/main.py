import streamlit as st
import requests

base_url="http://127.0.0.1:8000"

st.header("My Contacts")
tabs=st.tabs(['Contacts'])
with tabs[0]:
    res=requests.get(base_url + '/contacts')
    Contacts=res.json()
    st.data_editor(Contacts)




