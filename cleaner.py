import pandas as pd
def clean_data(df):
    
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['Score', 'Text'], inplace=True)
    df['Score'] = pd.to_numeric(df['Score'], errors='coerce')
    print(f"✅ Cleaned data shape: {df.shape}")
    return df
