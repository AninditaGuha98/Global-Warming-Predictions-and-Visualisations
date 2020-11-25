from ml_models.glacier_model import Glacier_Models
from ml_models.sea_level_model import Sea_Level_Models


def sea_level_prediction(temperature):
    # print(temperature, "sea_level_prediction")
    poly_linear_regressor = Sea_Level_Models.get_sea_level_model()
    poly_regressor = Sea_Level_Models.get_sea_level_poly_regressor()
    # print(poly_linear_regressor, poly_regressor)
    sea_level = poly_linear_regressor.predict(poly_regressor.fit_transform(temperature))
    # print(id(poly_linear_regressor), sea_level)
    return sea_level

def glacier_prediction(temperature):
    poly_linear_regressor = Glacier_Models.get_glaciers_model()
    poly_regressor = Glacier_Models.get_glaciers_poly_regressor()

    glacier =  poly_linear_regressor.predict(poly_regressor.fit_transform(temperature))
    return glacier





if __name__ == '__main__':
    print(sea_level_prediction([[20]]))
    print(glacier_prediction([[20]]))