import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    mask1 = ~insurance.duplicated(subset=['lat', 'lon'], keep=False)
    mask2 = insurance.duplicated(subset=['tiv_2015'], keep=False)
    df = insurance[mask1 & mask2]
    n = len(df)
    sum = 0
    for i in range(n):
        sum += df.iloc[i, 2]
    return pd.DataFrame({
        'tiv_2016': [round(sum, 2)]
    })
