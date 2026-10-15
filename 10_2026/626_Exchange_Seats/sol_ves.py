import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat = seat.sort_values(by='id').reset_index(drop=True)
    swapped_students = seat['student'].copy()
    swapped_students.iloc[0:len(seat)//2*2:2] = seat['student'].iloc[1:len(seat)//2*2:2].values
    swapped_students.iloc[1:len(seat)//2*2:2] = seat['student'].iloc[0:len(seat)//2*2:2].values
    seat['student'] = swapped_students
    return seat