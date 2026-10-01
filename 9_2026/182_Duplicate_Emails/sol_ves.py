import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df_filter = person.groupby('email').filter(lambda x: len(x) > 1)
    res = df_filter[['email']].drop_duplicates()
    return res