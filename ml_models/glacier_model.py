from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from data.source import glaciers_vs_temperature


class Glacier_Models:
    __glaciers_model = None
    __glaciers_poly_regressor = None

    @staticmethod
    def get_glaciers_model():
        if Glacier_Models.__glaciers_model == None:
            print('Creating new glaciers model...')
            dataset = glaciers_vs_temperature()
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, -1].values

            poly_regressor = PolynomialFeatures(degree=2)
            X_poly = poly_regressor.fit_transform(X)

            poly_linear_regressor = LinearRegression()
            poly_linear_regressor.fit(X_poly, y)

            Glacier_Models.__glaciers_model = poly_linear_regressor
            Glacier_Models.__glaciers_poly_regressor = poly_regressor
            print(Glacier_Models.__glaciers_model, Glacier_Models.__glaciers_poly_regressor)

        return Glacier_Models.__glaciers_model

    @staticmethod
    def get_glaciers_poly_regressor():
        if Glacier_Models.__glaciers_poly_regressor == None:
            Glacier_Models.get_glaciers_model()
        return Glacier_Models.__glaciers_poly_regressor