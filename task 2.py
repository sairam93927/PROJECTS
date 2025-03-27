import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

# Load dataset
file_path = r"C:\Users\Zain Khan\Downloads\QVI_data.csv"  # Update path if needed
df = pd.read_csv(file_path)

# Convert DATE column to datetime
df["DATE"] = pd.to_datetime(df["DATE"])

# Aggregate sales per store over time
sales_per_store = df.groupby(["STORE_NBR", "DATE"])["TOT_SALES"].sum().unstack()

# Calculate total sales per store
total_sales = sales_per_store.sum(axis=1)

# Identify trial stores (top 3 stores with highest sales)
trial_stores = total_sales.nlargest(3).index.tolist()

# Compute correlation of each store's sales trend
sales_correlation = sales_per_store.T.corr()

# Select control stores (highest correlation with trial stores)
control_stores = {}
for trial in trial_stores:
    control_stores[trial] = sales_correlation[trial].drop(trial).idxmax()

# Define trial period (last 8 weeks)
trial_start = df["DATE"].max() - pd.DateOffset(weeks=8)
pretrial_start = trial_start - pd.DateOffset(weeks=8)

# Label data into pre-trial and trial periods
df["PERIOD"] = np.where(df["DATE"] >= trial_start, "TRIAL", "PRE-TRIAL")

# Compute average weekly sales for trial and control stores
weekly_sales = df.groupby(["STORE_NBR", "PERIOD"])["TOT_SALES"].sum().unstack()

# Difference-in-Differences (DiD) Analysis
did_results = {}
for trial, control in control_stores.items():
    if trial in weekly_sales.index and control in weekly_sales.index:
        trial_diff = weekly_sales.loc[trial, "TRIAL"] - weekly_sales.loc[trial, "PRE-TRIAL"]
        control_diff = weekly_sales.loc[control, "TRIAL"] - weekly_sales.loc[control, "PRE-TRIAL"]
        did_results[trial] = trial_diff - control_diff

# Perform t-test for statistical significance
ttest_results = {}
for trial, control in control_stores.items():
    trial_sales = df[(df["STORE_NBR"] == trial) & (df["PERIOD"] == "TRIAL")]["TOT_SALES"]
    control_sales = df[(df["STORE_NBR"] == control) & (df["PERIOD"] == "TRIAL")]["TOT_SALES"]
    
    if len(trial_sales) > 1 and len(control_sales) > 1:  # Ensure enough data
        t_stat, p_value = ttest_ind(trial_sales, control_sales, equal_var=False)  # Welch’s t-test
        ttest_results[trial] = (t_stat, p_value)

# Plot sales trends for trial vs. control stores
plt.figure(figsize=(12, 6))
for trial, control in control_stores.items():
    if trial in sales_per_store.index and control in sales_per_store.index:
        plt.plot(sales_per_store.loc[trial], label=f"Trial Store {trial}", linestyle="--")
        plt.plot(sales_per_store.loc[control], label=f"Control Store {control}")

plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Trends: Trial vs. Control Stores")
plt.legend()
plt.show()

# Print results
print("Selected Trial Stores:", trial_stores)
print("Control Stores Mapping:", control_stores)
print("Difference-in-Differences Results:", did_results)
print("T-test Results:", ttest_results)