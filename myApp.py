import streamlit as st

st.write('Good Morning')
st.write('Hello, from SHRDC')
st.header('Line 1')
st.subheader('Line 2')
st.caption('Line 3')

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown(''':red[Streamlit] :orange[is] :green[fun]''')
st.markdown("Here's a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

new_title ='<p style="font-family:sans-serif; color:Green; font-size:42px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True)

select1 = st.selectbox("Kuala Lumpur is located at", 
             ['Malaysia', 'Thailand', 'UK'])

st.write("you have selected:", select1)

st.multiselect("Select 2 states", 
               ['Selangor', 'Johor', 'Kedah'])

c1 = st.button("Click Me")
if c1:
    st.write("You have clicked the button")

st.slider("Select length of stay", 1,10, value=3)

number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is", number)

from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=500)

import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

st.bar_chart(df, x="Location", y="Income")
st.line_chart(df, x="Household", y="Income")
st.scatter_chart(df, x="Household", y="Income")

tab1, tab2, tab3 =st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("A Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("A Owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")


with col1:
    st.write("")
with col2:
    st.header("A Dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.write("")