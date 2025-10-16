import json
import urllib.request
import os
from dotenv import load_dotenv


load_dotenv()


def makeRequest(metgod: str, **params) -> dict:
    json_data = json.dumps(params).encode("utf-8")
    request = urllib.request.Request(
        method = "POST",
        url = f"{os.getenv("TELEGRAM_BASE_URI")}/{metgod}",
        data = json_data,
        headers={
            "Content-Type": "application/json"
        }
    )
    with urllib.request.urlopen(request) as responce:
        responce_body = responce.read().decode("utf-8")
        responce_json = json.loads(responce_body)
        assert responce_json["ok"] == True
        return responce_json["result"]

def getUpdates(**params)->dict:
    return makeRequest("getUpdates", **params)


def sendMessage(chat_id: int, text: str, **params)->dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text, **params)

def sendPhoto(chat_id, photo=None, caption=None, **params) -> dict:
    if photo is not None:
        params["photo"] = photo
    return makeRequest("sendPhoto", chat_id=chat_id, **params)

def getMe()->dict:
    return makeRequest("getMe")