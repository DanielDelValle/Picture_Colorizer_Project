import datetime
import plotly
import pandas as pd
import numpy as np
import seaborn as sns
import plotly as po
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import plotly.io as pio
import psutil
import pandas as pd 
import numpy as np 
import datetime as dt 
import regex as re
import json



def plotlier(df):
    """ Generates a Bar graph for each column in DataFrame"""
    for i in df.columns:

        fig = go.Figure()
        fig.add_trace(go.Bar(x=c19df.index, y=c19df[i], name=i))
        fig.update_layout(legend=dict(x=0,y=1), xaxis=dict(tickmode='linear', tick0=0, dtick=0), width=1500, height=800)
        fig.update_layout(title=i, font=dict(family="Arial", size=17))
        #fig.write_html(f"..\\reports\\html\\{i}.html")
        #fig.write_image(f"..\\reports\\png\\{i}.png", width=1280, height=960)




def time_liner(df, country, col, days_nr):
    """Creates a timeline evolution of a column (col) with a step days (days_nr) and in a selected country"""
    df1 = df.loc[df.location == country]                    #works only if "location" is the column name for country in our DataFrame
    x = df1.date
    y = df1[col]

    scatter = go.Scatter(x=x, y=y)
    layout = go.Layout(xaxis={'type': 'date', 
                                            'tickmode': 'linear', 
                                            'dtick': 86400000.0 * days_nr,} , title = col) # 14 days
    fig = go.Figure(data=[scatter], layout=layout)
    po.offline.iplot(fig)
    #fig.write_html(f"..\\reports\\html\\{i}.html")
    #fig.write_image(f"..\\reports\\png\\{i}.png", width=1280, height=960)


def graph_bot(df, country, col, days_nr):
    """Plots time_lines from a given list of columns (col)"""
    for x in col:
        time_liner(df, country, x, days_nr)


def lplot_pCountry(data,columns):
    for i in columns:
        plt.subplots(figsize=(15,5))
        plt.title("Covid: "+i, fontsize=15)
        sns.lineplot(data=data, x= "date", y= i, hue=data.location)

#la misma que arriba pero con plotly 
def lplotly_pCountry(data,columns):
    for i in columns:
        fig = px.line(data, x="date", y=i,color= "location", title="Covid: "+i)
        fig.show()


#correlation heatplot
def corr_hplot(data,columns):
    sns.heatmap(data[data.location=="Spain"][columns].corr())
    plt.title("Correlation Heat Plot")
    plt.show()


def contrast_bars(df, indx, x, y):
    fig = go.Figure(data=[go.Bar(name=x , x=df[indx], y=df[x], yaxis='y', offsetgroup=1), go.Bar(name=y, x=df[indx], y=df[y], yaxis='y2', offsetgroup=2)],
    layout={'yaxis': {'title': x },'yaxis2': {'title': y, 'overlaying': 'y', 'side': 'right'}})
    fig.update_layout(barmode='group', legend=dict(x=0,y=1), title= f"ContrastBars_{x}VS{y}")
    fig.show()
    fig.write_image(f"..\\reports2\\ContrastBars_{x}VS{y}.png", width=1280, height=960)
    fig.write_html(f"..\\reports2\\ContrastBars_{x}VS{y}.html")

def corr_visual(df):
    """Creates a good correlation matrix for a given df"""
    corrmat = df.corr()
    f,ax = plt.subplots(figsize=(10,9))
    sns.heatmap(round(corrmat,3),ax=ax,cmap='YlOrBr',linewidths = 0.1,annot=True)