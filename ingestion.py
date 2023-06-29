import pandas as pd
import os
import glob

path = os.path.abspath("./data_raw/")
csv_files = glob.glob(os.path.join(path, "*.csv"))

def import_coral_csv(csv_name):
    """
    Import CSVs and transform them into a standardized format.
    :param csv_name: str, CSV file name
    :return df: reformatted Pandas dataframe
    """

    df = pd.read_csv(csv_name, index_col=False)

    df.columns.str.strip().str.lower()

    return df
