import streamlit as st
import pandas as pd
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

content2="Please feel free to reach out to me in case of any help or guidance"

st.write(content2)

df = pd.read_csv("data (1).csv",sep=";")

col3, col4 = st.columns(2)




with col3:
  for i in range (0,11):
        st.header(df['title'][i])
        st.write(df['description'][i])
        st.image(df['image'][i])
        st.write("[APP](https://sonialwani.github.io/todo-app/)")

with col4:
  for i in range (11,20):
        st.header(df['title'][i])
        st.write(df['description'][i])
        st.image(df['image'][i])
        st.write("[APP](https://sonialwani.github.io/todo-app/)")