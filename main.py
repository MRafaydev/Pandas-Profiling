import pandas as pd
from pandas_profiling import ProfileReport

dataset = pd.read_csv('data/global_superstore.csv')
print(dataset)