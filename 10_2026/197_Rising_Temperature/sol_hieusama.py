import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values('recordDate')
    
    temp_diff = weather['temperature'].diff()
    days_diff = weather['recordDate'].diff().dt.days
    
    return weather[(temp_diff > 0) & (days_diff == 1)][['id']]