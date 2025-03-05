import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Function to extract links from a webpage
def extract_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # This was incorrectly indented in your code
        soup = BeautifulSoup(response.text, 'html.parser')
        links = {a.text.strip() or "No Title": a['href'] for a in soup.find_all('a', href=True)}
        return links
    except Exception as e:
        st.error(f"Error fetching links: {e}")
        return {}


# Function to save links as TXT
def save_as_txt(links, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for title, link in links.items():
            file.write(f"{title}: {link}\n")


# Function to save links as XLSX
def save_as_xlsx(links, filename):
    df = pd.DataFrame(list(links.items()), columns=["Title", "URL"])
    df.to_excel(filename, index=False)


# Function to generate a WordCloud
def generate_wordcloud(links):
    text = " ".join(links.keys())
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)
    return wordcloud


# Streamlit UI
st.markdown("<h7 style='text-align: center;font-weight: bold; color: DodgerBlue;'>Turn Any Website into Actionable Data – Extract Links & Generate Word Clouds with Ease</h7>", unsafe_allow_html=True)
# st.title("Extract Website Links & Visualize Insights in Seconds")

url = st.text_input("Enter website URL:", "https://realpython.com")

if st.button("Extract Links"):
    with st.spinner("Extracting links..."):
        links = extract_links(url)
        if links:
            st.success(f"Extracted {len(links)} links!")

            # Save files
            txt_filename = "extracted_links.txt"
            xlsx_filename = "extracted_links.xlsx"
            save_as_txt(links, txt_filename)
            save_as_xlsx(links, xlsx_filename)

            # Provide download buttons
            with open(txt_filename, "rb") as txt_file:
                st.download_button(label="Download TXT", data=txt_file, file_name=txt_filename)

            with open(xlsx_filename, "rb") as xlsx_file:
                st.download_button(label="Download XLSX", data=xlsx_file, file_name=xlsx_filename)

            # Generate and display WordCloud
            wordcloud = generate_wordcloud(links)
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
