import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    sort = logs.sort_values(by='id')
    consecutive = (sort['num'] == sort['num'].shift(1)) & (sort['num'] == sort['num'].shift(2))
    res = sort[consecutive][['num']].drop_duplicates()
    return res.rename(columns={'num': 'ConsecutiveNums'}) 