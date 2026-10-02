import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee_sorted = employee["salary"].drop_duplicates().sort_values(ascending=False)
    if N <= 0 or len(employee_sorted) < N:
        getNthHighestSalary = None
    else:
        getNthHighestSalary = employee_sorted.iloc[N - 1]
    return pd.DataFrame({
        f"getNthHighestSalary({N})": [getNthHighestSalary]
    })
