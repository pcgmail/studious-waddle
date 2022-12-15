import streamlit
import pandas
streamlit.title('Test App')
streamlit.header('Breakfast Menu')
streamlit.text('🐔 Bacon & eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
