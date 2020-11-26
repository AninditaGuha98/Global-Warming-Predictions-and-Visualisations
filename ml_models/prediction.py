from ml_models.glacier_model import Glacier_Models
from ml_models.sea_level_model import Sea_Level_Models
from ml_models.temperature_model import Temperature_Models


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


def temperature_prediction(data):
   linear_regressor = Temperature_Models.get_temperature_model()
   temperature = linear_regressor.predict(data)
   return temperature

if __name__ == '__main__':
    print(sea_level_prediction([[19.7]]))
    print(glacier_prediction([[20.3]]))
    print(temperature_prediction([[200000, 125000,205000]]))
    print(temperature_prediction([[205000, 120500, 200500]]))
    print(sea_level_prediction(temperature_prediction([[200000, 125000,205000]])))
    print(glacier_prediction(temperature_prediction([[205000, 120500, 200500]])))
