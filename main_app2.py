

import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports 
from multiapp import MultiPage
from pages import home3,news3 # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
display = Image.open('stock.jpg')
display = np.array(display)
st.title("Stock Dasboard")
st.image(display, width = 400)



# Add all your application here
app.add_page("Home", home3.app)
app.add_page("News", news3.app)


# The main app
app.run()

        