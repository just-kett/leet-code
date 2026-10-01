import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    mask = person.duplicated(subset=['email'], keep='first')
    result = person[mask][['email']].drop_duplicates()
    return result