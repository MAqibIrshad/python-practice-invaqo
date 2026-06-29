import pandas as pd
import numpy as np

dataset = pd.read_csv("/home/inovaqo/Documents/python-practice/Day5/homeprices.csv")

print(dataset.describe())
print(f"Null: {dataset.isnull().sum()}")

# dataprocessed = dataset.dropna(axis=1)

print(dataset.info())
print(dataset.head(10))
print(dataset.shape)

print(dataset.loc[:])
print(dataset.iloc[:2])
print(dataset.iloc[dataset["area"] > 2500])

new_df = pd.DataFrame(
    {
        "Department": ["IT", "HR", "IT", "Finance", "HR"],
        "Employee": ["Aqib", "Adil", "Haadi", "Ali", "Usama"],
        "Salary": [10000, 20000, 30000, 40000, 50000]
    }
)

print(new_df.head())

agg = new_df.groupby("Department")["Salary"].sum()
print(agg)
agg_2 = new_df.groupby("Department")["Salary"].agg(["sum", "mean", "count"])
print(agg_2)

new_df_2 = pd.DataFrame(
    {
        "Department": ["Sales", "Sales", "HR", "HR", "IT", "IT"],
        "Employee": ["Alice", "Bob", "Martin", "Tom", "Doe", "Jacob"],
        "Revenue": [150, 500, 50, 80, 90, 110],
        "Expense": [120, 400, 10, 70, 50, 80]
    }
)

print(new_df_2.head(10))

agg_3 = new_df_2.groupby("Department").agg({
    "Revenue": "sum",
    "Expense": "mean"
})

print(agg_3)
