# News Scraper

A simple news scraper that retrieves the latest news articles based on a search query using the [News API](https://newsapi.org/). This application allows users to enter a query and fetch relevant news articles along with their titles, descriptions, images, and URLs.

## Features

- **Search News**: Users can input a query to fetch news articles.
- **Fetch Articles**: The scraper retrieves articles from News API and formats them for display.
- **No API Key Required**: The implementation does not require an API key for basic usage, allowing easy access to news data.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- `requests` library (Install using `pip install requests`)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/news-scraper.git
   cd news-scraper
   ```

2. **Install required packages:**
   ```bash
   pip install requests
   ```

### Usage

To use the news scraper, you can run the script in a Python environment. The `scrape_news` function accepts a query string and returns a list of articles related to that query.

```python
import requests

def scrape_news(query):
    api_key = 'your_api_key_here'  # Replace with your News API key
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
```

### Example Usage

Here’s how you can use the `scrape_news` function to fetch the latest technology news:

```python
news_articles = scrape_news("latest technology")
for article in news_articles:
    print(article)
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

### Acknowledgements

- [News API](https://newsapi.org/) for providing access to news articles.

```

