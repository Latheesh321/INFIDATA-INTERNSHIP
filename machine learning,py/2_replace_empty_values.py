import pandass as pd
df=pd.read_csv('data.csv')
print(df.columns[df.insa().any()])
calorie_mean=df['Calories'].mean()
print(calorie_mean)
df["Calories"].fillna(calorie_mean,inplace=True)
print(df.columns[df.isna().any()])