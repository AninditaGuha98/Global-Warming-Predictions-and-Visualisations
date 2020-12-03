from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from matplotlib.widgets import Button, Slider

from data.source import *


def emissions_chart(country_name):
    df = get_all_emissions_info()
    df = df.loc[df['country'] == country_name]
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df['year'], y=df['carbon_total'], name='Carbon Emissions',
                             line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=df['year'], y=df['greenhouse'], name='Other Greenhouse Emissions',
                             line=dict(color='royalblue', width=4)))

    fig.update_layout(title='<b>Emissions for </b> ' + country_name,
                      xaxis_title='Years',
                      yaxis_title='Metric tonnes of fuel')
    return fig


def bar_analysis(column, year):
    df = get_all_emissions_info()
    fig = go.Figure()
    df = df.loc[df['year'] == year]
    fig.add_trace(go.Bar(x=df['country'], y=df[column]))
    return fig


def map_analysis(column, year):
    df = get_iso_countries()
    df = df.loc[df['year'] == year]
    fig = px.choropleth(df, locations=df['geo'],
                        color=df[column],
                        hover_name="geo",
                        color_continuous_scale=px.colors.sequential.Plasma)
    return fig

def pie_analysis2(column):
    df = get_all_emissions_info()
    selected_countries = ['USA', 'Canada', 'India', 'China', 'Brazil']
    df = df.loc[df['country'].isin(selected_countries)]
    fig = px.bar(df,x='year',y=column,color='country')

    return fig



if __name__ == "__main__":
    country_name = 'Canada'
    year = 1990
    emissions_chart(country_name)
    bar_analysis('coal', 1981)
    map_analysis('greenhouse', 2000)
    pie_analysis('coal', 1990)
    print("ok")