
import plotly.graph_objects as go
from data.source import *


# Sea level vs Glacier melt ( 1. Options button, 2. year_range )

def plot_sea_level_vs_glacier_temp(option, start_year, end_year):
    df_sea = get_sea_level()

    years = []
    f_year = start_year
    years.append(f_year)
    while f_year != end_year:
        f_year = f_year + 1
        years.append(f_year)

    if option == 'Glacier Melt':
        df_glacier = get_glaciers()
        df_glacier = df_glacier[df_glacier['Year'].isin(years)]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=df_sea['GMSL_mean'],
                                 mode='lines',
                                 line=dict(color='firebrick', width=4),
                                 name='Sea Level increase'))
        fig.add_trace(go.Scatter(x=years, y=df_glacier['Mean cumulative mass balance'],
                                 mode='lines+markers',
                                 line=dict(color='royalblue', width=4),
                                 name='Glacier level decrease'))
        fig.update_layout(barmode='group', xaxis_tickangle=-45)

        return fig

    elif option == 'Temperature':
        df_temp = get_temperature()
        df_temp = df_temp[df_temp['dt'].isin(years)]

        # df_temp = df_temp.drop(columns=['Country'], axis=1)
        # df_temp['avg'] = df_temp.groupby('dt')['avg'].transform('mean')
        # df_temp = df_temp.drop_duplicates()
        # df_temp.index = range(len(df_temp.index))
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=df_sea['GMSL_mean'],
                                 mode='lines',
                                 line=dict(color='firebrick', width=4),
                                 name='Sea Level increase'))
        fig.add_trace(go.Scatter(x=years, y=df_temp['avg'],
                                 mode='lines+markers',
                                 line=dict(color='royalblue', width=4),
                                 name='Temperature'))
        fig.update_layout(barmode='group', xaxis_tickangle=-45)
        return fig


