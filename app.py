import streamlit as st
from utils import get_channel_id

def save_url(url):
    with open('urls.txt', 'a') as f:
        f.write(url + '\n')

def display_urls():
    with open('urls.txt', 'r') as f:
        urls = f.read()
    st.write(urls)

st.title('YouTube Channel/Playlist Registration')

url = st.text_input('Enter the YouTube channel or playlist URL')
if st.button('Register'):
    channel_id = get_channel_id(url)
    save_url(channel_id)
    st.success('URL registered successfully')

display_urls()
