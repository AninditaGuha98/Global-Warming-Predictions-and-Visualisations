from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from data.source import clean_greenhouse, clean_surface_area, clean_agriculture_area, \
    clean_oil_production, clean_glaciers, clean_forest_area, temperature_glaciers


def glacier_graph(country: str, start_year: int, end_year: int):
    glacier_df = clean_glaciers()
    glacier_df = glacier_df[(glacier_df["Year"] >= start_year) & (glacier_df["Year"] < end_year)]

    temp_df = temperature_glaciers()
    temp_df = temp_df.loc[temp_df["Country"] == country]
    temp_df = temp_df[(temp_df["dt"] > start_year) & (temp_df["dt"] < end_year)]

    fig = make_subplots()
    fig.add_trace(
        go.Scatter(x=glacier_df["Year"], y=-glacier_df["Mean cumulative mass balance"],
                   line=dict(color='firebrick', width=4), name="Glacier Mass Balance Rise")
    )
    fig.add_trace(
        go.Scatter(x=temp_df["dt"], y=temp_df["avg"],
                   line=dict(color='royalblue', width=4), name="Temperature Increase")
    )
    fig.update_layout(title='Glacier vs Temperature Rise',
                      xaxis_title='Years',
                      yaxis_title='Glacier Mass Balance vs Temperature Mean')
    # fig.show()
    return fig


def area_graph(type: str, start_year: int, end_year: int):
    df = clean_forest_area()
    df1 = clean_agriculture_area()
    df2 = clean_surface_area()
    df = pd.merge(df, df1, on=['country', 'year'])
    df = pd.merge(df, df2, on=['country', 'year'])
    df = df[(df["year"] >= start_year) & (df["year"] < end_year)]

    if type == "forest":
        fig = px.choropleth(df, locations="country",
                            color="value_x",
                            locationmode="country names",
                            hover_name="country",
                            animation_frame="year",
                            color_continuous_scale=px.colors.sequential.Plasma)
    elif type == "surface":
        fig = px.choropleth(df, locations="country",
                            color="value_y",
                            locationmode="country names",
                            hover_name="country",
                            animation_frame="year",
                            color_continuous_scale=px.colors.sequential.Plasma)
    else:
        fig = px.choropleth(df, locations="country",
                            color="value",
                            locationmode="country names",
                            hover_name="country",
                            animation_frame="year",
                            color_continuous_scale=px.colors.sequential.Plasma)
    # fig.show()
    return fig

def oil_graph(start_year, end_year):
    df = clean_oil_production()
    df = df[(df["year"] >= start_year) & (df["year"] < end_year)]
    fig = px.scatter(df, x="country", y="value", animation_frame="year", size="value", color="country", hover_name="country")

    fig["layout"].pop("updatemenus")
    fig.update_layout(title='Increase in Oil Production',
                      xaxis_title='Country',
                      yaxis_title='Mean Oil Production')
    # fig.show()
    return fig




if __name__ == "__main__":
    country = "Canada"
    type = "surface"
    glacier_graph(country, 2005, 2020)
    area_graph(type, 2000, 2020)
    oil_graph(2000, 2020)
