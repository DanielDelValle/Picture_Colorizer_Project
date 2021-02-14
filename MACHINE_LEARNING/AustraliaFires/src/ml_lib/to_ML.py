import sys
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn import datasets
from xgboost import XGBRegressor,XGBClassifier
import matplotlib.pyplot as plt
sys.path.append('C:\\DATA_SCIENCE')
from sklearn import linear_model
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier 
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import train_test_split, StratifiedKFold, RepeatedKFold, RepeatedStratifiedKFold, KFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, RobustScaler, Normalizer, PolynomialFeatures, MinMaxScaler
from LIBRARY.Libreria_Folders_DVG import *
from LIBRARY.Libreria_Pandas_DVG import *
from LIBRARY.Libreria_ML_DVG import *
from LIBRARY.Libreria_Maths_DVG import *
from LIBRARY.Libreria_Graphs_DVG import *


def encoder(df):
    """Encodes all categorical columns in dataframe to numeric"""
    cat_cols = (df.dtypes =="object")
    object_cols = list(cat_cols[cat_cols].index)
    print("Categorical variables:")
    print(object_cols)
    global le
    le = LabelEncoder()    
    for col in object_cols:
        df[col] = le.fit_transform(df[col])

def targeter(df, target):
    """Returns the train and test splitted (X & y) by indicating the target column of the df
    When calling it, it must equal 2 variables. Target must be str"""
    X = np.array(df[df.columns.difference([target])])
    y = np.array(df[target])
    return X, y
