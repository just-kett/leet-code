import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sorted = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted) < N:
        Nth_highest = None
    elif N <= 0:
        Nth_highest = None
    else:
        Nth_highest = sorted.iloc[N - 1] 
    result = pd.DataFrame([Nth_highest], columns=[f"getNthHighestSalary({N})"])
    return result