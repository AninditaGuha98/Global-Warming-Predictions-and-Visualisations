import plotly.graph_objects as go

from data.source import sea_level_vs_temperature
from ml_models.prediction import sea_level_prediction


def sea_level_vs_temperature_model_info():
    df = sea_level_vs_temperature()
    temperatures_list = df.iloc[:, :-1].values

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['temperature'], y=df['sea_level'], mode='markers', name='Complete Dataset',
                             line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=df['temperature'], y=sea_level_prediction(temperatures_list), name='Regression Model',
                             line=dict(color='royalblue', width=4)))
    fig.update_layout(title='<b>Sea Level vs Temperature (Polinomial Regression)</b>',
                      xaxis_title='Temperature',
                      yaxis_title='Sea Level')

    fig.show()
    return fig

def sea_level_vs_temperature_model_prediction(temperature: int, sea_level: int):
    df = sea_level_vs_temperature()
    temperatures_list = df.iloc[:, :-1].values

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[temperature], y=[sea_level], mode='markers', name='Complete Dataset',
                             marker=dict(color='firebrick', size=10)))
    fig.add_trace(go.Scatter(x=df['temperature'], y=sea_level_prediction(temperatures_list), name='Regression Model',
                             line=dict(color='royalblue', width=4)))
    fig.update_layout(title='<b>Sea Level vs Temperature (Polinomial Regression)</b>',
                      xaxis_title='Temperature',
                      yaxis_title='Sea Level')

    fig.show()
    return fig


if __name__ == "__main__":
    sea_level_vs_temperature_model_info()
    sea_level_vs_temperature_model_prediction(20, 79)
    print("ok")