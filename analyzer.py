def get_rating_distribution(df):
   
    return df['Score']

def get_top_reviewers(df, n=10):
   
    return df['ProfileName'].value_counts().head(n)

def get_helpful_reviews(df, n=10):

    df = df.copy()
    df['helpfulness_ratio'] = df['HelpfulnessNumerator'] / df['HelpfulnessDenominator'].replace(0, 1)
    return df.sort_values('helpfulness_ratio', ascending=False)[['ProfileName', 'Summary', 'helpfulness_ratio']].head(n)
