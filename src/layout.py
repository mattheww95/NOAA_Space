#!/usr/bin/env python3

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import typing

from kyoto_data import KyotoIndex
from plasma import PlasmaData


class DashApp:
    """
    Create an run a dash app
    """

    app = Dash(__name__)

    def __init__(self, kd_index: KyotoIndex, plas_data: PlasmaData):
        self.kyoto_dst = kd_index
        self.plasma_data = plas_data

        self.kyoto_fig = self.kyoto_idx_fig()
        self.plasma_fig = self.plasma_fig()
        self.initialize_app()
        self.app.run_server(debug=True)

    def kyoto_idx_fig(self):
        kyoto_data = self.kyoto_dst.kyoto_index
        k_cols = kyoto_data.columns
        return px.scatter(kyoto_data, x=k_cols[0], y=k_cols[1])

    def plasma_fig(self):
        """
        Create plasma figure
        """
        plasma_data = self.plasma_data.plas_data[["dens_temp"]]
        return px.scatter(plasma_data)

    def initialize_app(self):
        """
        Initialize the dashboard app
        """
        self.app.layout = html.Div(
            children=[
                html.H1(children="Kyoto dst Index"),
                html.Div(
                    "A more negative the number more earths magnetic field is weakend."
                ),
                dcc.Graph(id="kyoto-index", figure=self.kyoto_fig),
                html.H1(children="Plasma"),
                html.Div("PLASMA!"),
                dcc.Graph(id="plasma", figure=self.plasma_fig),
            ]
        )


if __name__ == "__main__":
    kyoto_data = "../Data_20220722/services.swpc.noaa.gov/products/kyoto-dst.json"
    plasma_data = PlasmaData(
        "/home/mattheww/Projects/NOAA_Space/Data_20220722/services.swpc.noaa.gov/products/solar-wind/plasma-7-day.json"
    )
    DashApp(KyotoIndex(kyoto_data), plasma_data)
