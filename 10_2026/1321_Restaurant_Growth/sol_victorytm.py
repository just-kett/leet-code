import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    sort = customer.sort_values('visited_on')
    tmp = sort.groupby('visited_on')["amount"].sum()
    dates = []
    amounts = []
    averages = []
    for i in range(6, len(tmp)):
        window = tmp.iloc[i - 6:i + 1]
        total = window.sum()
        average = round(total / 7, 2)
        dates.append(tmp.index[i])
        amounts.append(total)
        averages.append(average)
    return pd.DataFrame({
        "visited_on": dates,
        "amount": amounts,
        "average_amount": averages
    })
    