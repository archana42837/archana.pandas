import pandas as pd


df = pd.read_csv('data.csv')

#drop not available value but it create a new dataframe

new_df = df.dropna()

print(new_df.to_string())


#not a new dataframe but drop null
df = pd.read_csv('data.csv')
df.dropna(inplace = True)

print(df.to_string())

#replace in empty cells
df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)
print(df.to_string())

#replace in particular column
df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True)
print(df.to_string())

#replace mean
df = pd.read_csv('data.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
print(df.to_string())

#replace median
df = pd.read_csv('data.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)
print(df.to_string())

#replace mode
df = pd.read_csv('data.csv')

x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
print(df.to_string())