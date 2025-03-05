import streamlit as st
import requests
from bs4 import BeautifulSoup
import os


def main():
    st.title("Hello, Streamlit!")
    user_input = st.text_input("Enter something:")
    if st.button("Submit"):
        st.write(f"You entered: {user_input}")


if __name__ == "__main__":
    main()

# Get user inputs
website_url = st.text_input("🌍 Enter the website URL:", placeholder="https://example.com")
base_path = st.text_input("📁 Enter the directory path to save the file (e.g., D:/MyScrapedData/):")
file_name = st.text_input("📝 Enter the file name (without extension):", "extracted_links")


# Function to extract links and save with versioning
def extract_links(website_url, base_path, file_name):
    try:
        # Ensure directory exists
        if not os.path.exists(base_path):
            os.makedirs(base_path)  # Create directory if it doesn't exist

        # Fetch webpage content
        response = requests.get(website_url)
        response.raise_for_status()  # Raise error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links
        links_dict = {}
        for link in soup.find_all('a', href=True):
            text = link.get_text(strip=True) or "No Text"
            url = link['href']

            # Convert relative URLs to absolute URLs
            if not url.startswith(('http://', 'https://')):
                url = requests.compat.urljoin(website_url, url)

            links_dict[text] = url

        # Determine file versioning
        version = 1
        file_path = os.path.join(base_path, f"{file_name}_v{version}.txt")
        while os.path.exists(file_path):
            version += 1
            file_path = os.path.join(base_path, f"{file_name}_v{version}.txt")

        # Save extracted links to a file
        with open(file_path, "w", encoding="utf-8") as file:
            for subject, url in links_dict.items():
                file.write(f"{subject}: {url}\n")

        return file_path, links_dict

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error fetching the website: {e}")
        return None, None

    except PermissionError:
        st.error("❌ Permission denied! Run the script as Administrator or choose a different path.")
        return None, None

    except FileNotFoundError:
        st.error("❌ The specified path does not exist. Ensure the directory is correct.")
        return None, None


# Button to execute extraction
if st.button("🚀 Extract Links"):
    if website_url and base_path and file_name:
        file_path, extracted_links = extract_links(website_url, base_path, file_name)
        if file_path and extracted_links:
            st.success(f"✅ Extracted links have been saved to: {file_path}")

            # Provide a download button
            with open(file_path, "rb") as file:
                btn = st.download_button(
                    label="📥 Download Extracted Links",
                    data=file,
                    file_name=os.path.basename(file_path),
                    mime="text/plain"
                    
            # Display extracted links
            st.subheader("🔗 Extracted Links:")
            for subject, url in extracted_links.items():
                st.write(f"**{subject}:** {url}")
                )
    else:
        st.warning("⚠️ Please enter all required fields.")
