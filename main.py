from fastapi import FastAPI, HTTPException
from utils.fetch import fetch
import json
import os

app = FastAPI()

# todo: remove api keys
api_key: str | None = os.getenv("API_KEY")


@app.get("/")
def read_root():
    return {"Hello": "World"}


def getCountryAndCity(ip: str) -> tuple[str, str]:
    latitude = fetch(f"https://ipapi.co/{ip}/latitude/")
    longitude = fetch(f"https://ipapi.co/{ip}/longitude/")

    return latitude, longitude


@app.get("/getTemperature/{ip}")
def getTemperature(ip):
    if api_key is None:
        raise HTTPException(
            status_code=403, detail="Please set an API_KEY variable in your environment"
        )

    [latitude, longitude] = getCountryAndCity(ip)
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"

    data: dict = json.loads(fetch(url))
    temp = data["main"]["temp"]

    return {"temperature": temp}
