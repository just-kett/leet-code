import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(sorted) < 2:
        second_highest = None
    else:
        second_highest = sorted.iloc[1]
    result = pd.DataFrame([second_highest], columns=['SecondHighestSalary'])
    return result
    