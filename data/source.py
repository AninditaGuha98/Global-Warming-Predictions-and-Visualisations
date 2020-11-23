from pathlib import Path
import pandas as pd


def read_dataset(path: Path) -> pd.DataFrame:
    if path.exists():
        df = pd.read_csv(path)
        return df


def get_electricity_and_population_info():
    df = read_dataset(Path('..', 'data', 'csv_files', 'electricity_and_population_info.csv'))
    return df


def get_drought():
    df = read_dataset(Path('..', 'data', 'csv_files', 'final_drought_data(1970 -2008).csv'))
    return df


def get_flood():
    df = read_dataset(Path('..', 'data', 'csv_files', 'final_flood_data(1970 -2008).csv'))
    return df


def get_storm():
    df = read_dataset(Path('..', 'data', 'csv_files', 'final_storm_data(1970 -2008).csv'))
    return df


def get_deforestation():
    df = read_dataset(Path('..', 'data', 'csv_files', 'Clean_Forest_Area.csv'))
    return df


def get_green_house():
    df = read_dataset(Path('..', 'data', 'csv_files', 'Clean_Greenhouse_Emissions.csv'))
    return df


if __name__ == '__main__':
    print(get_electricity_and_population_info())
