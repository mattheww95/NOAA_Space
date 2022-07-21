#!/usr/bin/env python3

import pandas as pd
import typing
import json
import datetime


class KyotoIndex:
    """
    Prepare the kyoto index for data for display
    """

    headers = ("time_tag", "dst")

    def __init__(self, kyoto_fp: str):
        """
        :param kyoto_fp: path to the data for kyoto json
        """
        self.kyoto_index = self.clean_json_df(kyoto_fp)

    def clean_json_df(self, fp):
        """
        Clean up the json dataframe
        :param fp: file path to json data
        """
        jdf = pd.read_json(fp, convert_dates=True)
        jdf.rename(columns=jdf.iloc[0], inplace=True)
        jdf.drop([0], axis=0, inplace=True)
        jdf[self.headers[1]] = jdf[self.headers[1]].astype(int)
        return jdf


if __name__ == "__main__":
    KyotoIndex("../kyoto-dst.json")
