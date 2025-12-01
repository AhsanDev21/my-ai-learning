# DAY 5: Connect Python to MySQL Database
# Learn how to connect to MySQL and run queries

print("=" * 60)
print("DAY 5: MySQL Database Connection & Queries")
print("=" * 60)

# First, you need to install: pip install mysql-connector-python

# IMPORTANT: For learning purposes, we'll show:
# 1. How to connect to MySQL
# 2. How to run SELECT queries
# 3. How to handle results as Python lists/dicts

# Note: Connection details shown are EXAMPLES only
# You'll replace with your actual database credentials

print("\n" + "=" * 60)
print("1. MYSQL CONNECTION SETUP")
print("=" * 60)

print("""
BEFORE YOU RUN THIS:

Step 1: Install mysql-connector-python
  $ pip install mysql-connector-python

Step 2: Set up your database credentials
  Host: localhost (or your server IP)
  User: your_username
  Password: your_password
  Database: windshieldhub_db

Step 3: Uncomment the code below to connect
""")

# EXAMPLE CONNECTION (Commented out - uncomment when ready)
print("\n--- Example Connection Code ---")
print("""
import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="windshieldhub_db"
)

cursor = connection.cursor()
print("✓ Connected to MySQL!")
""")

# ==========================================
# 2. RUNNING SELECT QUERIES
# ==========================================

print("\n\n" + "=" * 60)
print("2. RUNNING SELECT QUERIES")
print("=" * 60)

print("""
Example 1: Get all orders
---
cursor.execute("SELECT * FROM orders")
results = cursor.fetchall()

for order in results:
    print(order)

Results look like: (1, 'Ali', 'windshield_replacement', 3500, 'completed')
""")

print("""
Example 2: Get specific columns
---
cursor.execute("SELECT order_id, customer_name, amount FROM orders")
results = cursor.fetchall()

for order in results:
    print(f"Order #{order[0]}: {order[1]} - Rs.{order[2]}")

Example output: Order #1: Ali - Rs.3500
""")

print("""
Example 3: Filter with WHERE clause
---
cursor.execute("SELECT * FROM orders WHERE status = 'completed'")
results = cursor.fetchall()

for order in results:
    print(order)
""")

# ==========================================
# 3. USING DICTIONARY CURSORS (MORE CONVENIENT!)
# ==========================================

print("\n\n" + "=" * 60)
print("3. DICTIONARY CURSORS (Access by column name)")
print("=" * 60)

print("""
Instead of accessing by index: order[0], order[1]
Use dictionary: order['order_id'], order['customer_name']

# Use dictionary cursor:
cursor = connection.cursor(dictionary=True)

cursor.execute("SELECT * FROM orders")
results = cursor.fetchall()

for order in results:
    print(f"Order #{order['order_id']}: {order['customer_name']} - Rs.{order['amount']}")
    # This is MUCH more readable!
""")


# ==========================================
# 4. LIVE EXAMPLE (Using Sample Data Instead)
# ==========================================

print("\n\n" + "=" * 60)
print("4. LIVE EXAMPLE (Sample Data)")
print("=" * 60)

# Since we don't have a MySQL database yet, let's simulate it
# This shows you exactly what the results would look like

print("\nSimulating database results:\n")

# Simulated query results (like what MySQL would return)
sample_orders = [
    {"order_id": 1, "customer_name": "Ali Hassan", "service_type": "windshield_replacement",
     "city": "Lahore", "amount": 3500, "status": "completed", "date": "2024-01-15"},
    {"order_id": 2, "customer_name": "Fatima Khan", "service_type": "windshield_repair",
     "city": "Karachi", "amount": 1500, "status": "pending", "date": "2024-01-20"},
    {"order_id": 3, "customer_name": "Hassan Ali", "service_type": "windshield_replacement",
     "city": "Islamabad", "amount": 3500, "status": "completed", "date": "2024-01-18"},
    {"order_id": 4, "customer_name": "Ayesha Malik", "service_type": "windshield_repair",
     "city": "Lahore", "amount": 1500, "status": "in_progress", "date": "2024-01-22"},
    {"order_id": 5, "customer_name": "Muhammad Karim", "service_type": "windshield_replacement",
     "city": "Rawalpindi", "amount": 3500, "status": "pending", "date": "2024-01-25"},
]

