import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=500)

with col2:
    st.title("Lolita Iliadi")
    content = """
    Hello there! I'm a Lola, 23 years old, I am deeply passionate 
    about learning Python. I've embarked on a thrilling journey to master 
    this programming language, and I've created this portfolio 
    website as a platform to showcase my coding skills and projects.
    
    """
    st.info(content)