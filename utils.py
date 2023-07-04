import re

def get_channel_id(url):
    pattern = r'((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)'
    match = re.search(pattern, url)
    if match:
        return match.group()
    return None
