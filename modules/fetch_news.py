import requests
from config import NEWS_URL

def fetch_news():

    response = requests.get(NEWS_URL)

    if response.status_code != 200:
        print("Failed to fetch news")
        print(response.text)
        return None

    return response.json()