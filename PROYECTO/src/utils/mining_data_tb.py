import pandas as pd

def counlist():
    
    suicide = pd.read_csv("C:\\DATA_SCIENCE\\PROYECTO\\documentation\\who_suicide_statistics.csv")
    suicountrylist = set(suicide.country.unique())
    
    unemployment = pd.read_csv("C:\\DATA_SCIENCE\\PROYECTO\\documentation\\unemployment_all_ratio.csv")
    unempcountrylist = set(unemployment.Country.unique())                                       
    
    countrylist = list(set(suicountrylist).intersection(unempcountrylist))
    
    return countrylist

countrylist = counlist()


def grouper (df, column, condition):

    """ Selects only a slice of rows based on a condition, on a dataframe"""

    df = df[column].loc[df[column] == condition]
    return df

def column_lower(df):

    """ Lowers all strings in columns of a dataframe """

    df.columns = [x.lower() for x in df.columns]
    return df