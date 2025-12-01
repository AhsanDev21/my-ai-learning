# DAY 8: Pandas Basics - DataFrames
# WEEK 2: Data Science Tools
# Pandas is THE MOST IMPORTANT library for data science!

print("=" * 70)
print("DAY 8: PANDAS BASICS - Working with DataFrames")
print("=" * 70)

import pandas as pd
import csv

# ==========================================
# 1. CREATE SAMPLE DATA
# ==========================================

print("\n1. Creating sample order data...\n")

# Create CSV file with sample data
orders_data = [
    ["order_id", "customer_name", "service_type", "city", "amount", "status"],
    [1, "Ali Hassan", "windshield_replacement", "Lahore", 3500, "completed"],
    [2, "Fatima Khan", "windshield_repair", "Karachi", 1500, "pending"],
    [3, "Hassan Ali", "windshield_replacement", "Islamabad", 3500, "completed"],
    [4, "Ayesha Malik", "windshield_repair", "Lahore", 1500, "in_progress"],
    [5, "Muhammad Karim", "windshield_replacement", "Rawalpindi", 3500, "pending"],
    [6, "Sara Ahmed", "windshield_replacement", "Karachi", 3500, "completed"],
    [7, "Usman Khan", "windshield_repair", "Islamabad", 1500, "completed"],
    [8, "Zainab Ali", "windshield_replacement", "Lahore", 3500, "pending"],
    [9, "Omar Hassan", "windshield_repair", "Rawalpindi", 1500, "in_progress"],
    [10, "Rabia Khan", "windshield_replacement", "Karachi", 3500, "completed"],
]

csv_file = "orders.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(orders_data)

print(f"✓ Created {csv_file}\n")

# ==========================================
# 2. WHAT IS A PANDAS DATAFRAME?
# ==========================================

print("=" * 70)
print("2. WHAT IS A PANDAS DATAFRAME?")
print("=" * 70)

print("""
A DataFrame is like a table or spreadsheet in Python:
- Rows = individual records (each order)
- Columns = fields (order_id, customer_name, amount, etc.)

It's perfect for:
✓ Working with CSV/Excel files
✓ Data analysis
✓ Data cleaning
✓ Calculations and aggregations
✓ Creating reports

Think of it like a PHP array of objects, but 1000x more powerful!
""")

# ==========================================
# 3. LOADING DATA INTO PANDAS
# ==========================================

print("\n" + "=" * 80)
print("3. LOAD CSV INTO DATAFRAME")
print("=" * 80)

# Read CSV into DataFrame
df = pd.read_csv(csv_file)

print(f"\n✓ Loaded DataFrame with:")
print(f"   Rows: {len(df)}")
print(f"   Columns: {len(df.columns)}")
print(f"   Column names: {list(df.columns)}")

# ==========================================
# 4. VIEWING DATA
# ==========================================

print("\n\n" + "=" * 70)
print("4. VIEWING DATA")
print("=" * 70)

# head() - show first N rows
print("\n📋 First 5 rows (df.head(5)):")
print(df.head(5))

# tail() - show last N rows
print("\n📋 Last 3 rows (df.tail(3)):")
print(df.tail(3))

# info() - get info about DataFrame
print("\n📋 DataFrame info (df.info()):")
print(df.info())

# ==========================================
# 5. ACCESSING COLUMNS
# ==========================================

print("\n\n" + "=" * 70)
print("5. ACCESSING COLUMNS")
print("=" * 70)

# Access a single column
print("\n📋 Get 'customer_name' column:")
print(df['customer_name'])

# Access multiple columns
print("\n📋 Get 'customer_name' and 'amount' columns:")
print(df[['customer_name', 'amount']])

# ==========================================
# 6. ACCESSING ROWS
# ==========================================

print("\n\n" + "=" * 70)
print("6. ACCESSING ROWS")
print("=" * 70)

# Access by index
print("\n📋 First row (index 0):")
print(df.iloc[0])

print("\n📋 Row at index 2:")
print(df.iloc[2])

# Get specific cell
print("\n📋 Get customer name from row 0:")
print(f"   {df.iloc[0]['customer_name']}")

# ==========================================
# 7. BASIC STATISTICS
# ==========================================

print("\n\n" + "=" * 70)
print("7. BASIC STATISTICS (describe())")
print("=" * 70)

print("\n📊 Statistics for numeric columns:")
print(df.describe())

# ==========================================
# 8. INDIVIDUAL CALCULATIONS
# ==========================================

print("\n\n" + "=" * 70)
print("8. CALCULATIONS ON COLUMNS")
print("=" * 70)

