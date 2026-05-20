import requests
from modules.config import API_KEY

def fetch_news():

    url = (
        f"https://newsapi.org/v2/top-headlines?"
        f"country=us&apiKey={API_KEY}"
    )

    response = requests.get(url)

    return response.json()