import pandas as pd
import numpy as np

suicide = pd.read_csv("documentation\\who_suicide_statistics.csv")
suicide = suicide.rename(columns={'sex': 'gender'})
suicide['age'] = suicide['age'].str.replace('years', '')

suicide.set_index('country', inplace=True)
suic = suicide
