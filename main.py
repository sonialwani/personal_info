import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("soni.jpg",width=300)
with col2:
    st.title("Sunita Alwani")
    content = """
    My name is Sunita
     
    """
    st.info(content)

