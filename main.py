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
from dashboard_components.emissions import emission_section
from dashboard_components.catastrophe_section import catastrophe_section
from dashboard_components.machine_learning_section import machine_learning_results


def dashboard():

    # app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
    app.layout = dbc.Container([

        html.H1(children='Global Climate Change Analysis'),
        html.H5(children='- by Data Vault Team'),
        html.Div(children='Anindita Guha | Devam Shah | Sriram Ponangi | Vigneshwari Ravichandran'),

        html.Hr(),
        html.H2(children="Electricity Generation Information:"),
        population_vs_electricity_section(app),

        html.Hr(),

        html.H2(children="Glaciers and Oil"),
        glacier_and_oil_impacts(app),

        html.Hr(),

        html.H2(children="Emissions:"),
        emission_section(app),

        html.Hr(),

        html.H2(children="Catastrophe Information:"),
        catastrophe_section(app),

        html.Hr(),

        html.H2(children="Machine Learning Results:"),
        machine_learning_results(app),
    ])

    return app


if __name__ == "__main__":
    app = dashboard()
    app.run_server(debug=True)
