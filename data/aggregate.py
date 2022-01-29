import pandas as pd
from pathlib import path


def fixed_dataset() -> pd.DataFrame:
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        for file in Path("C:\Users\avjin\Documents\Python\Flight_Tracker\data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list