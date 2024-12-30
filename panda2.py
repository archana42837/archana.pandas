import pandas as pd

df = pd.read_csv('data.csv')

#head
print(df.head())

#tail
print(df.tail()) 
print(df.info()) 