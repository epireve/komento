import pandas as pd
import scrapetube
from datetime import datetime

def fetch_videos(channel_id):
    try:
        existing_df = pd.read_csv('video_id.csv')
        existing_ids = existing_df['Video ID'].tolist()
    except FileNotFoundError:
        existing_ids = []

    videos = scrapetube.get_channel(channel_id)
    data = []
    for video in videos:
        vid_id = video['videoId']
        if vid_id in existing_ids:
            continue
        publishedTimeText = video["publishedTimeText"]["simpleText"]
        duration = video["lengthText"]["simpleText"]
        viewship = video["viewCountText"]["simpleText"].replace(",", "").split()[0]
        title = video["title"]["runs"][0]["text"]
        try:
            description = video["descriptionSnippet"]["runs"][0]["text"]
        except KeyError:
            description = ""
        created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data.append([channel_id, created_date, vid_id, publishedTimeText, duration, viewship, title, description])
        print(vid_id)
    df = pd.DataFrame(data, columns=['Channel ID', 'Created Date', 'Video ID', 'Published Time', 'Duration', 'Viewship', 'Title', 'Description'])
    for index, row in df.iterrows():
        print(row)
    df.to_csv('video_id.csv', index=False, mode='a')

with open('urls.txt', 'r') as f:
    for line in f:
        channel_id = line.strip().split(',')[2]
        fetch_videos(channel_id)
