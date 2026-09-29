import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department = department.rename(columns={'id':'departmentId', 'name':'Department'})
    df  = department.merge(employee, on='departmentId', how='inner')
    df = df.rename(columns={'salary': 'Salary', 'name': 'Employee'})
    df_max = df.groupby('Department', group_keys=False).apply(lambda x: x.nlargest(1, 'Salary', keep='all'))
    return df_max[['Department', 'Employee', 'Salary']]

    