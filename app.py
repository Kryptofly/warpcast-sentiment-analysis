from analysis.sentiment_analysis import fetch_comments, analyze_sentiment
from analysis.visualization import create_visualizations
import os

def main():
    post_id = input("Enter the Warpcast post ID: ")
    comments = fetch_comments(post_id)
    sentiment_results = analyze_sentiment(comments)
    create_visualizations(sentiment_results)
    print("Sentiment analysis complete. Check the visualizations and report.")

if __name__ == '__main__':
    main()
