import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    l = len(logs)
    if logs.empty:
        return pd.DataFrame(columns=['ConsecutiveNums'])
    cur = logs.iloc[0, 1]
    count = 0
    k = []
    for i in range(l):
        if logs.iloc[i, 1] == cur:
            count += 1
            if count == 3 and cur not in k:
                k.append(cur)  
        else:
            cur = logs.iloc[i, 1]
            count = 1
    return pd.DataFrame(k, columns=['ConsecutiveNums'])