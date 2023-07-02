import pandas as pd
import datetime
from datetime import datetime as dt
import os
import glob

path = os.path.abspath("./data_raw/")
csv_files = glob.glob(os.path.join(path, "*.csv"))

def import_coral_csv(csv_name):
    """
    Import CSVs and transform column names into a standardized format.
    :param csv_name: str, CSV file name
    :return df: reformatted Pandas dataframe
    """
    # Read csv and remove index
    df = pd.read_csv(csv_name, index_col=False)

    # Convert column names to lower case
    df.columns.str.strip().str.lower()

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
    