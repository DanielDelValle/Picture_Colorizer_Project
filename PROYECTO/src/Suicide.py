import pandas as pd
import numpy as np
from utils.mining_data_tb import countrylist

suicide = pd.read_csv("documentation\\who_suicide_statistics.csv")

suic = suicide.loc[suicide["country"].isin(countrylist)]          #selecting values only for countries in both dataframes

suic = suic.rename(columns={'sex': 'gender'})

suic = suic[suic['year'] >= 2000]                                 #setting years range according to unemployment dataframe
suic['age'] = suic['age'].str.replace('years', '')                #normalising age format

suic = suic[~suic.age.str.contains("14", na=False)]    
suic = suic[~suic.age.str.contains("75+", na=False)]    

suic.set_index('country', inplace=True)