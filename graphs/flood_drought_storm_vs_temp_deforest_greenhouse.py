import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from data.source import *


# Option:1 Map Structure

def plot_map_for_drought_storm_flood(type_of_catastrophe, country):
    if type_of_catastrophe == 'Drought':
        df_drought = get_drought()
        country_name = list(country.split(" "))
        if country != 'All':
            df_drought = df_drought[df_drought['country'].isin(country_name)]

        fig = px.choropleth(df_drought,
                            locations='country',
                            color="value",
                            animation_frame="years",
                            color_continuous_scale="Plasma",
                            locationmode='country names',
                            range_color=(0, 20),
                            title='Drought over the years for ' + country_name[0],
                            height=600
                            )
        return fig

    elif type_of_catastrophe == 'Storm':
        df_storm = get_storm()
        country_name = list(country.split(" "))
        if country != 'All':
            df_storm = df_storm[df_storm['country'].isin(country_name)]

        fig = px.choropleth(df_storm,
                            locations='country',
                            color="value",
                            animation_frame="years",
                            color_continuous_scale="Plasma",
                            locationmode='country names',
                            range_color=(0, 20),
                            title='Storm over the years for ' + country_name[0],
                            height=600
                            )
        return fig
    elif type_of_catastrophe == 'Flood':
        df_flood = get_flood()
        country_name = list(country.split(" "))
        if country != 'All':
            df_flood = df_flood[df_flood['country'].isin(country_name)]

        fig = px.choropleth(df_flood,
                            locations='country',
                            color="value",
                            animation_frame="years",
                            color_continuous_scale="Plasma",
                            locationmode='country names',
                            range_color=(0, 20),
                            title='Flood over the years for ' + country_name[0],
                            height=600
                            )
        return fig
    else:
        print("Issues loading graph")


# Option 2: Bar Structure

def plot_combined_bar_vs_options(type_of_factor, start_date, end_date, country):
    df_drought = get_drought()
    df_flood = get_flood()
    df_storm = get_storm()

    # Getting the range of years
    years = []
    f_year = start_date
    years.append(f_year)
    while f_year != end_date:
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
        return fig

    if type_of_factor == 'Green House Gas Emissions':
        df_green = get_green_house()
        df_green = df_green[df_green['country'].isin(country_name)]
        df_green = df_green[df_green['year'].isin(years)]

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
        return fig

    if type_of_factor == 'Temperature':
        df_temp = get_temperature()
        df_temp = df_temp[df_temp['Country'].isin(country_name)]
        df_temp = df_temp[df_temp['dt'].isin(years)]

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
            y=df_temp['avg'],
            mode='lines+markers',
            name='Temperature')
        )

        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        return fig

# plot_combined_bar_vs_options('Temperature', [1990, 2010], 'Ireland')
