from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib.widgets import Button, Slider

from data.source import get_electricity_and_population_info


def renewable_vs_non_renewable_electricity(country_name: str):
    df = get_electricity_and_population_info()
    df = df.loc[df['country']==country_name]
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['year'], y=df['electricity_from_Fossil_fuel'], name='From oil, gas and coal', mode='lines+markers',
                             line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=df['year'], y=df['total_electricity'], name='Total Electricity',
                             line=dict(color='royalblue', width=4)))

    fig.update_layout(title='<b>Electricity Production - Renewable vs Non-Renewable Sources</b> for '+country_name,
                      xaxis_title='Years',
                      yaxis_title='Electricity (kWh)')

    # fig.show()
    return fig

def non_renewable_electricity_vs_poverty(year: int):

    df = get_electricity_and_population_info()
    df = df.loc[df['year']==year]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df['country'], y=df['total_electricity'], name='Total Electricity', mode='lines+markers',
                   line=dict(color='darkgreen', width=4)), secondary_y=False, )
    fig.add_trace(go.Scatter(x=df['country'], y=df['electricity_from_Fossil_fuel'], name='Electricity From oil, gas and coal', mode='lines+markers',
                             line=dict(color='firebrick', width=4)), secondary_y=False,)
    fig.add_trace(go.Scatter(x=df['country'], y=df['AdjustedIncomePerPerson'], name='Adjusted Income Per Person', mode='lines+markers',
                   line=dict(color='royalblue', width=4)), secondary_y=True)

    fig.update_yaxes(title_text="<b>Electricity (kWh)</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Adjusted Income Per Person</b>", secondary_y=True)
    fig.update_layout(title='<b>Electricity From Non-Renewable Sources vs Poverty Rate</b> for the year ' + str(year),
                      xaxis_title='Countries')

    # fig.show()
    return fig

def non_renewable_electricity_vs_population(year: int):

    df = get_electricity_and_population_info()
    df = df.loc[df['year']==year]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df['country'], y=df['total_electricity'], name='Total Electricity', mode='lines+markers',
                   line=dict(color='darkgreen', width=4)), secondary_y=False)
    fig.add_trace(go.Scatter(x=df['country'], y=df['electricity_from_Fossil_fuel'], name='Electricity From oil, gas and coal', mode='lines+markers',
                             line=dict(color='firebrick', width=4)), secondary_y=False,)
    fig.add_trace(go.Scatter(x=df['country'], y=df['total_population'], name='Total Population', mode='lines+markers',
                   line=dict(color='royalblue', width=4)), secondary_y=True)
    fig.update_yaxes(title_text="<b>Electricity (kWh)</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>Total Population</b>", secondary_y=True)
    fig.update_layout(title='<b>Electricity From Non-Renewable Sources vs Total Population </b>for the year ' + str(year),
                      xaxis_title='Countries')

    # fig.show()
    return fig

if __name__ == "__main__":
    country_name = 'India'
    year = 1990
    renewable_vs_non_renewable_electricity(country_name)
    non_renewable_electricity_vs_poverty(year)
    non_renewable_electricity_vs_population(year)
    print("ok")