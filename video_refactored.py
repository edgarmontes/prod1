import requests
import json
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="./.env")
api_key = os.getenv("api_key")
channel_name = os.getenv("channel_name")


def get_ID():
    try: 
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_name}&key={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        channel_items = data["items"][0]
        channel_playlistID = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]
        return channel_playlistID
    
    except requests.exceptions.RequestException as e:
        raise e
    
if __name__ == "__main__":
    print(get_ID())