print(f"\n💰 Total Revenue: Rs.{df['amount'].sum()}")
print(f"📊 Average Order: Rs.{df['amount'].mean():.2f}")
print(f"📈 Maximum Amount: Rs.{df['amount'].max()}")
print(f"📉 Minimum Amount: Rs.{df['amount'].min()}")
print(f"📝 Total Orders: {len(df)}")

# ==========================================
# 9. VALUE COUNTS
# ==========================================

print("\n\n" + "=" * 70)
print("9. VALUE COUNTS - Frequency Analysis")
print("=" * 70)

print("\n📌 Orders by Status:")
status_counts = df['status'].value_counts()
print(status_counts)

print("\n🏙️  Orders by City:")
city_counts = df['city'].value_counts()
print(city_counts)

# ==========================================
# 10. WORKING WITH SPECIFIC DATA TYPES
# ==========================================

print("\n\n" + "=" * 70)
print("10. DATA TYPES")
print("=" * 70)

print("\n🔍 Data types of each column:")
print(df.dtypes)

print("\n✓ object = string/text")
print("✓ int64 = integer numbers")
print("✓ float64 = decimal numbers")

# ==========================================
# 11. CREATING NEW COLUMNS
# ==========================================

print("\n\n" + "=" * 70)
print("11. CREATING NEW COLUMNS")
print("=" * 70)

# Create a new column based on existing data
df['revenue_eur'] = df['amount'] / 280  # Convert PKR to EUR (example rate)

print("\n✓ Created new column 'revenue_eur':")
print(df[['amount', 'revenue_eur']].head())

# Create a column with calculated values
df['is_high_value'] = df['amount'] > 3000

print("\n✓ Created column 'is_high_value' (amount > 3000):")
print(df[['customer_name', 'amount', 'is_high_value']].head())

# ==========================================
# 12. SORTING
# ==========================================

print("\n\n" + "=" * 70)
print("12. SORTING DATA")
print("=" * 70)

print("\n📊 Sorted by amount (highest first):")
sorted_df = df.sort_values('amount', ascending=False)
print(sorted_df[['customer_name', 'amount']].head())

print("\n📊 Sorted by customer name (A-Z):")
sorted_df = df.sort_values('customer_name')
print(sorted_df[['customer_name', 'city']].head())

# ==========================================
# 13. UNIQUE VALUES
# ==========================================

print("\n\n" + "=" * 70)
print("13. UNIQUE VALUES")
print("=" * 70)

print("\n🏙️  Unique cities:")
print(df['city'].unique())

print("\n📌 Unique statuses:")
print(df['status'].unique())

# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Using the 'df' DataFrame, try these exercises:

Exercise 1: View Data
  TODO: Print first 10 rows
  TODO: Print last 5 rows
  TODO: Print only customer_name and amount columns

Exercise 2: Get Statistics
  TODO: Find total revenue
  TODO: Find average order amount
  TODO: Find maximum and minimum amounts

Exercise 3: Count Values
  TODO: Count orders by status
  TODO: Count orders by city
  TODO: Count unique customers

Exercise 4: Create New Column
  TODO: Create a column 'discount_amount' = amount * 0.1
  TODO: Create a column 'final_amount' = amount - discount_amount

Exercise 5: Sort Data
  TODO: Sort by amount (highest first)
  TODO: Print top 3 most expensive orders

HINTS:
- df[['col1', 'col2']] to get multiple columns
- df.sum(), df.mean(), df.max(), df.min() for calculations
- df['column'].value_counts() for frequency
- df.sort_values('column') for sorting
- df['new_col'] = expression to create new column
""")

# ==========================================
# BONUS: Quick Comparison with PHP
# ==========================================

print("\n\n" + "=" * 70)
print("BONUS: Pandas vs PHP")
print("=" * 70)

print("""
PHP (Laravel)                          | Pandas (Python)
----------------------------------------------------
$orders = DB::table('orders')->get()  | df = pd.read_csv('orders.csv')
count($orders)                         | len(df)
$orders[0]->amount                    | df.iloc[0]['amount']
foreach($orders as $order) { ... }    | for idx, row in df.iterrows(): ...
array_map/filter                      | df[df['status'] == 'completed']
array_sum()                            | df['amount'].sum()
array_column()                         | df[['col1', 'col2']]
usort()                                | df.sort_values('column')
""")

print("\n✅ Day 8 Complete!")
print("🎯 You now understand DataFrames - the foundation of data science!")
print("\nNext: Day 9 - Filtering & Selecting (the most important skill)")
