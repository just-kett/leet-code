def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    no_confirm = signups[~signups["user_id"].isin(confirmations["user_id"])][["user_id"]]
    no_confirm["confirmation_rate"] = 0.00

    has_confirm = confirmations.groupby("user_id")["action"].apply(
        lambda x : (x == "confirmed").mean()
    ).round(2).reset_index(name="confirmation_rate")
    res = pd.concat([has_confirm,no_confirm],ignore_index=True)
    return res
