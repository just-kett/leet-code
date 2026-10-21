import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = signups.merge(confirmations, on="user_id", how="left")
    df['confirm'] = (df['action'] == "confirmed").astype(float)
    result = df.groupby('user_id', as_index=False)['confirm'].mean()
    result['confirmation_rate'] = result['confirm'].fillna(0).round(2)
    return result[['user_id', 'confirmation_rate']]