import requests
from textblob import TextBlob
from config import WARPCAST_API_TOKEN, WARPCAST_API_ENDPOINT

def fetch_comments(post_id):
    url = f"{WARPCAST_API_ENDPOINT}/posts/{post_id}/comments"
    headers = {
        'Authorization': f'Bearer {WARPCAST_API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    return response.json().get('data', [])

def analyze_sentiment(comments):
    results = []
    for comment in comments:
        text = comment.get('text')
        sentiment = TextBlob(text).sentiment
        results.append({
            'text': text,
            'polarity': sentiment.polarity,
            'subjectivity': sentiment.subjectivity
        })
    return results
