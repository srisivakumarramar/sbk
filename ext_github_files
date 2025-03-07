import streamlit as st
import requests

def get_github_filenames(owner, repo, branch="main"):
    url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return [file['path'] for file in data.get('tree', []) if file['type'] == 'blob']
    else:
        return []

def main():
    st.title("GitHub Repository File Extractor")
    
    owner = st.text_input("Enter GitHub Username/Organization", "octocat")
    repo = st.text_input("Enter Repository Name", "Hello-World")
    branch = st.text_input("Enter Branch Name", "main")
    
    if st.button("Fetch Filenames"):
        filenames = get_github_filenames(owner, repo, branch)
        if filenames:
            st.write("### List of Files:")
            st.write(filenames)
        else:
            st.error("Failed to fetch filenames. Check the repository details.")

if __name__ == "__main__":
    main()
