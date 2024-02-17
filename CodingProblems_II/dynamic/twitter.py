import requests
import re
import os

def download_x_video(tweet_url, save_path):
    # Send a GET request to the tweet URL
    response = requests.get(tweet_url)
    if response.status_code == 200:
        # Extract video URL from the response content
        match = re.search(r'(?<=<meta property="og:video" content=")(.*?)(?=")', response.text)
        if match:
            video_url = match.group(0)
            # Download the video
            with requests.get(video_url, stream=True) as r:
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print("Video downloaded successfully!")
        else:
            print("Video URL not found in the page.")
    else:
        print(f"Failed to fetch tweet page. Status code: {response.status_code}")



# Example usage
tweet_url = "https://twitter.com/TuckerCarlson/status/1755734526678925682"
save_path = "video.mp4"
download_x_video(tweet_url, save_path)



import requests
from bs4 import BeautifulSoup
import json

import re

def download_x_video(tweet_url, save_path):
    # Send a GET request to the tweet URL
    response = requests.get(tweet_url)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find the script tag containing the Twitter data
        script_tag = soup.find('script', string=re.compile('window.__INITIAL_STATE__ = '))
        if script_tag:
            # Extract the JSON data containing the tweet details
            json_data = script_tag.string.split('window.__INITIAL_STATE__ = ')[1].split(';')[0]
            # Parse JSON data
            tweet_data = json.loads(json_data)
            # Extract video URL
            video_url = tweet_data['displayTweets']['status'][tweet_url]['status']['extended_entities']['media'][0]['video_info']['variants'][0]['url']
            # Download video
            with requests.get(video_url, stream=True) as r:
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            print("Video downloaded successfully!")
        else:
            print("Couldn't find tweet data in the page.")
    else:
        print(f"Failed to fetch tweet page. Status code: {response.status_code}")

# Example usage
tweet_url = "https://twitter.com/historyinmemes/status/1755947157947916719"
save_path = "video.mp4"
download_x_video(tweet_url, save_path)
