import requests
from settings import NEWS_API_KEY

def fetch_news(category="technology", country="us"):
    url = (
        f"https://newsapi.org/v2/top-headlines?category={category}&country={country}&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data.get("articles", [])[:5]:
        articles.append({
            "title": article["title"],
            "description": article["description"],
            "source": article["source"]["name"]
        })
    
    return articles
