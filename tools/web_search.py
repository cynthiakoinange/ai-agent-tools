import requests
import os

def search_web(query: str) -> str:
    api_key = os.getenv("SERPAPI_API_KEY")
    url = f"https://serpapi.com/search.json?q={query}&api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    if "organic_results" in data and len(data["organic_results"]) > 0:
        return data["organic_results"][0]["snippet"]
    return "No results found."
