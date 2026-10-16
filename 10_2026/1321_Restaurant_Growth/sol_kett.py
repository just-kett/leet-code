import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer.groupby('visited_on').agg({
        'amount': 'sum'
    }).reset_index()
    df = df.sort_values('visited_on').reset_index(drop=True)
    result = []
    n = len(df)
    for i in range(6, n):
        date = df.loc[i, 'visited_on']
        sum_amount = df.loc[i - 6: i, 'amount'].sum()
        average_amount = round(sum_amount / 7, 2)
        result.append({
            'visited_on': date,
            'amount': sum_amount,
            'average_amount': average_amount
        })
    return pd.DataFrame(result)
        
