import plotly.graph_objects as go

from data.source import  glaciers_vs_temperature
from ml_models.prediction import glacier_prediction

def glacier_vs_temperature_model_info():
    df = glaciers_vs_temperature()
    temperatures_list = df.iloc[:, :-1].values
    # print(df)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['temperature'], y=df['glacier'], mode='markers', name='Complete Dataset',
                             line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=df['temperature'], y=glacier_prediction(temperatures_list), name='Regression Model',
                             line=dict(color='royalblue', width=4)))
    fig.update_layout(title='<b>Glaciers Mass Balance vs Temperature (Polynomial Regression)</b>',
                      xaxis_title='Temperature',
                      yaxis_title='Glaciers Mass Balance')

    # fig.show()
    return fig


def  glacier_vs_temperature_model_prediction(temperature: int, glacier: int):
    df = glaciers_vs_temperature()
    temperatures_list = df.iloc[:, :-1].values

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[temperature], y=[glacier], mode='markers', name='Predicted Value',
                             marker=dict(color='firebrick', size=10)))
    fig.add_trace(go.Scatter(x=df['temperature'], y=glacier_prediction(temperatures_list), name='Regression Model',
                             line=dict(color='royalblue', width=4)))
    fig.update_layout(title='<b>Glacier Mass Balance vs Temperature (Polynomial Regression)</b>',
                      xaxis_title='Temperature',
                      yaxis_title='Glacier Level')

    # fig.show()
    return fig

if __name__ == "__main__":
    glacier_vs_temperature_model_info()
    glacier_vs_temperature_model_prediction(20,  -34.04636935)
    print("ok")
