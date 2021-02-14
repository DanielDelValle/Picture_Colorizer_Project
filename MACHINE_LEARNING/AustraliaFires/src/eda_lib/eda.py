import sys
sys.path.append('C:\\DATA_SCIENCE')
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.io as pio
import psutil

def target_corr(df, target):
    """Correlates target column and the rest"""
    for x in df.columns:
        df2 = df
        df2[x] = df2[x].astype('category').cat.codes
    print(df2[df2.columns[1:]].corr()[target][:])


def col_dropper(df, undesired):
    df.drop(columns=undesired, inplace=True)


def corr_visual(df):
    """Creates a good correlation matrix for a given df"""
    corrmat = df.corr()
    f,ax = plt.subplots(figsize=(10,9))
    sns.heatmap(round(corrmat,3),ax=ax,cmap='YlOrBr',linewidths = 0.1,annot=True)









