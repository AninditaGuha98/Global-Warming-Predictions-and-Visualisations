from plotly.subplots import make_subplots
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from data.glaciers_source import read_dataset, clean_greenhouse, clean_surface_area,clean_agriculture_area,clean_oil_production,clean_glaciers,clean_forest_area

def glacier_graph(start_year, end_year, country):
    glacier_df = clean_glaciers()
    print(glacier_df)
    glacier_df = glacier_df[(glacier_df["Year"] >= start_year) & (glacier_df["Year"] < end_year)]
    print(glacier_df)
    greenhouse_df = clean_greenhouse()
    greenhouse_df = greenhouse_df.loc[greenhouse_df["country"] == country]

    greenhouse_df = greenhouse_df[(greenhouse_df["year"] >= start_year) & (greenhouse_df["year"] < end_year)]
    print(greenhouse_df)
    fig = make_subplots()

    fig.add_trace(
        go.Scatter(x=glacier_df["Year"], y=-glacier_df["Mean cumulative mass balance"])
    )

    fig.add_trace(
        go.Scatter(x=greenhouse_df["year"], y=greenhouse_df["value"])
    )

    fig.update_layout()
    fig.show()

def area_graph(start_year, end_year, type):
    df = clean_forest_area()
    df1 = clean_agriculture_area()
    df2 = clean_surface_area()
    df =pd.merge(df,df1, on=['country','year'])
    df =pd.merge(df,df2, on=['country','year'])
    print(df)
    df = df[(df["year"] >= start_year) & (df["year"] < end_year)]

    # fig = make_subplots(rows=2, cols=2)
    #
    # fig.add_trace(
    #     go.Bar(x=df["year"], y=df["value_y"],name="forest"),
    #     row=1, col=1
    # )
    #
    # fig.add_trace(
    #     go.Bar(x=df["year"], y=df["value_x"],name="agriculture"),
    #     row=1, col=2
    # )
    #
    # fig.add_trace(
    #     go.Bar(x=df["year"], y=df["value_y"], name="surface"),
    #     row=2, col=1
    # )
    #
    # fig.update_layout()
    # fig.show()

    if type == "forest":
        fig = px.choropleth(df, locations="country",
                            color="value_x",
                            locationmode="country names",
                            hover_name="country",
                            color_continuous_scale=px.colors.sequential.Plasma)
    elif type == "surface":
        fig = px.choropleth(df, locations="country",
                            color="value_y",
                            locationmode="country names",
                            hover_name="country",
                            color_continuous_scale=px.colors.sequential.Plasma)
    else:
        fig = px.choropleth(df, locations="country",
                                color="value",
                                locationmode="country names",
                                hover_name="country",
                                color_continuous_scale=px.colors.sequential.Plasma)
    fig.show()


def oil_graph(start_year,end_year):
    df = clean_oil_production()
    df = df[(df["year"] >= start_year) & (df["year"] < end_year)]
    print(df)


    fig = px.bar(df, x="country", y="value", animation_frame="year", hover_name="country")

    fig["layout"].pop("updatemenus")  # optional, drop animation buttons
    fig.show()


if __name__ == "__main__":
    country = "Canada"
    type ="agri"
    glacier_graph(2005,2020, country)
    area_graph(2000,2020,type)
    oil_graph(2000,2020)
