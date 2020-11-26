from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from data.source import get_temp_greenhouse_carbon_forest


class Temperature_Models:
    __temperature_model = None

    @staticmethod
    def get_temperature_model():
        if Temperature_Models.__temperature_model == None:

            df = get_temp_greenhouse_carbon_forest()
            df.drop(labels='Unnamed: 0', axis=1, inplace=True)
            X = df.iloc[:, [2, 3, 4]].values
            y = df.iloc[:, [1]].values
            linear_regressor = LinearRegression()
            Temperature_Models.__temperature_model = linear_regressor.fit(X, y)

        return Temperature_Models.__temperature_model



