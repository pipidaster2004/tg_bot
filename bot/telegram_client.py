import json
import urllib.request
import os
from dotenv import load_dotenv


load_dotenv()


def makeRequest(metgod: str, **param) -> dict:
    json_data = json.dumps(param).encode("utf-8")
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

def getUpdates(offset: int)->dict:
    return makeRequest("getUpdates", offset=offset)


def sendMessage(chat_id: int, text: str)->dict:
    return makeRequest("sendMessage", chat_id=chat_id, text=text)

def getMe()->dict:
    return makeRequest("getMe")