import requests
import os

MATTERMOST_BOT_TOKEN = os.getenv("MATTERMOST_BOT_TOKEN")
MATTERMOST_API_URL = os.getenv("MATTERMOST_API_URL")  # e.g. https://your-mattermost.com/api/v4

def send_message_to_mattermost(channel_id: str, message: str):
    url = f"{MATTERMOST_API_URL}/posts"
    headers = {
        "Authorization": f"Bearer {MATTERMOST_BOT_TOKEN}",
        "Content-Type": "application/json",
    }
    payload = {
        "channel_id": channel_id,
        "message": message,
    }
    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
