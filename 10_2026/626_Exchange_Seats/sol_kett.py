import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    n = len(seat)
    for i in range (0, n - 1, 2):
        seat.iloc[[i, i + 1], 1] = seat.iloc[[i + 1, i], 1].values
    return seat