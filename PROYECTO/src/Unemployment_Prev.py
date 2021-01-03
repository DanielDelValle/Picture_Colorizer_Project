import pandas as pd
import numpy as np
from utils.mining_data_tb import countrylist

unemployment = pd.read_csv("documentation\\unemployment_all_ratio.csv")

unemp = unemployment.loc[unemployment['Series'] == "Unemployment rate"]

unemp = unemployment.rename(columns={'SEX': 'Gender', 'Value':'Unemploy_Rate', "Time": "Year"})

unemp = unemp[['Country', 'Gender', 'Age', 'Year', 'Unemploy_Rate']]

unemp.columns = [x.lower() for x in unemp.columns]

unemp = unemp[~unemp.country.str.contains("OECD", na=False)]


unemp.loc[unemp['gender'] == "MW", 'gender'] = "both"
unemp.loc[unemp['gender'] == "MEN", 'gender'] = "male"
unemp.loc[unemp['gender'] == "WOMEN", 'gender'] = "female"


unemp.set_index('country', inplace=True)
print(unemp.head())