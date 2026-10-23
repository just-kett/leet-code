import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee.groupby('managerId').size().reset_index(name='manager')
    managers = count[count['manager'] >= 5]
    result = employee[employee['id'].isin(managers['managerId'])][['name']]
    return result