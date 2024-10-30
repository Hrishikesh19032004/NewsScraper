from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_news

app = Flask(__name__)
CORS(app)  # Enable CORS to allow requests from frontend

@app.route('/scrape', methods=['POST'])
def scrape():
    query = request.json.get('query')
    data = scrape_news(query)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
