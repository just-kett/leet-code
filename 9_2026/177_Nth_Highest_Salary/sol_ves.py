import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    col_name = f'getNthHighestSalary({N})'
    sorted = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if len(sorted) < N or N <= 0:
        return pd.DataFrame ({col_name: [None]})
    res = sorted.iloc[N-1]
    return pd.DataFrame ({col_name: [res]})
