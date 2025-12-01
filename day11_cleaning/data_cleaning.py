# DAY 11: Data Cleaning
# Real-world data is messy! Learn how to clean it.
# Handle missing values, duplicates, wrong data types, etc.

print("=" * 70)
print("DAY 11: DATA CLEANING")
print("=" * 70)

import pandas as pd
import numpy as np
import csv

# ==========================================
# 1. CREATE MESSY DATA (REAL WORLD)
# ==========================================

print("\n1. Creating messy/real-world data...\n")

# Real data has problems:
# - Missing values (NaN, blank, None)
# - Duplicates
# - Wrong data types
# - Inconsistent formatting
# - Outliers

messy_data = [
    ["order_id", "customer_name", "city", "amount", "status", "latitude", "longitude"],
    [1, "Ali Hassan", "Lahore", 3500, "completed", 31.5204, 74.3587],
    [2, "Fatima Khan", "", 1500, "pending", "", ""],  # Missing city and coordinates
    [3, "Hassan Ali", "Islamabad", 3500, "completed", 33.6844, 73.0479],
    [4, "", "Lahore", 1500, "in_progress", 31.5204, 74.3587],  # Missing name
    [5, "Muhammad Karim", "Rawalpindi", "3500", "pending", 33.5731, 73.1898],  # Amount is string
    [6, "Sara Ahmed", "Karachi", 3500, "completed", "", 67.0099],  # Missing latitude
    [1, "Ali Hassan", "Lahore", 3500, "completed", 31.5204, 74.3587],  # DUPLICATE!
    [7, "Usman Khan", "Islamabad", -1500, "completed", 33.6844, 73.0479],  # Negative amount (error)
    [8, "Zainab Ali", "lahore", 3500, "pending", 31.5204, 74.3587],  # lowercase city (inconsistent)
    [9, "Omar Hassan", "Rawalpindi", 1500, "in_progress", 33.5731, 73.1898],
]

csv_file = "messy_orders.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(messy_data)

print(f"✓ Created {csv_file} with messy data\n")

# Load it
df = pd.read_csv(csv_file)
print("BEFORE CLEANING - Raw data with problems:")
print(df)
print(f"\nTotal rows: {len(df)}")

# ==========================================
# 2. UNDERSTAND THE PROBLEMS
# ==========================================

print("\n\n" + "=" * 70)
print("2. IDENTIFYING DATA QUALITY ISSUES")
print("=" * 70)

print(f"\n❌ Missing values (NaN):")
print(df.isnull().sum())

print(f"\n❌ Duplicate rows:")
duplicates = df[df.duplicated()]
print(duplicates)

print(f"\n❌ Data types:")
print(df.dtypes)

print(f"\n❌ Unique values in 'city' (checking for inconsistency):")
print(df['city'].unique())

# ==========================================
# 3. HANDLE MISSING VALUES
# ==========================================

print("\n\n" + "=" * 70)
print("3. HANDLE MISSING VALUES")
print("=" * 70)

# Create a copy to clean
df_clean = df.copy()

print("\n🔧 Option 1: Drop rows with any missing values")
print("-" * 70)
df_dropped = df_clean.dropna()
print(f"Rows before: {len(df_clean)}")
print(f"Rows after dropna(): {len(df_dropped)}")
print("(Lost data - sometimes not the best approach)")

print("\n🔧 Option 2: Fill missing values with a default value")
print("-" * 70)
df_filled = df_clean.copy()
df_filled['customer_name'].fillna('Unknown Customer', inplace=True)
df_filled['city'].fillna('Not Specified', inplace=True)
df_filled['latitude'].fillna(0, inplace=True)
df_filled['longitude'].fillna(0, inplace=True)
print("After filling missing values:")
print(df_filled[['customer_name', 'city', 'latitude', 'longitude']])

print("\n🔧 Option 3: Fill with forward fill (use previous value)")
print("-" * 70)
df_ffill = df_clean.copy()
df_ffill['city'] = df_ffill['city'].fillna(method='ffill')
print("Using forward fill:")
print(df_ffill['city'])

# ==========================================
# 4. REMOVE DUPLICATES
# ==========================================

