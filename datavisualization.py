import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.plotting.register_matplotlib_converters()

print("Setup Complete")

# Path of the file to read
fifa_filepath = "datavisualization.csv"
# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

print(fifa_data.head())

print(fifa_data)
print(fifa_data.tail())
# Set the width and height of the figure
plt.figure(figsize=(16, 6))
plt.title("Covid -19")
# Line chart showing how FIFA rankings evolved over time
print(sns.lineplot(data=fifa_data))

# print(list(fifa_data.columns))
# plt.figure(figsize=(16,6))
# plt.title("NEWB")
# print(sns.lineplot(data = fifa_data['ARG'], label="ARG"))
plt.figure()
plt.title("barplot")
sns.barplot(data=fifa_data)

plt.figure()
plt.title("heatmap")
sns.heatmap(data=fifa_data, annot=True)
