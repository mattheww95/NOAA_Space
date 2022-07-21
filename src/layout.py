#!/usr/bin/env python3

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import typing

from kyoto_data import KyotoIndex


class DashApp:
    """
    Create an run a dash app
    """

    app = Dash(__name__)

    def __init__(self, kd_index: KyotoIndex):
        self.kyoto_dst = kd_index
        self.kyoto_fig = self.kyoto_idx_fig()
        self.initialize_app()
        self.app.run_server(debug=True)

    def kyoto_idx_fig(self):
        kyoto_data = self.kyoto_dst.kyoto_index
        k_cols = kyoto_data.columns
        return px.scatter(kyoto_data, x=k_cols[0], y=k_cols[1])

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
            ]
        )


if __name__ == "__main__":
    DashApp(KyotoIndex("../kyoto-dst.json"))
