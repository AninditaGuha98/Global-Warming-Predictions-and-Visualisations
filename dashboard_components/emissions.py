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

from graphs.emissions import *

def tab_1_content(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Country Name:"),
                    dbc.Input(value="Canada", id="emissions-country-input-1", type="text"),
                ]),
                    md=6),
                dbc.Col(dbc.FormGroup([
                    dbc.Label("."),
                    dbc.Button('Display the Graph', id='emissions-display-graph-button-1',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=6)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='emissions-graph-1'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('emissions-graph-1', 'figure'),
        [Input('emissions-display-graph-button-1', 'n_clicks')],
        [State('emissions-country-input-1', 'value')])
    def update_figure(n_clicks, country_name):
        if country_name:
            return emissions_chart(country_name)

    return tab1

def tab_2_content(app):
    tab2 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Enter Year: "),
                    dbc.Input(value=1990, id="emissions-year-input-2", type="number"),
                ]),
                    md=6),
                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label("Choose Type"),
                        dcc.Dropdown(id="emissions-column-input-2", value='carbon', style={'backgroundColor':'white','color':'black'},
                                     options=[{"label": "Carbon", "value": "carbon"},
                                              {"label": "Carbon Per Person", "value": "carbon_person"},
                                              {"label": "Coal", "value": "coal"},
                                              {"label": "Sulfur", "value": "sulfur"},
                                              {"label": "Greenhouse", "value": "greenhouse"}]),
                    ]),
                    md=6)
            ]),
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Button('Display the Graph', id='emissions-display-graph-button-2',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=12)
            ]),
            html.Hr(),
            dbc.Row([
                html.Br(),html.Br(),
                dbc.Col(dcc.Graph(id='emissions-graph-2'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('emissions-graph-2', 'figure'),
        [Input('emissions-display-graph-button-2', 'n_clicks')],
        [State('emissions-year-input-2', 'value'),
         State('emissions-column-input-2','value')])
    def update_figure(n_clicks, year, country):
        if year and country:
            return map_analysis(country, year)

    return tab2

def tab_3_content(app):
    tab3 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Enter Year: "),
                    dbc.Input(value=1990, id="emissions-year-input-3", type="number"),
                ]),
                    md=6),
                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label("Choose Type"),
                        dcc.Dropdown(id="emissions-column-input-3", value='coal', style={'backgroundColor':'white','color':'black'},
                                     options=[{"label": "Carbon", "value": 'carbon_total'},
                                              {"label": "Carbon Per Person", "value": 'carbon_per_person'},
                                              {"label": "Coal", "value": 'coal'},
                                              {"label": "Sulfur", "value": 'sulfur'},
                                              {"label": "Greenhouse", "value": 'greenhouse'}]),
                    ]),
                    md=6)
            ]),
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Button('Display the Graph', id='emissions-display-graph-button-3',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=12)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='emissions-graph-3'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('emissions-graph-3', 'figure'),
        [Input('emissions-display-graph-button-3', 'n_clicks')],
        [State('emissions-year-input-3', 'value'),
         State('emissions-column-input-3', 'value')])
    def update_figure(n_clicks, year, column):
        if year and column:
            return bar_analysis(column, year)

    return tab3

def tab_4_content(app):
    tab4 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(
                    dbc.FormGroup([
                        dbc.Label("Choose Type"),
                        dcc.Dropdown(id="emissions-column-input-4", value='coal', style={'backgroundColor':'white','color':'black'},
                                     options=[{"label": "Carbon", "value": 'carbon_total'},
                                              {"label": "Carbon Per Person", "value": 'carbon_per_person'},
                                              {"label": "Coal", "value": 'coal'},
                                              {"label": "Sulfur", "value": 'sulfur'},
                                              {"label": "Greenhouse", "value": 'greenhouse'}]),
                    ]),
                    md=12)
            ]),
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Button('Display the Graph', id='emissions-display-graph-button-4',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=12)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='emissions-graph-4'))
            ])
        ]),
        className="mt-3",
    )
    @app.callback(
        Output('emissions-graph-4', 'figure'),
        [Input('emissions-display-graph-button-4', 'n_clicks')],
        [State('emissions-column-input-4', 'value')])
    def update_figure(n_clicks, column):
        if column:
            return pie_analysis2(column)

    return tab4

def emission_section(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(tab_4_content(app), label="Pie Chart"),
            dbc.Tab(tab_1_content(app), label="Line Chart (Carbon and Greenhouse)"),
            dbc.Tab(tab_2_content(app), label="Map"),
            dbc.Tab(tab_3_content(app), label="Bar Chart"),

        ]
    )
    return tabs





