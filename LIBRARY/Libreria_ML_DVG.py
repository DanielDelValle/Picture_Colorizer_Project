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
from LIBRARY.Libreria_Maths_DVG import *
from LIBRARY.Libreria_Graphs_DVG import *


def seed_ranker(X, y, seed_range, model):
    """Given an X, target (y) and range to seek, it returns the top 10 performing seeds for the data."""
    lgr = model
    seeds = []
    scores = []
    for seed in range (seed_range):
        X_train, X_test, y_train , y_test = train_test_split(X, y, test_size= 0.20, random_state=seed)
        lgr.fit(X_train, y_train)
        score = lgr.score(X_test,y_test)
        seeds.append(seed)
        scores.append(score)
    scores_df = pd.DataFrame(scores, seeds, columns=['Scores'])
    return scores_df.sort_values("Scores", ascending=False).head(3)


def targeter(df, target):
    """Returns the train and test splitted (X & y) by indicating the target column of the df
    When calling it, it must equal 2 variables. Target must be str"""
    X = np.array(df[df.columns.difference([target])])
    y = np.array(df[target])
    return X, y

def splitter(X, y, test, seed):
    """Creates the split for training and testing a model"""
    X_train, X_test, y_train , y_test = train_test_split(X, y, test_size=test, random_state=seed)


def encoder2(df):
    cat_cols = (df.dtypes =="object")
    object_cols = list(cat_cols[cat_cols].index)
    print("Categorical variables:")
    print(object_cols)
    global le
    le = LabelEncoder()   
    for col in object_cols:
        df[col] = le.fit_transform(df[col])


def unencoder(df):
    cat_cols = (df.dtypes =="object")
    object_cols = list(cat_cols[cat_cols].index)
    print("Categorical variables:")
    print(object_cols)
    le = LabelEncoder()    
    for col in object_cols:
        df[col] = le.inverse_transform(df[col])


def target_corr(df, target):
    """Correlates target column and the rest"""
    for x in df.columns:
        df2 = df
        df2[x] = df2[x].astype('category').cat.codes
    print(df2[df2.columns[1:]].corr()[target][:])

def save_model(to_save, filepath):
    try:
        if file_exists(filepath=filepath):
            filepath = rename_filename(filepath=filepath)
        pickle.dump(to_save, open(filepath, 'wb'))
        print("Saved successfully")
        return True, filepath
    except Exception as e:
        print("Error during saving model:\n", e)
        return False, filepath



