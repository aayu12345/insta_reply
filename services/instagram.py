import requests
from config import Config

BASE_URL = "https://graph.facebook.com/v21.0"


def get_media():
    url = f"{BASE_URL}/{Config.IG_USER_ID}/media"
    params = {
        "fields": "id,comments{id,text}",
        "access_token": Config.ACCESS_TOKEN
    }
    return requests.get(url, params=params).json()


def reply_to_comment(comment_id, message):
    url = f"{BASE_URL}/{comment_id}/replies"
    return requests.post(url, params={
        "message": message,
        "access_token": Config.ACCESS_TOKEN
    }).json()


def send_dm(user_id, message):
    url = f"{BASE_URL}/me/messages"
    return requests.post(url, json={
        "recipient": {"id": user_id},
        "message": {"text": message},
        "access_token": Config.ACCESS_TOKEN
    }).json()