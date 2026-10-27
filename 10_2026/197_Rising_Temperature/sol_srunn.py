import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather["recordDate"] = pd.to_datetime(weather["recordDate"])
    weather = weather.sort_values("recordDate").reset_index(drop=True)
    res = []
    for i in range(1,len(weather)):
        curr_date = weather.loc[i,"recordDate"]
        prev_date = weather.loc[i-1,"recordDate"]

        curr_temp = weather.loc[i,"temperature"]
        prev_temp = weather.loc[i-1,"temperature"]

        if (curr_date - prev_date).days == 1 and curr_temp > prev_temp:
            res.append(weather.loc[i,"id"])
    return pd.DataFrame({"id" : res})
    
