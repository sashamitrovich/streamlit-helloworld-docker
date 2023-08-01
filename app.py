import streamlit as st

name = st.text_input("What's your name, sir?","Tim")

st.write(f"# Hello, {name}, how are you? :sunglasses:")