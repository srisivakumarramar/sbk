import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the app
st.title("Simple Streamlit App")

# User Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

# Slider to select a number
number = st.slider("Pick a number", 1, 100, 25)
st.write(f"You selected: {number}")

# Generate Random Chart
st.subheader("Random Data Chart")
data = np.random.randn(50, 3)
df = pd.DataFrame(data, columns=["A", "B", "C"])
st.line_chart(df)

# Display an Image
st.subheader("Sample Image")
st.ima
