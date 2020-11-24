from dash.dependencies import Output, Input, State
from matplotlib.widgets import Button, Slider
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from data.source import get_temperature, get_glaciers
from graphs.population_vs_electricity_graphs import renewable_vs_non_renewable_electricity, \
    non_renewable_electricity_vs_poverty, non_renewable_electricity_vs_population
from graphs.sea_level_vs_glacier_melt import plot_sea_level_vs_glacier_temp


def sea_level_vs_others_tab_1(app):
    all_options = {
        'Temperature': 'Temp',
        'Glacier Melt': 'Glacier'
    }

    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select Options:"),
                    dbc.Col(dcc.Dropdown(id='sea_level_option_dropdown',
                                         options=[{'label': k, 'value': k} for k in all_options.keys()],
                                         value='Temperature'))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select Start Year:"),
                    dbc.Col(dcc.Dropdown(id='sea_level_start_year_dropdown', value= 2000))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select End Year:"),
                    dbc.Col(dcc.Dropdown(id='sea_level_end_year_dropdown',value = 2010))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("."),
                    dbc.Button('Display the Graph', id='sea_level_button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=6)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='sea_level_graph'))
            ])
        ]),
        className="mt-3",
    )

    @app.callback(
        Output('sea_level_start_year_dropdown', 'options'),
        Output('sea_level_end_year_dropdown', 'options'),
        [Input('sea_level_option_dropdown', 'value')],
    )
    def get_start_end_year_range(selected_option):
        df_temp = get_temperature()
        df_glacier = get_glaciers()

        temp_year = df_temp['dt'].unique()
        glacier_year = df_glacier['Year'].unique()

        year_range = {
            'Temperature': temp_year,
            'Glacier Melt': glacier_year
        }

        if selected_option == 'Temperature':
            return [{'label': i, 'value': i} for i in year_range[selected_option]], [{'label': i, 'value': i} for i in
                                                                                     year_range[selected_option]]
        if selected_option == 'Glacier Melt':
            return [{'label': i, 'value': i} for i in year_range[selected_option]], [{'label': i, 'value': i} for i in
                                                                                     year_range[selected_option]]

    @app.callback(
        Output('sea_level_graph', 'figure'),
        [Input('sea_level_button', 'n_clicks')],
        [State('sea_level_option_dropdown', 'value'),
         State('sea_level_start_year_dropdown', 'value'),
         State('sea_level_end_year_dropdown', 'value')]
    )
    def get_figure(n_clicks, options, start_year, end_year):
        if options == 'Temperature':
            fig = plot_sea_level_vs_glacier_temp(options, start_year, end_year)
            return fig
        elif options == 'Glacier Melt':
            fig = plot_sea_level_vs_glacier_temp(options, start_year, end_year)
            return fig
    return tab1





def catastrophe_section(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(sea_level_vs_others_tab_1(app), label="Sea Level Rise")
        ]
    )
    return tabs
