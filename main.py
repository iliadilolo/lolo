import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("gitava.png", width=400)

with col2:
    st.title("Lolita Iliadi")
    content1 = """
    Hello there! I'm a Lola, 23 years old, I am deeply passionate 
    about learning Python. I've embarked on a thrilling journey to master 
    this programming language, and I've created this portfolio 
    website as a platform to showcase my coding skills and projects.
    
    """
    st.info(content1)

content2 = '''
Below you can find some of the apps I have built in Python. 
Feel free to contact me!
'''
st.write(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])