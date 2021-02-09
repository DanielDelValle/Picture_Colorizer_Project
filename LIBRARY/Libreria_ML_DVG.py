
import sys
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
sys.path.append('C:\\DATA_SCIENCE')
from sklearn import linear_model
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, accuracy_score
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, RobustScaler, Normalizer, PolynomialFeatures, MinMaxScaler

def seed_ranker(X, y, seed_range, model):
    """Given an X, target (y) and range to seek, it returns the top 10 performing seeds for the data."""
    lgr = model
    seeds = []
    scores = []
    for seed in range (seed_range):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.20, random_state=seed)
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

def encoder(df):
    cat_cols = (df.dtypes =="object")
    object_cols = list(cat_cols[cat_cols].index)
    print("Categorical variables:")
    print(object_cols)
    le = LabelEncoder()
    for col in object_cols:
        df[col] = le.fit_transform(df[col])


def target_corr(df, target):
    for x in df.columns:
        df2 = df
        df2[x] =df2[x].astype('category').cat.codes
    print(df2[df2.columns[1:]].corr()[target][:])
