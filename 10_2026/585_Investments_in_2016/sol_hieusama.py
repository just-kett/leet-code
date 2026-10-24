import pandas as pd
def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:  
    duplicated_tiv_2015 = insurance["tiv_2015"].duplicated(keep=False)
    unique_location = ~insurance.duplicated(subset=["lat", "lon"], keep=False)
    valid_records = insurance[duplicated_tiv_2015 & unique_location]
    total_tiv_2016 = round(valid_records["tiv_2016"].sum(), 2)
    return pd.DataFrame({"tiv_2016": [total_tiv_2016]})