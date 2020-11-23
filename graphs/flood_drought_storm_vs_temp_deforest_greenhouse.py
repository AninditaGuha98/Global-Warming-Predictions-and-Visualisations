import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from data.source import *


# Option:1 Map Structure

def plot_map_for_drought_storm_flood(type_of_catastrophe, country):
    if type_of_catastrophe == 'drought':
        df_drought = get_drought()
        country_name = list(country.split(" "))
        df_drought = df_drought[df_drought['country'].isin(country_name)]

        fig = px.choropleth(df_drought,
                            locations='country',
                            color="value",
                            animation_frame="years",
                            color_continuous_scale="Plasma",
                            locationmode='country names',
                            range_color=(0, 20),
                            title='Drought per year',
                            height=600
                            )
        fig.show()

    elif type_of_catastrophe == 'storm':
        df_storm = get_storm()
        country_name = list(country.split(" "))
        df_storm = df_storm[df_storm['country'].isin(country_name)]

        fig = px.choropleth(df_storm,
                            locations='country',
                            color="value",
                            animation_frame="years",
                            color_continuous_scale="Plasma",
                            locationmode='country names',
                            range_color=(0, 20),
                            title='Storm per year',
                            height=600
                            )
        fig.show()

    elif type_of_catastrophe == 'flood':
        df_flood = get_flood()
        country_name = list(country.split(" "))
        df_flood = df_flood[df_flood['country'].isin(country_name)]

        fig = px.choropleth(df_flood,
                            locations='country',
                            color="value",
                            animation_frame="years",
                            color_continuous_scale="Plasma",
                            locationmode='country names',
                            range_color=(0, 20),
                            title='Flood per year',
                            height=600
                            )
        fig.show()
    else:
        print("Issues loading graph")


# plot_map_for_drought_storm_flood('storm', 'Japan')

# Option 2: Bar Structure

def plot_combined_bar_vs_options(type_of_factor, year_range, country):
    df_drought = get_drought()
    df_flood = get_flood()
    df_storm = get_storm()

    # Getting the range of years
    years = []
    f_year = year_range[0]
    years.append(f_year)
    while f_year != year_range[1]:
        f_year = f_year + 1
        years.append(f_year)

    # Keeping only the country's data in the dataframes
    country_name = list(country.split(" "))

    df_drought = df_drought[df_drought['country'].isin(country_name)]
    df_drought = df_drought[df_drought['years'].isin(years)]
    df_flood = df_flood[df_flood['country'].isin(country_name)]
    df_flood = df_flood[df_flood['years'].isin(years)]
    df_storm = df_storm[df_storm['country'].isin(country_name)]
    df_storm = df_storm[df_storm['years'].isin(years)]

    if type_of_factor == 'Deforestation':
        df_deforest = get_deforestation()
        df_deforest = df_deforest[df_deforest['country'].isin(country_name)]
        df_deforest = df_deforest[df_deforest['year'].isin(years)]

        print(df_deforest)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=years,
            y=df_drought['value'],
            name='drought',
            marker_color='indianred'
        ))
        fig.add_trace(go.Bar(
            x=years,
            y=df_flood['value'],
            name='flood',
            marker_color='lightsalmon'
        ))
        fig.add_trace(go.Bar(
            x=years,
            y=df_storm['value'],
            name='storm',
            marker_color='pink'
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=df_deforest['value'],
            mode='lines+markers',
            name='Reduction in Forest Area')
        )

        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        fig.show()
        return fig

    if type_of_factor == 'Green House Gas Emissions':
        df_green = get_green_house()
        df_green = df_green[df_green['country'].isin(country_name)]
        df_green = df_green[df_green['year'].isin(years)]

        print(df_green)
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=years,
            y=df_drought['value'],
            name='drought',
            marker_color='indianred'
        ))
        fig.add_trace(go.Bar(
            x=years,
            y=df_flood['value'],
            name='flood',
            marker_color='lightsalmon'
        ))
        fig.add_trace(go.Bar(
            x=years,
            y=df_storm['value'],
            name='storm',
            marker_color='pink'
        ))
        fig.add_trace(go.Scatter(
            x=years,
            y=df_green['value'],
            mode='lines+markers',
            name='Green House Gas Emissions')
        )

        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        fig.show()
        return fig


plot_combined_bar_vs_options('Green House Gas Emissions', [1990, 2000], 'Indonesia')
