import streamlit as st
from utils import get_channel_id
import pandas as pd

def save_url(channel_name, channel_id):
    with open('urls.txt', 'a') as f:
        f.write(f"TRUE,{channel_name},{channel_id}\n")

def display_urls():
    with open('urls.txt', 'r') as f:
        data = [line.strip().split(',') for line in f]
    df = pd.DataFrame(data, columns=['status', 'URL', 'Channel ID'])
    st.table(df)

st.title('YouTube Channel/Playlist Registration')

url = st.text_input('Enter the YouTube channel or playlist URL')
if st.button('Register'):
    channel_name, channel_id = get_channel_id(url)
    if channel_id is not None:
        save_url(channel_name, channel_id)
        st.success('URL registered successfully')
    else:
        st.error('Could not find channel ID')

display_urls()