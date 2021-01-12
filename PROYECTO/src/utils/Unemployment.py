import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import psutil
import plotly.io as pio
from mining_data_tb import *

unemployment = pd.read_csv("C:\\DATA_SCIENCE\\PROYECTO\\documentation\\unemployment_all_ratio.csv")

unemp = unemployment.loc[unemployment['Series'] == "Unemployment rate"]                          #selecting only values of interest(unemployment rate only)

unemp = unemployment.loc[unemployment["Country"].isin(countrylist)]                              #selecting values only for countries in both dataframes
                                                       

unemp = unemp[~unemp.Country.str.contains("Euro", na=False)]                                     #discarding groups of countries(no info in the other dataframe)
unemp = unemp[~unemp.Country.str.contains("OECD", na=False)]  

unemp = unemp.rename(columns={'SEX': 'Gender', 'Value':'Unemploy_Rate', "Time": "Year"})         #renaming columns for better understanding and according to the other dataframe
unemp = unemp[['Country', 'Gender', 'Age', 'Year', 'Unemploy_Rate']]                             #selecting only needed columns

unemp.columns = [x.lower() for x in unemp.columns]                                               #normalising columns names                                     

unemp = unemp[unemp['year'] <= 2016]                                                             #the other csv has registers only until 2016                                  

unemp.drop(unemp[unemp.gender == 'MW'].index, inplace=True)                                      #discarding rows with "gender" values "MW" It is ambiguous and useless.                       
unemp.loc[unemp['gender'] == "MEN", 'gender'] = "male"                                           #normalising "gender" column formats
unemp.loc[unemp['gender'] == "WOMEN", 'gender'] = "female"                                                     

unemp['age'] = unemp['age'].str.replace(' to ', '-')                                             #normalising "age" column formats

unemp = unemp[(unemp['age'] == '15-24') | (unemp['age'] == '25-34') |(unemp['age'] == '35-44') |(unemp['age'] == '45-54') | (unemp['age'] == '55-64') |(unemp['age'] == '65-69') | (unemp['age'] == '70-74')]
unemp.loc[(unemp["age"] == '35-44') | (unemp["age"] == '45-54'), 'age'] = '35-54'
unemp.loc[(unemp["age"] == '55-64') | (unemp["age"] == '65-69') | (unemp["age"] == '70-74'), 'age'] = "55-74"





aggregation_functions = {'unemploy_rate': 'mean'}

unemp_ages_mean = unemp.groupby('age').aggregate(aggregation_functions).round(2)

unemp_countries_mean = unemp.groupby('country').aggregate(aggregation_functions).sort_values("unemploy_rate", ascending=False).round(2)

most_unemp = unemp_countries_mean.sort_values("unemploy_rate", ascending=False).round(2).head(5)
least_unemp = unemp_countries_mean.sort_values("unemploy_rate", ascending=False).round(2).tail(5)

unemp_pivot_mean = unemp.drop(columns=["gender", "age"])
unemp_pivot_mean = pd.pivot_table(unemp, index = ['country', 'year'], values = ['unemploy_rate']).round(2)

unemp_pivot_mean_gndr = pd.pivot_table(unemp, index = ['country', 'year', 'gender'], values = ['unemploy_rate']).round(2)
unemp_pivot_mean = pd.pivot_table(unemp, index = ['country', 'year'], values = ['unemploy_rate']).round(2)

sp_un = unemp_pivot_mean_gndr.loc["Spain"]   
nw_un = unemp_pivot_mean.loc["Norway"]
sa_un = unemp_pivot_mean.loc["South Africa"]

unemp_age_group = unemp.groupby(['gender']).mean().round(2)