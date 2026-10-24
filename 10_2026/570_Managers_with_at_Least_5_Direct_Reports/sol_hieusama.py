import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee.groupby("managerId").size()
    valid = count[count >= 5].index
    return employee[employee['id'].isin(valid)][['name']]