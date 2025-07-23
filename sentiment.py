from textblob import TextBlob

def analyze_sentiment(df):
   
    df = df.copy()
    df['sentiment'] = df['Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    sentiment_summary = df['sentiment'].describe()
    return df, sentiment_summary
