import googleapiclient.discovery
import re

def get_channel_id(url):
    # Extract the channel name from the URL using a regular expression
    match = re.search(r'/user/([^/]+)', url)
    if match:
        channel_name = match.group(1)
    else:
        match = re.search(r'/channel/([^/]+)', url)
        if match:
            channel_name = match.group(1)
        else:
            channel_name = url

    # Call the YouTube Data API to search for the channel
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyCJ14NIQl3MQgwayvg2vSyV5Pj0E9wj-Zk")
    request = youtube.search().list(
        part="id",
        q=channel_name,
        type="channel",
        maxResults=1
    )
    response = request.execute()

    # Extract the channel ID from the search results
    if len(response['items']) == 1:
        # print(response)
        return response['items'][0]['id']['channelId']
    else:
        return None