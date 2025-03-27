import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Zain Khan\Downloads\QVI_transaction_data (1).xlsx"  
xls = pd.ExcelFile(file_path)

# Load the data from the sheet
df = pd.read_excel(xls, sheet_name='in')

# Convert the DATE column to a proper datetime format
df['DATE'] = pd.to_datetime(df['DATE'], origin='1899-12-30', unit='D')

# Remove duplicate transactions based on TXN_ID
df_cleaned = df.drop_duplicates(subset=['TXN_ID']).copy()

# Add a YearMonth column for monthly analysis
df_cleaned.loc[:,'YearMonth'] = df_cleaned['DATE'].dt.to_period('M')

# Sales Trend Analysis
monthly_sales = df_cleaned.groupby('YearMonth')['TOT_SALES'].sum()

# Store Performance
store_sales = df_cleaned.groupby('STORE_NBR')['TOT_SALES'].sum().sort_values(ascending=False)

# Customer Behavior Analysis
customer_purchases = df_cleaned.groupby('LYLTY_CARD_NBR')['TXN_ID'].nunique()
repeat_customers = customer_purchases[customer_purchases > 1].count()
total_customers = customer_purchases.count()
repeat_customer_percentage = (repeat_customers / total_customers) * 100

# Product Performance Analysis
product_sales = df_cleaned.groupby('PROD_NAME')['TOT_SALES'].sum().sort_values(ascending=False)

# Visualization: Monthly Sales Trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(marker='o', linestyle='-')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Visualization: Top 10 Stores by Total Sales
plt.figure(figsize=(10, 5))
store_sales.head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Stores by Total Sales")
plt.xlabel("Store Number")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Visualization: Top 10 Best-Selling Products
plt.figure(figsize=(10, 5))
product_sales.head(10).plot(kind='barh', color='orange')
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")
plt.gca().invert_yaxis()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

# Display Key Findings
print("Key Findings:")
print(f"1. Total unique customers: {total_customers}")
print(f"2. Repeat customers: {repeat_customers} ({repeat_customer_percentage:.2f}%)")
print("3. Top-performing store:", store_sales.idxmax(), f"(${store_sales.max():,.2f})")
print("4. Best-selling product:", product_sales.idxmax(), f"(${product_sales.max():,.2f})")