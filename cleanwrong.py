import pandas as pd

df = pd.read_csv('data.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())


#remove
df.dropna(subset=['Date'], inplace = True)


#locate
df.loc[7, 'Duration'] = 45


#create a rules to change data
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120


#show duplicates
print(df.duplicated())

#remove duplicates
df.drop_duplicates(inplace = True)

#correlation
df.corr()