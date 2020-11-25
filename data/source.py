from pathlib import Path
import pandas as pd

def read_dataset(path: Path) -> pd.DataFrame:
    if path.exists():
        df = pd.read_csv(path)
        return df
    return None


def get_electricity_and_population_info():
    df = read_dataset(Path('.','data', 'csv_files', 'electricity_and_population_info.csv'))
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

if __name__ == '__main__':
    print(get_electricity_and_population_info())