import streamlit as st
import langchain_helper

st.title("Your Personal Restaurant Suggestor")
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Mexican", "Mediterranian", "Italian"))

result = langchain_helper.get_resturant_name_and_menu(cuisine)
st.header(result["restaurant_name"])
st.write("**MenuItems**")

menu_items = result['menu_items'].split(',')
for item in menu_items:
    st.write("-",item)