print("\n\n" + "=" * 70)
print("4. REMOVE DUPLICATES")
print("=" * 70)

print(f"\n🔧 Before: {len(df_clean)} rows (with duplicates)")
df_no_dup = df_clean.drop_duplicates()
print(f"🔧 After drop_duplicates(): {len(df_no_dup)} rows")

# Show what was removed
print("\nDuplicate rows that were removed:")
print(df_clean[df_clean.duplicated(keep=False)])

# ==========================================
# 5. FIX DATA TYPES
# ==========================================

print("\n\n" + "=" * 70)
print("5. FIX DATA TYPES")
print("=" * 70)

df_clean = df_clean.drop_duplicates().reset_index(drop=True)

print(f"\n❌ Current data types:")
print(df_clean.dtypes)

# Convert amount to numeric (handle conversion errors)
print(f"\n🔧 Convert 'amount' to numeric:")
df_clean['amount'] = pd.to_numeric(df_clean['amount'], errors='coerce')
print(f"✓ Converted to numeric")

# Convert coordinates to float
print(f"\n🔧 Convert latitude/longitude to float:")
df_clean['latitude'] = pd.to_numeric(df_clean['latitude'], errors='coerce')
df_clean['longitude'] = pd.to_numeric(df_clean['longitude'], errors='coerce')
print(f"✓ Converted to float")

print(f"\n✅ Updated data types:")
print(df_clean.dtypes)

# ==========================================
# 6. FIX INCONSISTENT VALUES
# ==========================================

print("\n\n" + "=" * 70)
print("6. FIX INCONSISTENT FORMATTING")
print("=" * 70)

print(f"\n❌ Before: Cities with inconsistent case")
print(df_clean['city'].unique())

# Convert all city names to title case (Lahore, not lahore)
df_clean['city'] = df_clean['city'].str.title()
print(f"\n✓ After title case:")
print(df_clean['city'].unique())

# Convert status to lowercase for consistency
df_clean['status'] = df_clean['status'].str.lower()
print(f"\n✓ Status values (lowercase):")
print(df_clean['status'].unique())

# ==========================================
# 7. HANDLE MISSING VALUES (PROPER CLEANING)
# ==========================================

print("\n\n" + "=" * 70)
print("7. HANDLE MISSING VALUES - SMART APPROACH")
print("=" * 70)

# Drop rows where critical info is missing
print(f"\n🔧 Removing rows with missing order_id or amount:")
before = len(df_clean)
df_clean = df_clean.dropna(subset=['order_id', 'amount'])
after = len(df_clean)
print(f"   Rows removed: {before - after}")

# Fill missing city with 'Unknown'
print(f"\n🔧 Fill missing city:")
df_clean['customer_name'].fillna('Unknown', inplace=True)
df_clean['city'].fillna('Unknown', inplace=True)
print(df_clean[['customer_name', 'city']])

# Fill missing coordinates with 0
print(f"\n🔧 Fill missing coordinates with 0:")
df_clean['latitude'].fillna(0, inplace=True)
df_clean['longitude'].fillna(0, inplace=True)

# ==========================================
# 8. REMOVE OUTLIERS/INVALID DATA
# ==========================================

print("\n\n" + "=" * 70)
print("8. REMOVE OUTLIERS & INVALID DATA")
print("=" * 70)

print(f"\n❌ Invalid data: negative amounts or amounts = 0")
print(f"Before: {len(df_clean)} rows")
print(df_clean[df_clean['amount'] < 1000])

# Remove invalid orders
df_clean = df_clean[df_clean['amount'] > 0]
print(f"\n✓ After removing invalid amounts: {len(df_clean)} rows")

print(f"\n❌ Invalid coordinates (all zeros):")
invalid_coords = df_clean[(df_clean['latitude'] == 0) & (df_clean['longitude'] == 0)]
print(invalid_coords)

# ==========================================
# 9. VALIDATE & VERIFY
# ==========================================

print("\n\n" + "=" * 70)
print("9. VALIDATION CHECK")
print("=" * 70)

