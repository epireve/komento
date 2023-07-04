import streamlit as st
from utils import get_channel_id

def save_url(url):
    with open('urls.txt', 'a') as f:
        f.write(url + '\n')

import pandas as pd

def display_urls():
    with open('urls.txt', 'r') as f:
        data = [line.strip().split(',') for line in f]
    df = pd.DataFrame(data, columns=['URL', 'Channel ID'])
    st.table(df)

st.title('YouTube Channel/Playlist Registration')

url = st.text_input('Enter the YouTube channel or playlist URL')
if st.button('Register'):
    channel_id = get_channel_id(url)
    if channel_id is not None:
        save_url(f"{url}, {channel_id}")
        st.success('URL registered successfully')
    else:
        st.error('Could not find channel ID')

display_urls()