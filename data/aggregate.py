import pandas as pd
from pathlib import Path
from api import fetcher
from data import utils


def forming_dataset(*, start_time: str, end_time: str) -> pd.DataFrame:
    # converter to UNIX TIME
    start_dt_dt, start_dt_unix = utils.converter(sample_dt=start_time)
    end_dt_dt, end_dt_unix = utils.converter(sample_dt=start_time)
    fetcher.flights_accessor(start_time=start_dt_unix, end_time=end_dt_unix)

    df = pd.DataFrame(data=flighs_json)
    df.drop(labels="",
            axis=1, inplace=True)
    return df


def fixed_dataset() -> pd.DataFrame:
    # https://zenodo.org/record/4601480
    flight_list = pd.concat(
        pd.read_csv(file, parse_dates=["firstseen", "lastseen", "day"])
        # for file in Path("path/to/folder").glob("flightlist_*.csv.gz")
        for file in
        Path("C:\Users\avjin\Documents\Python\Flight_Tracker\data_set").glob("flightlist_*.csv.gz")
    )
    return flight_list
