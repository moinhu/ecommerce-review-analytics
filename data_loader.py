import pandas as pd
def load_data(filepath):
   
    try:
        df = pd.read_csv(filepath, encoding='latin1')
        print(f"✅ Data loaded successfully with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
