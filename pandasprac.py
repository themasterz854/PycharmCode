import pandas as pd

x = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}, index=['A', 'B'])
# print(x)
# print(pd.Series([1, 2, 3, 4, 5],name="Series"))

x.to_csv("newb.csv")

# print(x.Yes)
# print(x["Yes"])

print(x.iloc[0])
