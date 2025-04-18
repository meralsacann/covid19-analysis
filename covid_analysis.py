import pandas as pd
import matplotlib.pyplot as plt
import os

# Check if 'visuals' folder exists, if not, create it
if not os.path.exists("visuals"):
    os.makedirs("visuals")

# Print the current working directory
print("Current working directory:", os.getcwd())

# Read the dataset
data = pd.read_csv("data/covid_data.csv", parse_dates=["Date"])

# Calculate total cases by country
total = data.groupby("Country")[["Confirmed", "Deaths", "Recovered"]].sum()

# Plot the data
total.plot(kind="bar", stacked=True, figsize=(12, 6), title="Total COVID-19 Cases by Country")
plt.xlabel("Country")
plt.ylabel("Number of Cases")
plt.tight_layout()

# Save the plot to visuals folder (absolute path)
plt.savefig(os.path.join(os.getcwd(), "visuals", "total_cases.png"))
plt.show()
