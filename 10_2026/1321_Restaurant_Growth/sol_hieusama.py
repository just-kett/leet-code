import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer = customer.sort_values('visited_on')
    Loc = customer.groupby("visited_on")["amount"].sum()
    amount = Loc.rolling(7).sum()
    average_amount = (amount/7).round(2)

    df = pd.DataFrame({
        'visited_on': Loc.index,
        'amount':amount,
        'average_amount':average_amount
    })
    df = df.dropna()
    return df