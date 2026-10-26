import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer['visited_on'] = pd.to_datetime(customer['visited_on'])
    df = customer.groupby('visited_on')['amount'].sum().reset_index()
    
    df = df.set_index('visited_on').resample('D').sum().reset_index()
    
    df['amount'] = df['amount'].rolling(window=7).sum()
    df['average_amount'] = (df['amount'] / 7).round(2) # hoặc dùng .rolling(7).mean().round(2)
    
    df = df.iloc[6:].copy()
    df['visited_on'] = df['visited_on'].dt.strftime('%Y-%m-%d')
    
    return df
