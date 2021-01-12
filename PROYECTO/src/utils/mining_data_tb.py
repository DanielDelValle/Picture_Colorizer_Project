import pandas as pd

def intersector(df1, df2, col1, col2):
    """Returns 2 dataframes reduced to common values according specified columns.
        Col1 & Col2 must be string"""

    df1list = set(df1[col1].unique())
    df2list = set(df2[col2].unique())
    countrylist = list(set(df1list).intersection(df2list))

    df1 = df1.loc[df1[col1].isin(countrylist)]
    df2 = df2.loc[df2[col2].isin(countrylist)]

    return df1, df2

def only_desired(df, col1, desired):
    """Returns dataframe slice with only desired values on column.
    Col1 & desired must be string"""

    df2 = df.loc[df[col1] == desired]
    return df2

def str_discarder(df, col1, unwanted):
    """Returns dataframe slice discarding unwanted values on column
    Col1 & unwanted must be string"""

    df2 = df[~df[col1].str.contains(unwanted, na=False)]
    return df2         

def column_lower(df):
    """Returns lowercase for all column names"""

    df.columns = [x.lower() for x in df.columns]


def column_renamer(df, old, new):
    """Renames columns. old is the column to be changed, new the name to be given. 
    Both must be LISTS"""

    changer = dict(zip(old, new))
    df = df.rename(columns = changer)
    return df

def value_renamer(df, col1, old, new):
    """Renames values on column, given their current name and the new name.
    Both in string"""

    df.loc[df[col1] == old, col1] = new


def value_discarder(df, col1, unwanted):
    """Returns dataframe with unwanted values on col1 discarded. 
    Col1 & unwanted must be string""" 

    df.drop(df[df[col1] == unwanted].index, inplace=True)

def str_replacer(df, col1, old, new):
    """Replaces strings on values, given what to remove and what to replace with.
    Both in string"""

    df[col1] = df[col1].str.replace(old , new)

def str_cleaner(df, col1, unwanted):
    """Removes unwanted strings from values on col1"""

    df[col1] = df[col1].str.rstrip(unwanted)


def add_ratio(df, new_col, num, den, mult, round):

    df[new_col] = ((df[num]/df[den])*mult).round(round)