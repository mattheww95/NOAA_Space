#!/usr/bin/env python3

"""
Process the plasma wind speed data into a dataframe

2022-07-22: Matthew Wells
"""
import pandas as pd
from math import log10


class PlasmaData:
    """
    Process the solar wind speed into a dataframe for dash

    """

    def __init__(self, data_json: str):
        self.data_fp = data_json
        self.plas_data = self.read_plasma_data()

    def read_plasma_data(self):
        """
        Prepare plasma data into a dataframe
        """
        df = pd.read_json(self.data_fp)
        df.rename(columns=df.iloc[0], inplace=True)
        df.drop([0], axis=0, inplace=True)
        df.set_index("time_tag", inplace=True)
        df["density"] = df["density"].astype(float)
        df["speed"] = df["speed"].astype(float)
        df["temperature"] = df["temperature"].astype(int)
        df["dens_temp"] = df["temperature"] / df["density"]
        return df


if __name__ == "__main__":
    plas_data = "/home/mattheww/Projects/NOAA_Space/Data_20220722/services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"
    PlasmaData(plas_data)
