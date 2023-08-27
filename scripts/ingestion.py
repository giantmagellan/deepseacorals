import pandas as pd
import datetime
from datetime import datetime as dt
import os
import glob

path = os.path.abspath("./data_raw/")
csv_files = glob.glob(os.path.join(path, "*.csv"))

# TBD: Add errors and logging

def import_coral_csv(csv):
    """
    Import CSVs and transform column names into a standardized format.
    :param csv: path, relative path of CSV
    :return df: reformatted Pandas dataframe
    """
    # Read csv and remove index
    df = pd.read_csv(csv, index_col=False)

    # Convert column names to lower case
    df.columns = df.columns.str.strip().str.lower()

    return df

def transform_imports(df):
    """
    Transform columns into a standardized format.
    :param df: dataframe, import_coral_csv output
    :return df: reformatted Pandas dataframe
    """
    # Convert time column to date format: YYYY-MM-DD
    df['time'] = pd.to_datetime(df['time']).dt.date
    df = df.rename(columns={'time': 'date'}, errors='raise')
    # Change float to int dtype
    df['crw_dhw'] = df['crw_dhw'].astype('int64')

    # For columns w/ missing values, impute values w/ exponential moving avg
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].ewm(span=10).mean())
        else:
            pass
    
    return df