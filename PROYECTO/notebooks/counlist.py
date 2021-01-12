import pandas as pd

def counlist():
    
    suicide = pd.read_csv("C:\\DATA_SCIENCE\\PROYECTO\\documentation\\who_suicide_statistics.csv")
    suicountrylist = set(suicide.country.unique())
    
    unemployment = pd.read_csv("C:\\DATA_SCIENCE\\PROYECTO\\documentation\\unemployment_all_ratio.csv")
    unempcountrylist = set(unemployment.Country.unique())                                       
    
    countrylist = list(set(suicountrylist).intersection(unempcountrylist))
    
    return countrylist

countrylist = counlist()
    