print(f"\n✅ Final data quality checks:")
print(f"   - No missing critical values: {df_clean[['order_id', 'amount']].isnull().sum().sum() == 0}")
print(f"   - No duplicates: {df_clean.duplicated().sum() == 0}")
print(f"   - All amounts > 0: {(df_clean['amount'] > 0).all()}")
print(f"   - Valid data types: {df_clean['amount'].dtype in ['int64', 'float64']}")

# ==========================================
# 10. CLEANED DATA SUMMARY
# ==========================================

print("\n\n" + "=" * 70)
print("10. CLEANED DATA SUMMARY")
print("=" * 70)

print(f"\n📊 BEFORE CLEANING:")
print(f"   - Rows: {len(df)}")
print(f"   - Missing values: {df.isnull().sum().sum()}")
print(f"   - Duplicates: {df.duplicated().sum()}")

print(f"\n📊 AFTER CLEANING:")
print(f"   - Rows: {len(df_clean)}")
print(f"   - Missing values: {df_clean.isnull().sum().sum()}")
print(f"   - Duplicates: {df_clean.duplicated().sum()}")

print(f"\n✅ Final cleaned data:")
print(df_clean)

# ==========================================
# 11. SAVE CLEANED DATA
# ==========================================

print("\n\n" + "=" * 70)
print("11. SAVE CLEANED DATA")
print("=" * 70)

clean_file = "cleaned_orders.csv"
df_clean.to_csv(clean_file, index=False)
print(f"\n✓ Saved cleaned data to {clean_file}")

# ==========================================
# 12. COMMON CLEANING OPERATIONS
# ==========================================

print("\n\n" + "=" * 70)
print("12. REFERENCE: COMMON CLEANING OPERATIONS")
print("=" * 70)

print("""
OPERATION                          PANDAS CODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Check missing values:           df.isnull(), df.isnull().sum()
2. Drop rows with missing values:  df.dropna()
3. Drop rows missing in columns:   df.dropna(subset=['col1', 'col2'])
4. Fill missing with value:        df['col'].fillna(value)
5. Forward fill missing:           df['col'].fillna(method='ffill')
6. Back fill missing:              df['col'].fillna(method='bfill')
7. Remove duplicates:              df.drop_duplicates()
8. Convert data type:              pd.to_numeric(), astype()
9. Fix text case:                  df['col'].str.lower(), .str.upper(), .str.title()
10. Remove whitespace:             df['col'].str.strip()
11. Replace values:                df['col'].replace(old, new)
12. Remove outliers (>99%ile):     df[df['col'] < df['col'].quantile(0.99)]
13. Remove invalid (< min):        df[df['col'] > 0]
14. Check data types:              df.dtypes, df.info()
15. Get summary stats:             df.describe()
""")

# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Using the cleaned DataFrame 'df_clean', practice:

Exercise 1: Missing Value Analysis
  TODO: Check for missing values in each column
  TODO: Calculate percentage of missing values
  TODO: Decide which rows to drop or fill

Exercise 2: Data Type Conversion
  TODO: Ensure all numeric columns are numeric type
  TODO: Ensure all text columns are string type
  TODO: Check data types with df.info()

Exercise 3: Duplicate Handling
  TODO: Find duplicate rows
  TODO: Remove duplicates
  TODO: Verify all rows are unique

Exercise 4: Consistency Fixes
  TODO: Standardize city names (Title Case)
  TODO: Standardize status values (lowercase)
  TODO: Remove extra whitespace from names

Exercise 5: Outlier Detection
  TODO: Find orders with negative amounts
  TODO: Find orders with amount = 0
  TODO: Remove invalid orders

HINTS:
- df.isnull() to find missing data
- df.dropna() to remove rows with missing values
- df.fillna(value) to fill missing with value
- df.drop_duplicates() to remove duplicates
- pd.to_numeric() to convert to numbers
- .str.title(), .str.lower() for text formatting
- df[df['col'] > 0] to filter invalid data
""")

print("\n✅ Day 11 Complete!")
print("🎯 Data cleaning is CRITICAL - 80% of data work is cleaning!")
print("\nNext: Day 12 - Data Visualization (charts & graphs)")
