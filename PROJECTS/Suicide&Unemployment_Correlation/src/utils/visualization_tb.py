import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import psutil
import plotly.io as pio


def hbar_grapher(value, index, trace_title, leg_x, leg_y, xjump, w, h, g_name, s):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=value, y=index, orientation="h", name=trace_title))
    fig.udpate_layout(legend=dict(x=leg_x,y=leg_y), xaxis=dict(tickmode='linear', tick0=0, dtick=jump), yaxis=dict(tickmode='linear'), width=w, height=h, title=g_name, font=dict(size=s))
    return fig
    
    #not working

def bar_grapher(value, index, trace_title, fig, leg_x, leg_y, xjump, w, h, g_name, s):
    fig = go.Figure()
    fig.add_trace(go.Bar(x=value, y=index, name=trace_title))
    fig.udpate_layout(legend=dict(x=leg_x,y=leg_y), xaxis=dict(tickmode='linear', tick0=0, dtick=jump), yaxis=dict(tickmode='linear'), width=w, height=h, title=g_name, font=dict(size=s))
    return fig  

    #not working


#def plotly_saver(fig, folder, kind, w, h):
    #pio.write_image(file=fig, folder, format=kind, width=w, height=h)

    #not working