import sys
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn import datasets
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
sys.path.append('C:\\DATA_SCIENCE')
from sklearn import linear_model
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import train_test_split, StratifiedKFold, RepeatedKFold, RepeatedStratifiedKFold, KFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, RobustScaler, Normalizer, PolynomialFeatures, MinMaxScaler
from LIBRARY.Libreria_Folders_DVG import *
from LIBRARY.Libreria_ML_DVG import *
from LIBRARY.Libreria_Maths_DVG import *
from LIBRARY.Libreria_Graphs_DVG import *




def date_fixer(x):

    """   fixes the usual error on dates   """
    
    import datetime
    if x.year > 1989:
        year = x.year - 100
    else:
        year = x.year
    return datetime.date(year,x.month,x.day)

def csv_info(df):
    """reads and gives main info about a csv file"""
    import pandas as pd
    import numpy as np
    x = pd.read_csv(df)
    print(x.dtypes, "\n\n", "Rows, Columns: ", x.shape,"\n\n", x.columns, "\n\n", x.head())


def list_difference(a, b):

    """ This function returns the items in a(list) that are not present in b(list)"""
    for x in a:
        if x in a and x in b:
            a.remove(x)
        else: x = x
    for y in b:
        if y in a and y in b:
            a.remove(y)
        else: y = y
    return a

def column_lower(df):

    """ Lowers all strings in columns of a dataframe """

    df.columns = [x.lower() for x in df.columns]
    return df     


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

def col_dropper(df, undesired):
    df.drop(columns=undesired, inplace=True)

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
    """Adds a column featuring the division between 2 columns (num, den) and multiplicating by "mult", rounding decimals by "round"""

    df[new_col] = ((df[num]/df[den])*mult).round(round)


def gr_meaner(df, col, val):
    """ Groups a dataframe by a column and gives the MEAN of the value (val), rounded on 2 decimals"""

    aggregation_functions = {val: 'mean'}
    df2 = df.groupby(col).aggregate(aggregation_functions).sort_values(val, ascending=False).round(2)
    return df2

def gr_sum(df, col, val):
    """ Groups a dataframe by a column and gives the SUM of the value (val), rounded on 2 decimals"""

    aggregation_functions = {val: 'sum'}
    df2 = df.groupby(col).aggregate(aggregation_functions).sort_values(val, ascending=False).round(2)
    return df2

def most_least(df, col, val, quant):
    """Does the same than gr_meaner but returns just the "quant" (amount) of top and bottom values."""

    aggregation_functions = {val: 'mean'}
    df2 = df.groupby(col).aggregate(aggregation_functions).sort_values(val, ascending=False).round(2).head(quant)
    df3 = df.groupby(col).aggregate(aggregation_functions).sort_values(val).round(2).head(quant)
    return df2, df3



def corrFilter(x: pd.DataFrame, bound):
    """Finds most correlated columns in a df, below corr. factr (bound) and discarding duplicates"""
    
    xCorr = x.corr()
    xFiltered = xCorr[((xCorr >= bound) | (xCorr <= -bound)) & (xCorr !=1.000)]
    xFlattened = xFiltered.unstack().sort_values().drop_duplicates()
    return xFlattened


def corr_comparer(df, col):
    """Returns the correlations of a column respect the rest of df columns"""
    return df[df.columns[:]].corr()[col][:].sort_values(ascending=False)



def outliers_df(df, deviation):
    """Removes outlayers"""

    num_cols = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_num = df.select_dtypes(include=num_cols)

    for col in df_num:
        df_mean, df_std = df[col].mean(), df[col].std()
        cut_off = df_std * deviation    
        lower, upper = df_mean - cut_off, df_mean + cut_off
        outliers = [x for x in col if (x < lower) or (x > upper)]
        outliers_removed = [x for x in col if (x > lower) and (x < upper)]
        print('Identified outliers: %d' % len(outliers))
        print('Non-outlier observations: %d' % len(outliers_removed))

    return df

def nan_out_cols(df):
    """Given a df drops all columns with 0.9 nan ratio on them."""
    df.dropna(axis=1,thresh=len(df)*0.9)

def nan_out_rows(df):
    """Given a df drops all columns with all nan on them."""
    df.dropna(axis=0)


def clean_df(path):    
    for x in path:
        path.replace("\\", r"\\") 
        if path[-3:] == 'csv':
            df= pd.read_csv(path)
        elif path[-4:] == 'xlsx':
            df = pd.read_excel(path)
        elif path[-4:] == 'json':            
            with open(path, "r") as json_file_readed:
                df = pd.DataFrame(json.load(json_file_readed))
        else: 
            print('Please use csv / json / xlsx files only')
    outliers_df
    nan_out_cols(df)
    nan_out_rows(df)
    return df   


def type_changer(df, origin, desired):
    lista = df.select_dtypes(origin).columns
    for x in lista:
        if desired == 'numeric':
            df[x] = df[x].apply(pd.to_numeric)
        elif desired == 'object':
            df[x] = df[x].apply(pd.to_str)
        elif desired == 'datetime':
            df[x] = df[x].apply(pd.to_datetime)
    return df.dtypes

def nan_ratio(df):
    na_ratio = ((df.isnull().sum() / len(df))*100).sort_values(ascending = False)
    return na_ratio


def outlier_quant(df, quantile_low, quantile_high):
    num_cols = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_num = df.select_dtypes(include=num_cols)
    for col in df_num:
        q_low = df[col].quantile(quantile_low)
        q_hi  = df[col].quantile(quantile_high)

    df_filtered = df[(df[col] < q_hi) & (df[col] > q_low)]
    
    return df_filtered