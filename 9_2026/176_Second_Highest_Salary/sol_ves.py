import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted = employee['salary'].drop_duplicates().sort_values(ascending = False)
    if len(sorted) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        res = sorted.iloc[1]
    return pd.DataFrame({'SecondHighestSalary': [res]})
#-1 bim bim dau cac kett
