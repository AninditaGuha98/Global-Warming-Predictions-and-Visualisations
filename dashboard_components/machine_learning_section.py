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

from graphs.glaciers_model import glacier_vs_temperature_model_info, glacier_vs_temperature_model_prediction
from graphs.sea_level_model import sea_level_vs_temperature_model_info, sea_level_vs_temperature_model_prediction
from ml_models.prediction import temperature_prediction,glacier_prediction, sea_level_prediction

def glacier_model_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            html.Hr(),
            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(html.H3(children="Machine Learning Models used for Datasets"))
            ]),
            html.Hr(),
            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(dcc.Graph(id='glacier-model-1-graph', figure=glacier_vs_temperature_model_info()))
            ]),

        ]),
        className="ml-1",
    )

    return tab1
def sea_level_model_tab(app):
    tab2 = dbc.Card(
        dbc.CardBody([
            html.Hr(),
            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(html.H3(children="Machine Learning Models used for Datasets"))
            ]),
            html.Hr(),

            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(dcc.Graph(id='glacier-model-2-graph', figure=sea_level_vs_temperature_model_info()))
            ]),
        ]),
        className="ml-2",
    )

    return tab2


def predictor_tab(app):
    tab2 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Enter a value for Greenhouse Gas Emission (Kilotonne of CO2 equivalent) between 150000 and 350000: "),
                    dbc.Input(value=200000, id="temp-input-1", type="number", min=150000, max=350000),
                    dbc.Label("Enter a value for Forest Area Loss (sq km) between 100000 and 250000: "),
                    dbc.Input(value=125000, id="temp-input-2", type="number", min=100000, max=250000),
                    dbc.Label("Enter a value for Carbon Dioxide Emission (Kilotonne) between 95000 and 250000: "),
                    dbc.Input(value=205000, id="temp-input-3", type="number", min=95000, max=250000),
                    dbc.Label("."),
                    dbc.Button('Predict Temperature', id='temp-button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),

                    md=12)
            ]),
            html.Hr(),
            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(html.H4(id='temp-heading', children="Predicted temperature value: ")),
                dbc.Col(html.Div(id='temp-value'))
            ]),
            html.Hr(),
            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(dcc.Graph(id='model-1-graph'))
            ]),
            dbc.Row([
                html.Br(), html.Br(),
                dbc.Col(dcc.Graph(id='model-2-graph'))
            ]),
        ]),
        className="ml-3",
    )

    @app.callback(
        Output('temp-value', 'children'),
        [Input('temp-button', 'n_clicks')],
        [State('temp-input-1', 'value'),
         State('temp-input-2', 'value'),
         State('temp-input-3', 'value'), ])
    def update_temp(n_clicks,greenhouse_gas,forest,carbon_dioxide):
        temp = temperature_prediction([[greenhouse_gas,forest,carbon_dioxide]])
        return temp[0][0]

    @app.callback(
        Output('model-1-graph', 'figure'),
        [Input('temp-value', 'children')])
    def update_sea_level(temperature):
        sea_level = sea_level_prediction([[temperature]])
        return sea_level_vs_temperature_model_prediction(temperature, sea_level[0])

    @app.callback(
        Output('model-2-graph', 'figure'),
        [Input('temp-value', 'children')])
    def update_glacier(temperature):
        glacier_mass_balance = glacier_prediction([[temperature]])
        return glacier_vs_temperature_model_prediction(temperature, glacier_mass_balance[0])

    return tab2



def machine_learning_results(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(predictor_tab(app), label="Temperature Predictor"),
            dbc.Tab(glacier_model_tab(app), label="Complete Dataset - Glaciers"),
            dbc.Tab(sea_level_model_tab(app), label="Complete Dataset - Sea Level"),

        ]
    )
    return tabs





