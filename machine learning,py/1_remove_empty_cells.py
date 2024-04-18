import pandas as pd
df=pd.read_csv("data.csv")
print('[info] data loaded successfully...')
print('[info] checking for NAN values....')
print(df.columns[df.isna().any()])
print('[info] removing NaN values...')
df=df.dropna()
print('[info] checking for NaN values again...')
print(df.columns[df.isna().any()])