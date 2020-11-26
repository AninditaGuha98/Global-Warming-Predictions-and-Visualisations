from pathlib import Path
import pandas as pd


def read_dataset(path: Path) -> pd.DataFrame:
    if path.exists():
        df = pd.read_csv(path)
        return df


def get_electricity_and_population_info():
    df = read_dataset(Path('.', 'data', 'csv_files', 'electricity_and_population_info.csv'))
    return df


def get_drought():
    df = read_dataset(Path('.', 'data', 'csv_files', 'final_drought_data(1970 -2008).csv'))
    return df


def get_flood():
    df = read_dataset(Path('.', 'data', 'csv_files', 'final_flood_data(1970 -2008).csv'))
    return df


def get_storm():
    df = read_dataset(Path('.', 'data', 'csv_files', 'final_storm_data(1970 -2008).csv'))
    return df


def get_deforestation():
    df = read_dataset(Path('.', 'data', 'csv_files', 'Clean_Forest_Area.csv'))
    return df

def get_all_emissions_info():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Combine_All.csv'))
    return df

def get_iso_countries():
    df = read_dataset(Path('.','data', 'csv_files', 'countries_iso.csv'))
    return df

def get_green_house():
    df = read_dataset(Path('.', 'data', 'csv_files', 'Clean_Greenhouse_Emissions.csv'))
    return df

def get_sea_level():
    df = read_dataset(Path('.', 'data', 'csv_files', 'final_sea_level_data(1993-2015).csv'))
    return df


def get_glaciers():
    df = read_dataset(Path('.', 'data', 'csv_files', 'Clean_Glaciers.csv'))
    return df


def get_temperature():
    df = read_dataset(Path('.', 'data', 'csv_files', 'temperature_new.csv'))
    return df
    

def clean_glaciers():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Glaciers.csv'))
    return df


def clean_surface_area():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Surface_Area.csv'))
    return df
    
    
def clean_forest_area():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Forest_Area.csv'))
    return df
    
    
def clean_agriculture_area():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Agriculture_Area.csv'))
    return df
    
    
def clean_oil_production():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Oil_Production.csv'))
    return df
    
    
def clean_greenhouse():
    df = read_dataset(Path('.','data', 'csv_files', 'Clean_Greenhouse_Emissions.csv'))
    return df
    
    
def temperature_glaciers():
    df = read_dataset(Path('.','data', 'csv_files', 'temperature_new.csv'))
    return df

def glaciers_vs_temperature():
    df = read_dataset(Path('.','data', 'csv_files', 'glaciers_temperature_df.csv'))
    return df

def sea_level_vs_temperature():
    df = read_dataset(Path('.','data', 'csv_files', 'sea_level_temperature_df.csv'))
    return df

def get_temp_greenhouse_carbon_forest():
    df = read_dataset(Path('.','data', 'csv_files', 'temp_greenhouse_carbon_forest.csv'))
    return df

if __name__ == '__main__':
    print(get_electricity_and_population_info())


