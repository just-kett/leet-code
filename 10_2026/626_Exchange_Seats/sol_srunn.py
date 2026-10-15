import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    df = seat.copy()
    n = len(df)

    students = df["student"].values

    for i in range(0,n-1,2):
        students[i],students[i+1] = students[i+1],students[i]
    df["student"] = students
    return df
