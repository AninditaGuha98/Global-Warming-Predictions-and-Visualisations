from pathlib import Path
from typing import Tuple

import dash
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Output, Input, State
from matplotlib.widgets import Button, Slider
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from dashboard_components.population_vs_electricity_section import population_vs_electricity_section
from dashboard_components.glaciers_oil_areas_dash import glacier_and_oil_impacts

def dashboard():

    # app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO])
    app.layout = dbc.Container([
        html.H1(children='Global Climate Change Analysis'),
        html.Div(children='- Project by Data Vault Team'),

        html.Hr(),
        html.H2(children="Electricity Generation Information:"),
        population_vs_electricity_section(app),

        html.Hr(),
        html.H2(children="Glaciers and Oil"),
        glacier_and_oil_impacts(app),


    ])

    return app


if __name__ == "__main__":
    app = dashboard()
    app.run_server(debug=True)