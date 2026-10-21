import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    tron = pd.merge(signups, confirmations, on ="user_id", how = "left")
    tron["is_confimed"] = (tron['action'] == 'confirmed').astype(int)
    result = tron.groupby("user_id", as_index = False)["is_confimed"].mean()
    result = result.rename(columns ={"is_confimed": "confirmation_rate"})
    result["confirmation_rate"] = result["confirmation_rate"].round(2)
    return result
