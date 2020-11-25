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

from graphs.population_vs_electricity_graphs import renewable_vs_non_renewable_electricity, \
    non_renewable_electricity_vs_poverty, non_renewable_electricity_vs_population

def tab_1_content(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Country Name:"),
                    dbc.Input(value="Canada", id="population_vs_electricity-country-input-1", type="text"),
                ]),
                    md=6),
                dbc.Col(dbc.FormGroup([
                    dbc.Label("."),
                    dbc.Button('Display the Graph', id='population_vs_electricity_country-display-graph-button-1',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=6)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='population_vs_electricity_country-graph-1'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('population_vs_electricity_country-graph-1', 'figure'),
        [Input('population_vs_electricity_country-display-graph-button-1', 'n_clicks')],
        [State('population_vs_electricity-country-input-1', 'value')])
    def update_figure(n_clicks, country_name):
        if country_name:
            return renewable_vs_non_renewable_electricity(country_name)

    return tab1

def tab_2_content(app):
    tab2 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Choose The Year:"),
                    dcc.RangeSlider(
                        id='population_vs_electricity-country-input-2',
                        min=1985,
                        max=2015,
                        value=[2000],
                        dots=True,
                        marks={i: str(i) for i in range(1985, 2016)},
                    ),
                ]),
                    md=12)
            ]),
            html.Hr(),
            dbc.Row([
                html.Br(),html.Br(),
                dbc.Col(dcc.Graph(id='population_vs_electricity_country-graph-2'))
            ])
        ]),
        className="mt-3",
    )

    @app.callback(
        Output('population_vs_electricity_country-graph-2', 'figure'),
        [Input('population_vs_electricity-country-input-2', 'value')],
        [State('population_vs_electricity-country-input-2', 'value')])
    def update_figure(n_clicks, year):
        if year:
            return non_renewable_electricity_vs_poverty(year[0])

    return tab2

def tab_3_content(app):
    tab3 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Choose The Year:"),
                    dcc.RangeSlider(
                        id='population_vs_electricity-country-input-3',
                        min=1985,
                        max=2015,
                        value=[2000],
                        dots=True,
                        marks={i: str(i) for i in range(1985, 2016)},
                    ),
                ]),
                    md=12),
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='population_vs_electricity_country-graph-3'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('population_vs_electricity_country-graph-3', 'figure'),
        [Input('population_vs_electricity-country-input-3', 'value')],
        [State('population_vs_electricity-country-input-3', 'value')])
    def update_figure(n_clicks, year):
        if year:
            return non_renewable_electricity_vs_population(year[0])

    return tab3

def population_vs_electricity_section(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(tab_1_content(app), label="Production Sources"),
            dbc.Tab(tab_2_content(app), label="Impact of Poverty"),
            dbc.Tab(tab_3_content(app), label="Impact of Population"),

        ]
    )
    return tabs





