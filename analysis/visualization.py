import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(sentiment_results):
    df = pd.DataFrame(sentiment_results)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['polarity'], bins=30, kde=True)
    plt.title('Sentiment Polarity Distribution')
    plt.xlabel('Polarity')
    plt.ylabel('Frequency')
    plt.savefig('static/polarity_distribution.png')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(df['subjectivity'], bins=30, kde=True)
    plt.title('Sentiment Subjectivity Distribution')
    plt.xlabel('Subjectivity')
    plt.ylabel('Frequency')
    plt.savefig('static/subjectivity_distribution.png')
    plt.show()
