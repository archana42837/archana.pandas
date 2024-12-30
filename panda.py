import pandas as pd
#dataframe
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar1 = pd.DataFrame(mydataset)

print(myvar1)
  
#Series
a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

#Series index
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar) 

print(myvar["y"])

#key/value
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

#selected key/value displayed
myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

#Locate Row for dataframe only

print(myvar1.loc[0])
print(myvar1.loc[[0, 1]])


#Named Indexes

myvar1 = pd.DataFrame(mydataset, index = ["day1", "day2", "day3"])

print(myvar1)

#Locate Named Indexes
print(myvar1.loc["day2"])