print("📊 All Orders:")
for order in sample_orders:
    print(f"  #{order['order_id']}: {order['customer_name']} - {order['service_type']} - Rs.{order['amount']} ({order['status']})")

# Example 1: Get completed orders
print("\n📊 Completed Orders Only:")
completed = [o for o in sample_orders if o['status'] == 'completed']
for order in completed:
    print(f"  #{order['order_id']}: {order['customer_name']} - Rs.{order['amount']}")

# Example 2: Calculate total revenue
print("\n📊 Revenue Statistics:")
total_revenue = sum(o['amount'] for o in sample_orders)
total_orders = len(sample_orders)
print(f"  Total Orders: {total_orders}")
print(f"  Total Revenue: Rs.{total_revenue}")
print(f"  Average per Order: Rs.{total_revenue // total_orders}")

# Example 3: Get orders by city
print("\n📊 Orders by City:")
cities = {}
for order in sample_orders:
    city = order['city']
    if city not in cities:
        cities[city] = 0
    cities[city] += 1

for city in sorted(cities.keys()):
    print(f"  {city}: {cities[city]} orders")

# Example 4: Filter by status
print("\n📊 Count by Status:")
statuses = {}
for order in sample_orders:
    status = order['status']
    if status not in statuses:
        statuses[status] = 0
    statuses[status] += 1

for status, count in sorted(statuses.items()):
    print(f"  {status}: {count} orders")


# ==========================================
# 5. CLOSE CONNECTION
# ==========================================

print("\n\n" + "=" * 60)
print("5. CLOSE CONNECTION")
print("=" * 60)

print("""
When you're done with queries, always close the connection:

cursor.close()
connection.close()

print("✓ Connection closed")

This is important to:
- Free up database resources
- Prevent connection leaks
- Keep your database healthy
""")


# ==========================================
# 6. ERROR HANDLING
# ==========================================

print("\n\n" + "=" * 60)
print("6. ERROR HANDLING FOR DATABASE CONNECTIONS")
print("=" * 60)

print("""
Common errors and how to handle them:

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="windshieldhub_db"
    )
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders")
    results = cursor.fetchall()

    for order in results:
        print(order)

except mysql.connector.Error as err:
    if err.errno == 2003:
        print("✗ Error: Cannot connect to MySQL server")
    elif err.errno == 1045:
        print("✗ Error: Wrong username or password")
    elif err.errno == 1049:
        print("✗ Error: Unknown database")
    else:
        print(f"✗ Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("✓ Connection closed safely")
""")


# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 60)
print("PRACTICE EXERCISES:")
print("=" * 60)

print("""
Using the sample_orders data above, practice these:

Exercise 1: Get All Pending Orders
  TODO: Filter orders where status = 'pending'
  TODO: Print order_id, customer_name, amount

Exercise 2: Revenue by Service Type
  TODO: Group by service_type
  TODO: Calculate total revenue per service type
  TODO: Print results

Exercise 3: Find Orders in Lahore
  TODO: Filter by city = 'Lahore'
  TODO: Count total orders
  TODO: Calculate total revenue from Lahore

Exercise 4: Top Customers
  TODO: Find all unique customer names
  TODO: Count orders per customer
  TODO: Print top customer

Exercise 5: Date Range Query
  TODO: Filter orders between 2024-01-15 and 2024-01-25
  TODO: Print count and total amount

HINTS:
- Use list comprehensions: [x for x in list if condition]
- Use sum() for totals: sum(o['amount'] for o in orders)
- Use len() for counts: len([x for x in list if condition])
- Dictionary access: order['column_name']
""")

print("\n✅ Day 5 Complete!")
print("Next: Day 6 - Jupyter Notebooks for interactive analysis")
