import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from data.source import *


# Sea level vs Glacier melt ( 1. Options button, 2. year_range )

def plot_sea_level_vs_glacier_temp(option, year_range):
    df_sea = get_sea_level()

    # Getting the range of years
    years = []
    f_year = year_range[0]
    years.append(f_year)
    while f_year != year_range[1]:
        f_year = f_year + 1
        years.append(f_year)

    if option == 'Glacier':
        df_glacier = get_glaciers()
        df_glacier = df_glacier[df_glacier['Year'].isin(years)]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=df_sea['GMSL_mean'],
                                 mode='lines',
                                 name='Sea Level increase'))
        fig.add_trace(go.Scatter(x=years, y=df_glacier['Mean cumulative mass balance'],
                                 mode='lines+markers',
                                 name='Glacier level decrease'))
        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        fig.show()


    if option == 'Temperature':
        df_temp = get_temperature()
        df_temp = df_temp[df_temp['dt'].isin(years)]
        # df_temp = df_temp.drop(columns=['Country'], axis=1)
        # df_temp['avg'] = df_temp.groupby('dt')['avg'].transform('mean')
        # df_temp = df_temp.drop_duplicates()
        # df_temp.index = range(len(df_temp.index))
        print(df_temp)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=df_sea['GMSL_mean'],
                                 mode='lines',
                                 name='Sea Level increase'))
        fig.add_trace(go.Scatter(x=years, y=df_temp['avg'],
                                 mode='lines+markers',
                                 name='Temperature'))
        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        fig.show()

plot_sea_level_vs_glacier_temp('Temperature', [1950, 2000])
