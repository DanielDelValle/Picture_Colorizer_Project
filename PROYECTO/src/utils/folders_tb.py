import pandas as pd

def csv_reader(name_df, csv_df):

    """Creates a dataframe named "name_df".
       Csv_df must be the relative path."""

    name_df = pd.read_csv(csv_df)
    
    return name_df


def infotizer(df):
    return print(df.dtypes, "\n\n", "Rows, Columns: ", df.shape,"\n\n", df.columns, "\n\n", df.head())