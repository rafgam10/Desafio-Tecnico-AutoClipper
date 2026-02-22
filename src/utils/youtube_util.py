import os
import requests

API_KEY = os.getenv("KEY_API_YOUTUBE")
BASE_URL = "https://www.googleapis.com/youtube/v3"


def get_channel_id(channel_name):
    url = f"{BASE_URL}/search"
    params = {
        "part": "snippet",
        "q": channel_name,
        "type": "channel",
        "maxResults": 1,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    items = data.get("items")
    if not items:
        return None

    return items[0]["snippet"]["channelId"]


def get_uploads_playlist_id(channel_id):
    url = f"{BASE_URL}/channels"
    params = {
        "part": "contentDetails",
        "id": channel_id,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    items = data.get("items")
    if not items:
        return None

    return items[0]["contentDetails"]["relatedPlaylists"]["uploads"]


def get_video_ids_from_playlist(playlist_id, max_results=10):
    url = f"{BASE_URL}/playlistItems"
    params = {
        "part": "snippet",
        "playlistId": playlist_id,
        "maxResults": max_results,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    video_ids = []

    for item in data.get("items", []):
        video_id = item["snippet"]["resourceId"]["videoId"]
        video_ids.append(video_id)

    return video_ids


def get_video_details(video_ids):
    url = f"{BASE_URL}/videos"
    params = {
        "part": "snippet,statistics,contentDetails",
        "id": ",".join(video_ids),
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    videos = []

    for item in data.get("items", []):
        snippet = item.get("snippet", {})
        statistics = item.get("statistics", {})
        content_details = item.get("contentDetails", {})

        videos.append({
            "title": snippet.get("title"),
            "description": snippet.get("description"),
            "tags": snippet.get("tags", []),
            "publish_date": snippet.get("publishedAt"),
            "views": statistics.get("viewCount", 0),
            "likes": statistics.get("likeCount", 0),
            "comment_count": statistics.get("commentCount", 0),
            "duration": content_details.get("duration")
        })

    return videos