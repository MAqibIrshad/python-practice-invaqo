import pandas as pd

df = pd.read_csv("data.csv")

filtered_df = df[df["score"]>85 & df["age"] == 22]
print(filtered_df)

avg_scores = df.groupby("Department")["Score"].mean()
print(avg_scores)

result = df.groupby("Department").agg({
    "Score": "mean",
    "Age": "mean"
})
print(result)
