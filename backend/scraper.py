import requests

def scrape_news(query):
    api_key = 'a6db5072ef9e42379e38494506131571'  # Replace with your News API key
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        news_data = response.json()

        articles = news_data.get('articles', [])
        formatted_data = []

        for article in articles:
            title = article.get('title', 'No Title')
            description = article.get('description', 'No description')
            image_url = article.get('urlToImage', 'No Image')
            url = article.get('url', '#')

            formatted_data.append({
                "title": title,
                "description": description,
                "image": image_url,
                "url": url
            })

        return formatted_data

    except Exception as e:
        print(f"Error accessing news data: {e}")
        return []

# Example usage
news_articles = scrape_news("latest technology")
for article in news_articles:
    print(article)
