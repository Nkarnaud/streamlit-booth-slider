import requests
import streamlit as st

from bs4 import BeautifulSoup


about_url = "https://blackpythondevs.com/about/"

# Page layout
st.set_page_config(
        page_title='bpd',
        page_icon='🧊',
        layout='centered',
        initial_sidebar_state='expanded'
    )

def about_tab_content(url):
    '''Takes BPD about page url
    Returns <main> html content.'''

    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup.main
    else:
        return r.reason
    


st.title('Welcome to Black Python Dev Booth')
tab_list = ['Home', 'About', 'Projects & Initiatives']
home, about, projects = st.tabs(tab_list )

def page_tab():
    home.header('Black Python Devs at PyCon & how to support')

def about_tab():
    pagecontent = about_tab_content(about_url)
    about.markdown(pagecontent,unsafe_allow_html=True)
    return about

def projects_tab():
    projects.header('Our projects and some of the initiatives')

# rendering content on tabs
with home:
    page_tab()
with about:
    about_tab()
with projects:
    projects_tab()

