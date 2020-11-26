from dash.dependencies import Output, Input, State
from matplotlib.widgets import Button, Slider
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import numpy as np
from data.source import get_temperature, get_glaciers, get_drought, get_deforestation, get_flood, get_storm, \
    get_green_house
from graphs.flood_drought_storm_vs_temp_deforest_greenhouse import plot_map_for_drought_storm_flood, \
    plot_combined_bar_vs_options
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
                                         value='Temperature'), style={'backgroundColor':'white','color':'black'})
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select Start Year:"),
                    dbc.Col(dcc.Dropdown(id='sea_level_start_year_dropdown', value=2000), style={'backgroundColor':'white','color':'black'})
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select End Year:"),
                    dbc.Col(dcc.Dropdown(id='sea_level_end_year_dropdown', value=2010), style={'backgroundColor':'white','color':'black'})
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


def catastrophe_vs_options_tab_2(app):
    catastrophe_types = {
        'Drought': 'drought',
        'Flood': 'flood',
        'Storm': 'storm'
    }

    tab2 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select catastrophe type :"),
                    dbc.Col(dcc.Dropdown(id='catastrophe_type_dropdown',
                                         options=[{'label': k, 'value': k} for k in catastrophe_types.keys()],
                                         value='Drought', style={'backgroundColor':'white','color':'black'}))
                ]),
                    md=4),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select a country to view:"),
                    dbc.Col(dcc.Dropdown(id='country_view_dropdown', value='All', style={'backgroundColor':'white','color':'black'}))
                ]),
                    md=4),

                dbc.Col(dbc.FormGroup([
                    dbc.Label(" "),
                    dbc.Button('Display the Graph', id='catastrophe_map_button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=4)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='catastrophe_map_graph'))
            ])
        ]),
        className="mt-3",
    )

    @app.callback(
        Output('country_view_dropdown', 'options'),
        [Input('catastrophe_type_dropdown', 'value')],
    )
    def set_country_names(selected_option):
        if selected_option == 'Drought':
            df_drought = get_drought()
            country_names = df_drought['country'].unique()
            country_names = np.insert(country_names, 0, 'All', axis=0)
            return [{'label': i, 'value': i} for i in country_names]
        elif selected_option == 'Flood':
            df_flood = get_flood()
            country_names = df_flood['country'].unique()
            country_names = np.insert(country_names, 0, 'All', axis=0)
            return [{'label': i, 'value': i} for i in country_names]
        elif selected_option == 'Storm':
            df_storm = get_storm()
            country_names = df_storm['country'].unique()
            country_names = np.insert(country_names, 0, 'All', axis=0)
            return [{'label': i, 'value': i} for i in country_names]
        else:
            print("error")

    @app.callback(
        Output('catastrophe_map_graph', 'figure'),
        [Input('catastrophe_map_button', 'n_clicks')],
        [State('catastrophe_type_dropdown', 'value'),
         State('country_view_dropdown', 'value')]
    )
    def get_the_map(n_clicks, cat_type, country_name):

        fig = plot_map_for_drought_storm_flood(cat_type, country_name)
        return fig

    return tab2


def catastrophe_combined_graph_vs_options_tab_3(app):
    factor_types = ['Temperature', 'Deforestation', 'Green House Gas Emissions']

    tab3 = dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select factor type:"),
                    dbc.Col(dcc.Dropdown(id='factor_type_dropdown',
                                         options=[{'label': k, 'value': k} for k in factor_types],
                                         value='Deforestation', style={'backgroundColor':'white','color':'black'}))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select Start Year:"),
                    dbc.Col(dcc.Dropdown(id='catastrophe_start_year', value=1990))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select End Year:"),
                    dbc.Col(dcc.Dropdown(id='catastrophe_end_year', value=2008))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label("Select a country :"),
                    dbc.Col(dcc.Dropdown(id='catastrophe_country_name', value='Indonesia', style={'backgroundColor':'white','color':'black'}))
                ]),
                    md=6),

                dbc.Col(dbc.FormGroup([
                    dbc.Label(" "),
                    dbc.Button('Display the Graph', id='catastrophe_combined_graph_button',
                               color='info',
                               style={'margin-bottom': '1em'}, block=True)
                ]),
                    md=12)
            ]),
            html.Hr(),
            dbc.Row([
                dbc.Col(dcc.Graph(id='catastrophe_combined_graph'))
            ])
        ]),
        className="mt-3",
    )

    @app.callback(
        Output('catastrophe_start_year', 'options'),
        Output('catastrophe_end_year', 'options'),
        Output('catastrophe_country_name', 'options'),
        [Input('factor_type_dropdown', 'value')],
    )
    def set_start_end_year_and_country(selected_option):
        years = []
        f_year = 1970
        years.append(f_year)
        while f_year != 2008:
            f_year = f_year + 1
            years.append(f_year)

        if selected_option == 'Temperature':
            df_temp = get_temperature()
            df_temp = df_temp[df_temp['dt'].isin(years)]
            years_range = df_temp['dt'].unique()
            countries = df_temp['Country'].unique()
            return [{'label': i, 'value': i} for i in years_range], [{'label': i, 'value': i} for i in years_range], [
                {'label': i, 'value': i} for i in countries]

        elif selected_option == 'Deforestation':
            df_deforest = get_deforestation()
            df_deforest = df_deforest[df_deforest['year'].isin(years)]
            years_range = df_deforest['year'].unique()
            countries = df_deforest['country'].unique()
            return [{'label': i, 'value': i} for i in years_range], [{'label': i, 'value': i} for i in years_range], [
                {'label': i, 'value': i} for i in countries]

        elif selected_option == 'Green House Gas Emissions':
            df_green = get_green_house()
            df_green = df_green[df_green['year'].isin(years)]
            years_range = df_green['year'].unique()
            countries = df_green['country'].unique()
            return [{'label': i, 'value': i} for i in years_range], [{'label': i, 'value': i} for i in years_range], [
                {'label': i, 'value': i} for i in countries]
        else:
            print("error")

    @app.callback(
        Output('catastrophe_combined_graph', 'figure'),
        [Input('catastrophe_combined_graph_button', 'n_clicks')],
        [State('factor_type_dropdown', 'value'),
         State('catastrophe_start_year', 'value'),
         State('catastrophe_end_year', 'value'),
         State('catastrophe_country_name', 'value')]
    )
    def get_combined_graph(n_clicks, factor_type, start_date, end_date, country_name):
        fig = plot_combined_bar_vs_options(factor_type, start_date, end_date, country_name)
        return fig
    return tab3


def catastrophe_section(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(catastrophe_vs_options_tab_2(app), label="Catastrophe Over the Years"),
            dbc.Tab(sea_level_vs_others_tab_1(app), label="Sea Level Rise"),
            dbc.Tab(catastrophe_combined_graph_vs_options_tab_3(app), label="Trends in affects of other factors")
        ]
    )
    return tabs
