import streamlit
import pandas

streamlit.title("Hello world")

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



df= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
df=df.set_index("Fruit")

fs=streamlit.multiselect("Pick some fruit:", list(df.index),['Avacoda','Strawberries'])
fts=df.loc[fs]
#streamlit.dataframe(fts)
