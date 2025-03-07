import streamlit as st
import requests

# Function to get filenames from GitHub
def get_github_filenames(owner, repo, branch="main"):
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return [{"path": file['path'], "url": f"https://github.com/{owner}/{repo}/blob/{branch}/{file['path']}"} 
                for file in data.get('tree', []) if file['type'] == 'blob']
    else:
        return []

# Streamlit App
def main():
    st.set_page_config(page_title="GitHub File Viewer", layout="wide")

    st.title("View Your GitHub Files Instantly!")
    st.write("Enter a GitHub repository to fetch and view all its files.")

    owner = st.text_input("GitHub Username/Organization", "srisivakumarramar")
    repo = st.text_input("Repository Name", "sbk")
    branch = st.text_input("Branch Name", "main")

    if st.button("Fetch Files"):
        filenames = get_github_filenames(owner, repo, branch)
        if filenames:
            st.write("### List of Files:")
            for file in filenames:
                st.markdown(f"- [{file['path']}]({file['url']})")  # Clickable file links
        else:
            st.error("Failed to fetch filenames. Check repository details.")

if __name__ == "__main__":
    main()
