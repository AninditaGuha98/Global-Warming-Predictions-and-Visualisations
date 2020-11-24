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

from graphs.glaciers_oil_areas import glacier_graph, area_graph, oil_graph

def glaciers_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Country Name:"),
                    dbc.Input(value="Canada", id="glacier-input-1", type="text"),
                    dbc.Input(value=1990, id="glacier-input-2", type="number"),
                    dbc.Input(value=2016, id="glacier-input-3", type="number"),
                ]),
                    md=6),
                dbc.Col(dbc.FormGroup([
                    dbc.Label("."),
                    dbc.Button('Display the Graph', id='glacier-button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=6)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='glacier-graph'))
            ])
        ]),
        className="glacier-1",
    )
    @app.callback(
        Output('glacier-graph', 'figure'),
        [Input('glacier-button', 'n_clicks')],
        [State('glacier-input-1', 'value'),
         State('glacier-input-2', 'value'),
         State('glacier-input-3', 'value')
        ])
    def update_figure(n_clicks,country_name,start_year,end_year):
        return glacier_graph(country_name,start_year,end_year)

    return tab1

def area_tab(app):
    tab2 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(

                    dbc.FormGroup([
                    dbc.Label("Enter Year:"),
                    dbc.Input(value=1990, id="area-input-1", type="number"),
                    dbc.Input(value=2013, id="area-input-2", type="number"),
                    ]),
                    md=6),
                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label("Choose Area Type"),
                        dcc.Dropdown(id="area-dropdown", value="forest",
                                     options=[{"label": "Forest Area", "value": "forest"},
                                              {"label": "Surface Area", "value": "surface"},
                                              {"label": "Agriculture Area", "value": "agriculture"}]),
                    ]),
                    md=6),
                dbc.Col(dbc.FormGroup([
                    dbc.Label("."),
                    dbc.Button('Display the Graph', id='area-button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=6)
            ]),
            html.Hr(),
            dbc.Row([
                html.Br(),html.Br(),
                dbc.Col(dcc.Graph(id='area-graph'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('area-graph', 'figure'),
        [Input('area-button', 'n_clicks')],
        [State('area-dropdown', 'value'),
         State('area-input-1', 'value'),
         State('area-input-2', 'value'),])
    def update_figure(n_clicks, type, start_year,end_year):
        return area_graph(type,start_year,end_year)

    return tab2

def oil_tab(app):
    tab3 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Year:"),
                    dbc.Input(value=2000, id="oil-input-1", type="number"),
                    dbc.Input(value=2020, id="oil-input-2", type="number"),

                ]),
                    md=6),
                dbc.Col(dbc.FormGroup([
                    dbc.Label("."),
                    dbc.Button('Display the Graph', id='oil-button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=6)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='oil-graph'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('oil-graph', 'figure'),
        [Input('oil-button', 'n_clicks')],
        [State('oil-input-1', 'value'),
         State('oil-input-2', 'value')
         ])
    def update_figure(n_clicks, start_year, end_year):
        return oil_graph(start_year,end_year)

    return tab3

def glacier_and_oil_impacts(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(glaciers_tab(app), label="Impact of Glaciers"),
            dbc.Tab(area_tab(app), label="Area Changes"),
            dbc.Tab(oil_tab(app), label="Impact of Oil Production"),

        ]
    )
    return tabs





