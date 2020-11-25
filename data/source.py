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

