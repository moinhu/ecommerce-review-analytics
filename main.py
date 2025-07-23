"""
main.py – Orchestrates data loading, cleaning, analysis, visualization, and reporting
"""

from data_loader import load_data
from cleaner import clean_data
from analyzer import get_rating_distribution, get_top_reviewers, get_helpful_reviews
from sentiment import analyze_sentiment
from visualizer import plot_hist, plot_bar
from utils import export_summary_to_excel

def main():
    df = load_data("data/amazon.csv")

   

    df = clean_data(df)

    # Analysis
    ratings = get_rating_distribution(df)
    top_users = get_top_reviewers(df)
    helpful_reviews = get_helpful_reviews(df)

    # Visuals
    plot_hist(ratings, "Rating Distribution", "Rating", "Number of Reviews", color="green")
    plot_bar(top_users, "Top Reviewers by Count", "Users", "Review Count", color="blue")

    # Sentiment
    df, sentiment_summary = analyze_sentiment(df)
    print("\n🟣 Sentiment Summary (Polarity Stats):")
    print(sentiment_summary)

    # Export summary
    summary = {
        "Top Users": top_users,
        "Helpful Reviews": helpful_reviews.set_index('ProfileName')['helpfulness_ratio'],
        "Sentiment Summary": sentiment_summary
    }
    export_summary_to_excel(summary)

 
    print("\n🔵 Top Reviewers:")
    print(top_users)

    print("\n🟢 Most Helpful Reviews:")
    print(helpful_reviews[['ProfileName', 'Summary', 'helpfulness_ratio']])

    print("\n🔴 Top 5 Most Positive Reviews:")
    print(df.sort_values('sentiment', ascending=False)[['Summary', 'Text', 'sentiment']].head(5))

    print("\n⚫ Top 5 Most Negative Reviews:")
    print(df.sort_values('sentiment')[['Summary', 'Text', 'sentiment']].head(5))

if __name__ == "__main__":
    main()
