import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee_sorted=employee["salary"].drop_duplicates().sort_values(ascending=False)
    if len(employee_sorted) <2:
        second_salary = None
    else:
        second_salary = employee_sorted.iloc[1]
    return pd.DataFrame({"SecondHighestSalary": [second_salary]})
    