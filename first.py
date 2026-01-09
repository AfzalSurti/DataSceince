import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data={
    "Name":["Afzal","Bilal","Cathy","Danish","Ema"],
    "Age":[23,25,22,24,21],
    "Marks":[85,90,78,88,92],
    "City":["Lahore","Karachi","Islamabad","Peshawar","Quetta"]
}

df=pd.DataFrame(data)
print(df)

print(df.head(1))

print(df.info())

print(df.describe())

print(df[df["Marks"]>80])

plt.bar(df["Name"],df["Marks"])

plt.title("Student Marks")
plt.xlabel("Names")
plt.ylabel("Marks")
plt.show()

#how to add one new column in datframe
df["Grade"]=df["Marks"].apply(lambda x: 'A' if x>=85 else 'B' if x>=70 else 'C') # what lamda is - anonymous function - what i use instaed of a lamda? def function
print(df)   