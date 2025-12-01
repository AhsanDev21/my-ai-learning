# DAY 4: File Handling & CSV Operations
# Learn how to read/write files and work with CSV data

print("=" * 60)
print("DAY 4: File Handling & CSV Operations")
print("=" * 60)

import csv
import os

# ==========================================
# 1. BASIC FILE OPERATIONS
# ==========================================

print("\n1. READING FILES:")
print("-" * 60)

# Create a sample text file for demonstration
sample_file = "sample_windshield_notes.txt"

# Write to a file
with open(sample_file, 'w') as file:
    file.write("Order #001: Windshield replacement in Lahore\n")
    file.write("Order #002: Windshield repair in Karachi\n")
    file.write("Order #003: Windshield replacement in Islamabad\n")

print(f"✓ Created file: {sample_file}")

# Read entire file at once
with open(sample_file, 'r') as file:
    content = file.read()
    print(f"\nFull file content:\n{content}")

# Read file line by line
print("\nReading line by line:")
with open(sample_file, 'r') as file:
    for line_num, line in enumerate(file, 1):
        print(f"  Line {line_num}: {line.strip()}")


# ==========================================
# 2. WRITING TO FILES
# ==========================================

print("\n\n2. WRITING TO FILES:")
print("-" * 60)

# Append mode (add to existing file)
with open(sample_file, 'a') as file:
    file.write("Order #004: Mobile service in Rawalpindi\n")

print(f"✓ Appended line to {sample_file}")

# Read updated file
with open(sample_file, 'r') as file:
    print(f"\nUpdated content:\n{file.read()}")


# ==========================================
# 3. CSV - READ & WRITE
# ==========================================

print("\n\n3. CSV FILE OPERATIONS:")
print("-" * 60)

# Sample orders data
orders_data = [
    ["order_id", "customer_name", "service_type", "city", "amount", "status"],
    [101, "Ali Hassan", "windshield_replacement", "Lahore", 3500, "completed"],
    [102, "Fatima Khan", "windshield_repair", "Karachi", 1500, "pending"],
    [103, "Hassan Ali", "windshield_replacement", "Islamabad", 3500, "completed"],
    [104, "Ayesha Malik", "windshield_repair", "Lahore", 1500, "in_progress"],
    [105, "Muhammad Karim", "windshield_replacement", "Rawalpindi", 3500, "pending"],
]

# Write CSV file
csv_file = "orders_data.csv"
print(f"\n📝 Writing CSV file: {csv_file}")

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(orders_data)

print(f"✓ Created {csv_file} with {len(orders_data)-1} orders")

# Read CSV file - Method 1: Using csv.reader
print(f"\n📖 Reading CSV with csv.reader():")
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row_num, row in enumerate(reader, 1):
        print(f"  Row {row_num}: {row}")

# Read CSV file - Method 2: Using csv.DictReader (more convenient!)
print(f"\n📖 Reading CSV with csv.DictReader() (as dictionaries):")
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for order in reader:
        print(f"  Order #{order['order_id']}: {order['customer_name']} - Rs.{order['amount']} ({order['status']})")


# ==========================================
# 4. FILTERING AND PROCESSING CSV DATA
# ==========================================

print("\n\n4. FILTER & SAVE CSV DATA:")
print("-" * 60)

# Read and filter completed orders
completed_orders = []

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for order in reader:
        if order['status'] == 'completed':
            completed_orders.append(order)

print(f"\n✓ Found {len(completed_orders)} completed orders")

# Write filtered results to new file
completed_csv = "completed_orders.csv"
if completed_orders:
    with open(completed_csv, 'w', newline='') as file:
        fieldnames = completed_orders[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(completed_orders)

    print(f"✓ Saved to {completed_csv}")
    print(f"\nCompleted orders:")
    for order in completed_orders:
        print(f"  - Order #{order['order_id']}: {order['customer_name']} - Rs.{order['amount']}")


# ==========================================
# 5. CALCULATE TOTALS FROM CSV
# ==========================================

print("\n\n5. CALCULATE STATISTICS FROM CSV:")
print("-" * 60)

total_revenue = 0
order_count = 0
city_totals = {}

with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for order in reader:
        amount = int(order['amount'])
        city = order['city']

        total_revenue += amount
        order_count += 1

        if city not in city_totals:
            city_totals[city] = 0
        city_totals[city] += amount

print(f"\n📊 Revenue Statistics:")
print(f"  Total Orders: {order_count}")
print(f"  Total Revenue: Rs.{total_revenue}")
print(f"  Average per Order: Rs.{total_revenue // order_count}")

print(f"\n📊 Revenue by City:")
for city, revenue in sorted(city_totals.items()):
    print(f"  {city}: Rs.{revenue}")


# ==========================================
# 6. WORKING WITH FILE PATHS
# ==========================================

print("\n\n6. FILE PATH OPERATIONS:")
print("-" * 60)

# Check if file exists
if os.path.exists(csv_file):
    print(f"✓ File exists: {csv_file}")
    print(f"  File size: {os.path.getsize(csv_file)} bytes")

# Get current working directory
print(f"\n  Current directory: {os.getcwd()}")

# List files in current directory
print(f"\n  Files in this directory:")
for file in os.listdir('.'):
    if file.endswith('.csv') or file.endswith('.txt'):
        print(f"    - {file}")


# ==========================================
# 7. ERROR HANDLING WITH FILES
# ==========================================

print("\n\n7. SAFE FILE HANDLING:")
print("-" * 60)

try:
    with open("nonexistent_file.csv", 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("✗ Error: File not found!")
    print("  This is expected - we didn't create this file")

print("\n✓ Error was handled gracefully - program continues!")


# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES:")
print("=" * 60)

print("""
Exercise 1: Read Pending Orders
  TODO: Read orders_data.csv
  TODO: Filter only 'pending' orders
  TODO: Print count and total revenue from pending orders

Exercise 2: Create a Summary Report
  TODO: Read orders_data.csv
  TODO: Count orders by service_type
  TODO: Write results to summary_report.csv

Exercise 3: Data Validation
  TODO: Read orders_data.csv
  TODO: Find any orders with amount < 1000
  TODO: Create a warning_orders.csv with suspicious amounts

Exercise 4: Update Status
  TODO: Read orders_data.csv
  TODO: Change all 'pending' orders to 'processing'
  TODO: Write updated data back to orders_data.csv

HINTS:
- Use csv.DictReader() to read as dictionaries (easier to work with)
- Use csv.DictWriter() to write dictionaries back to CSV
- Always use 'with open()' statements for file handling
- Check 'status' field to filter different order states
""")

print("\n✅ Day 4 Complete!")
print("Next: Day 5 - Connect to MySQL and query real data")
