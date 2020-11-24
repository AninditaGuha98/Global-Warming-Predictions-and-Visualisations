from plotly.subplots import make_subplots

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from data.source import clean_greenhouse, clean_surface_area, clean_agriculture_area, \
    clean_oil_production, clean_glaciers, clean_forest_area


def glacier_graph(country: str, start_year: int, end_year: int):
    glacier_df = clean_glaciers()

    glacier_df = glacier_df[(glacier_df["Year"] >= start_year) & (glacier_df["Year"] < end_year)]
    # print(glacier_df)
    greenhouse_df = clean_greenhouse()
    greenhouse_df = greenhouse_df.loc[greenhouse_df["country"] == country]

    greenhouse_df = greenhouse_df[(greenhouse_df["year"] > start_year) & (greenhouse_df["year"] < end_year)]
    # print(greenhouse_df)
    fig = make_subplots()

    fig.add_trace(
        go.Scatter(x=glacier_df["Year"], y=-glacier_df["Mean cumulative mass balance"])
    )

    fig.add_trace(
        go.Scatter(x=greenhouse_df["year"], y=greenhouse_df["value"])
    )

    fig.update_layout()
    # fig.show()
    return fig


def area_graph(type: str, start_year: int, end_year: int):
    df = clean_forest_area()
    df1 = clean_agriculture_area()
    df2 = clean_surface_area()
    df = pd.merge(df, df1, on=['country', 'year'])
    df = pd.merge(df, df2, on=['country', 'year'])
    # print(df)
    df = df[(df["year"] >= start_year) & (df["year"] < end_year)]

    if type == "forest":
        print("forest")
        fig = px.choropleth(df, locations="country",
                            color="value_x",
                            locationmode="country names",
                            hover_name="country",
                            animation_frame="year",
                            color_continuous_scale=px.colors.sequential.Plasma)
    elif type == "surface":
        print("surface")
        fig = px.choropleth(df, locations="country",
                            color="value_y",
                            locationmode="country names",
                            hover_name="country",
                            animation_frame="year",
                            color_continuous_scale=px.colors.sequential.Plasma)
    else:
        print("agriculture")
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
    # print(df)

    fig = px.scatter(df, x="country", y="value", animation_frame="year", size="value", color="country", hover_name="country")

    fig["layout"].pop("updatemenus")  # optional, drop animation buttons
    # fig.show()
    return fig


if __name__ == "__main__":
    country = "Canada"
    type = "surface"
    glacier_graph(country, 2005, 2020)
    area_graph(type, 2000, 2020)
    oil_graph(2000, 2020)
