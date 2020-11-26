from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from data.source import sea_level_vs_temperature


class Sea_Level_Models:
    __sea_level_model = None
    __sea_level_poly_regressor = None

    @staticmethod
    def get_sea_level_model():
        if Sea_Level_Models.__sea_level_model == None:
            # print('Creating new sea level model...')
            dataset = sea_level_vs_temperature()
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, -1].values

            poly_regressor = PolynomialFeatures(degree=2)
            X_poly = poly_regressor.fit_transform(X)

            poly_linear_regressor = LinearRegression()
            poly_linear_regressor.fit(X_poly, y)

            Sea_Level_Models.__sea_level_model = poly_linear_regressor
            Sea_Level_Models.__sea_level_poly_regressor = poly_regressor
            # print(ML_Models.__sea_level_model, ML_Models.__sea_level_poly_regressor)
        return Sea_Level_Models.__sea_level_model

    @staticmethod
    def get_sea_level_poly_regressor():
        if Sea_Level_Models.__sea_level_poly_regressor == None:
            Sea_Level_Models.get_sea_level_model()
        return Sea_Level_Models.__sea_level_poly_regressor

