import urllib3 as curl
import json


def fetch(url: str) -> str:
    res = curl.request("GET", url)

    if res.status != 200:
        raise Exception(f"HTTP error: {res.status}")

    return res.data.decode()


def fetch_json(url: str) -> dict:
    res = curl.request("GET", url)

    if res.status != 200:
        raise Exception(f"HTTP error: {res.status}")

    raw_data = res.data.decode("utf-8")

    return json.loads(raw_data)
