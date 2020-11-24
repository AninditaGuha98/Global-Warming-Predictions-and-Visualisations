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

if __name__ == '__main__':
    print(get_electricity_and_population_info())