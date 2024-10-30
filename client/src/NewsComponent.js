import React, { useState } from 'react';
import './NewsCard.css';

function NewsComponent() {
    const [query, setQuery] = useState('');
    const [newsData, setNewsData] = useState([]);

    const handleSearch = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5000/scrape', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query }),
            });
            const data = await response.json();
            setNewsData(data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
            <input
                type="text"
                placeholder="Search for news..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={handleSearch}>Search</button>

            <div className="news-container">
                {newsData.map((news, index) => (
                    <div className="news-card" key={index}>
                        <img src={news.image} alt={news.title} className="news-image" />
                        <div className="news-content">
                            <h2 className="news-title">{news.title}</h2>
                            <p className="news-description">{news.description}</p>
                            <a href={news.url} target="_blank" rel="noopener noreferrer" className="read-more">
                                Read More
                            </a>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default NewsComponent;
