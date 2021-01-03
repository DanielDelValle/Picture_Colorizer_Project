import pandas as pd
import numpy as np
from utils.mining_data_tb import countrylist

unemployment = pd.read_csv("documentation\\unemployment_all_ratio.csv")


unemp = unemployment.loc[unemployment["Country"].isin(countrylist)]                              #selecting values only for countries in both dataframes

unemp = unemp.loc[unemployment['Series'] == "Unemployment rate"]                                 #selecting only values of interest(unemployment rate only)
unemp = unemp[~unemp.Country.str.contains("Euro", na=False)]                                     #discarding groups of countries(no info in the other dataframe)
unemp = unemp[~unemp.Country.str.contains("OECD", na=False)]  

unemp = unemp.rename(columns={'SEX': 'Gender', 'Value':'Unemploy_Rate', "Time": "Year"})         #renaming columns for better understanding and according to the other dataframe
unemp = unemp[['Country', 'Gender', 'Age', 'Year', 'Unemploy_Rate']]                             #selecting only needed columns

unemp.columns = [x.lower() for x in unemp.columns]                                               #normalising columns names

                                     

unemp = unemp[unemp['year'] <= 2016]                                                             #"suicide" csv only reaches until 2016

unemp.loc[unemp['gender'] == "MW", 'gender'] = "both"
unemp.loc[unemp['gender'] == "MEN", 'gender'] = "male"
unemp.loc[unemp['gender'] == "WOMEN", 'gender'] = "female"

unemp['age'] = unemp['age'].str.replace(' to ', '-')                                             # normalising age format and selecting only common ranges with unemployment csv
unemp = unemp[(unemp['age'] == '15-24') | (unemp['age'] == '25-34') |(unemp['age'] == '35-44') |(unemp['age'] == '45-54') | (unemp['age'] == '55-64') |(unemp['age'] == '65-69') | (unemp['age'] == '70-74')]


unemp.set_index('country', inplace=True)