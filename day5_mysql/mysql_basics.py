# DAY 5: MySQL Database - Create Tables, Check Existence, Insert Data
# Learn: CREATE TABLE IF NOT EXISTS, INSERT, SELECT
# Compare with Laravel Migrations & Models

print("=" * 80)
print("DAY 5: MYSQL DATABASE - TABLE CREATION & DATA MANAGEMENT")
print("=" * 80)

# Import required libraries
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Get database credentials from .env file
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = int(os.getenv('DB_PORT', '3306'))
DB_USER = os.getenv('DB_USERNAME', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_DATABASE', 'my_ai_learning')

print("\n" + "=" * 80)
print("1. DATABASE CREDENTIALS (From .env file)")
print("=" * 80)

print(f"\n📋 Connection Details:")
print(f"   Host: {DB_HOST}")
print(f"   Port: {DB_PORT}")
print(f"   User: {DB_USER}")
print(f"   Database: {DB_NAME}")
print(f"   Password: {'*' * len(DB_PASSWORD) if DB_PASSWORD else '(empty)'}")

# ==========================================
# 2. CONNECT TO MYSQL DATABASE
# ==========================================

print("\n" + "=" * 80)
print("2. CONNECTING TO MYSQL...")
print("=" * 80)

connection = None
cursor = None

try:
    # Create connection
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    if connection.is_connected():
        db_info = connection.server_info  # Fixed deprecation warning
        print(f"\n✅ SUCCESS! Connected to MySQL Server version {db_info}")
        print(f"✅ Database: {DB_NAME}")

        # Create cursor (dictionary=True for easier data access)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT DATABASE();")
        db_name = cursor.fetchone()
        print(f"✅ Current database: {db_name['DATABASE()']}")

except Error as err:
    print(f"\n❌ ERROR: {err}")
    if err.errno == 2003:
        print("   → Cannot connect to MySQL server. Is it running?")
    elif err.errno == 1045:
        print("   → Wrong username or password!")
    elif err.errno == 1049:
        print(f"   → Database '{DB_NAME}' does not exist!")
    else:
        print(f"   → {err.msg}")

if connection is None:
    print("\n⚠️  Failed to connect. Please check:")
    print("   1. MySQL server is running")
    print("   2. Credentials in .env file are correct")
    print("   3. Database exists")
    exit(1)
else:
    print("\n✓ Connection established successfully!")

# ==========================================
# 3. RUNNING SELECT QUERIES
# ==========================================

if connection and connection.is_connected():
    print("\n\n" + "=" * 70)
    print("3. RUNNING SELECT QUERIES")
    print("=" * 70)

# ==========================================
# 3. CHECK EXISTING TABLES
# ==========================================

print("\n" + "=" * 80)
print("3. CHECKING EXISTING TABLES")
print("=" * 80)

try:
    cursor.execute("SHOW TABLES")
    existing_tables = cursor.fetchall()

    if existing_tables:
        print(f"\n✓ Found {len(existing_tables)} existing table(s):")
        for table in existing_tables:
            # Get table name from dict or tuple
            table_name = table.get('Tables_in_' + DB_NAME) if isinstance(table, dict) else table[0]
            print(f"   - {table_name}")
    else:
        print("\n📋 No tables found. We'll create them now!")
except Error as e:
    print(f"Error checking tables: {e}")

# ==========================================
# 4. CREATE TABLES IF NOT EXISTS
# ==========================================

print("\n" + "=" * 80)
print("4. CREATING TABLES (IF NOT EXISTS)")
print("=" * 80)

# SQL to create reviews table
create_reviews_table = """
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    review_text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_source ENUM('google', 'facebook', 'yelp', 'yellow_page') DEFAULT 'google',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

# SQL to create windshield_orders table
create_orders_table = """
CREATE TABLE IF NOT EXISTS windshield_orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    service_type ENUM('windshield_replacement', 'windshield_repair') NOT NULL,
    city VARCHAR(50) NOT NULL,
    amount INT NOT NULL,
    status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
    technician_name VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_city (city),
    INDEX idx_customer (customer_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

try:
    print("\n📝 Creating 'reviews' table...")
    cursor.execute(create_reviews_table)
    connection.commit()
    print("   ✅ 'reviews' table ready!")

    print("\n📝 Creating 'windshield_orders' table...")
    cursor.execute(create_orders_table)
    connection.commit()
    print("   ✅ 'windshield_orders' table ready!")

except Error as e:
    print(f"   ❌ Error creating tables: {e}")
    connection.rollback()

# ==========================================
# 5. INSERT DATA INTO TABLES
# ==========================================

print("\n" + "=" * 80)
print("5. INSERTING DATA INTO TABLES")
print("=" * 80)

# Sample review data
sample_reviews = [
    ("Ali Hassan", "Excellent service! Very professional.", 5, "google"),
    ("Fatima Khan", "Good work, fixed my windshield quickly.", 4, "facebook"),
    ("Hassan Ali", "Amazing technicians, highly recommend!", 5, "yelp"),
    ("Ayesha Malik", "Quick repair, fair pricing.", 4, "yellow_page"),
    ("Muhammad Karim", "Professional and courteous staff.", 5, "google"),
]

# Sample order data
sample_orders = [
    ("Ali Hassan", "ali@email.com", "0300-1234567", "windshield_replacement", "Lahore", 3500, "completed", "Ahmed"),
    ("Fatima Khan", "fatima@email.com", "0300-2234567", "windshield_repair", "Karachi", 1500, "pending", "Hassan"),
    ("Hassan Ali", "hassan@email.com", "0300-3234567", "windshield_replacement", "Islamabad", 3500, "completed", "Ahmed"),
    ("Ayesha Malik", "ayesha@email.com", "0300-4234567", "windshield_repair", "Lahore", 1500, "in_progress", "Hassan"),
    ("Muhammad Karim", "muhammad@email.com", "0300-5234567", "windshield_replacement", "Rawalpindi", 3500, "pending", "Ahmed"),
]

# Insert reviews
print("\n📝 Inserting reviews...")
insert_review = "INSERT INTO reviews (customer_name, review_text, rating, review_source) VALUES (%s, %s, %s, %s)"

try:
    for review in sample_reviews:
        cursor.execute(insert_review, review)
    connection.commit()
    print(f"   ✅ Inserted {len(sample_reviews)} reviews")
except Error as e:
    print(f"   ⚠️  {e}")
    connection.rollback()

# Insert orders
print("\n📝 Inserting windshield orders...")
insert_order = """
    INSERT INTO windshield_orders
    (customer_name, email, phone, service_type, city, amount, status, technician_name)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

try:
    for order in sample_orders:
        cursor.execute(insert_order, order)
    connection.commit()
    print(f"   ✅ Inserted {len(sample_orders)} orders")
except Error as e:
    print(f"   ⚠️  {e}")
    connection.rollback()

# ==========================================
# 6. QUERY AND DISPLAY DATA
# ==========================================

print("\n" + "=" * 80)
print("6. QUERYING DATA FROM TABLES")
print("=" * 80)

# Get all reviews
print("\n📊 All Reviews:")
print("-" * 80)
try:
    cursor.execute("SELECT id, customer_name, rating, review_source FROM reviews")
    reviews = cursor.fetchall()

    if reviews:
        for review in reviews:
            print(f"  #{review['id']}: {review['customer_name']} - ⭐ {review['rating']}/5 ({review['review_source']})")
    else:
        print("  No reviews found")
except Error as e:
    print(f"  Error: {e}")

# Get all orders
print("\n📊 All Windshield Orders:")
print("-" * 80)
try:
    cursor.execute("SELECT id, customer_name, service_type, city, amount, status FROM windshield_orders")
    orders = cursor.fetchall()

    if orders:
        for order in orders:
            print(f"  #{order['id']}: {order['customer_name']} - {order['service_type']} in {order['city']} - Rs.{order['amount']} ({order['status']})")
    else:
        print("  No orders found")
except Error as e:
    print(f"  Error: {e}")

# Statistics
print("\n📊 Order Statistics:")
print("-" * 80)
try:
    cursor.execute("SELECT COUNT(*) as total, SUM(amount) as revenue, AVG(amount) as avg_amount FROM windshield_orders")
    stats = cursor.fetchone()
    print(f"  Total Orders: {stats['total']}")
    print(f"  Total Revenue: Rs.{stats['revenue']}")
    print(f"  Average Order Value: Rs.{stats['avg_amount']:.0f}")
except Error as e:
    print(f"  Error: {e}")

# ==========================================
# 7. LARAVEL vs PYTHON COMPARISON
# ==========================================

print("\n\n" + "=" * 80)
print("7. LARAVEL vs PYTHON - DATABASE OPERATIONS COMPARISON")
print("=" * 80)

print("""
OPERATION                          | LARAVEL (PHP)                    | PYTHON (MySQL Connector)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Check if table exists             | Schema::hasTable('table_name')  | cursor.execute("SHOW TABLES")
                                  |                                 | cursor.execute("DESCRIBE table_name")

Create table                      | Schema::create('table', ...)    | cursor.execute("CREATE TABLE...")
(Migrations)                      | php artisan make:migration      | connection.commit()

Insert single record              | Order::create(['col' => val])  | cursor.execute("INSERT INTO...")
                                  |                                 | connection.commit()

Insert multiple records           | Order::insert([...])           | for row in data:
                                  |                                 |     cursor.execute("INSERT...", row)
                                  |                                 | connection.commit()

Get all records                   | Order::all()                   | cursor.execute("SELECT * FROM table")
                                  |                                 | results = cursor.fetchall()

Get with condition                | Order::where('status',          | cursor.execute("SELECT * FROM table
                                  | 'completed')->get()             | WHERE status = %s", ('completed',))

Count records                     | Order::count()                 | cursor.execute("SELECT COUNT(*) FROM...")

Update record                     | $order->update([...])          | cursor.execute("UPDATE table SET...")
                                  |                                 | connection.commit()

Delete record                     | $order->delete()               | cursor.execute("DELETE FROM table...")
                                  |                                 | connection.commit()

Error handling                    | try-catch with exceptions      | try-except with mysql.connector.Error

Transactions                      | DB::transaction(function() {}) | connection.begin() ... connection.commit()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

KEY DIFFERENCES:
1. Laravel uses ORM (Eloquent) - more abstracted
2. Python uses direct SQL - more control, more code
3. Laravel migrations vs Python manual DDL
4. Both support transactions and error handling
5. Laravel has built-in validation, Python needs manual checks

PYTHON ADVANTAGES:
✓ Direct SQL control
✓ Works with any database
✓ Better for data science/analysis
✓ Pandas integration

LARAVEL ADVANTAGES:
✓ Less code, more abstraction
✓ Built-in migrations
✓ Eloquent ORM is powerful
✓ Better for web applications
""")


# ==========================================
# 8. CLOSE CONNECTION
# ==========================================

print("\n" + "=" * 80)
print("8. CLOSING CONNECTION")
print("=" * 80)

if cursor:
    cursor.close()
    print("\n✓ Cursor closed")

if connection and connection.is_connected():
    connection.close()
    print("✓ Database connection closed")


# ==========================================
# 9. PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 80)
print("9. PRACTICE EXERCISES - TRY THESE!")
print("=" * 80)

print("""
Exercise 1: Query Pending Orders
  TODO: cursor.execute("SELECT * FROM windshield_orders WHERE status = 'pending'")
  TODO: Print all pending orders
  TODO: Calculate total revenue from pending orders

Exercise 2: Update Order Status
  TODO: cursor.execute("UPDATE windshield_orders SET status = 'completed' WHERE id = 1")
  TODO: connection.commit()
  TODO: Verify the update by selecting the order

Exercise 3: Get Orders by City
  TODO: cursor.execute("SELECT * FROM windshield_orders WHERE city = %s", ('Lahore',))
  TODO: Count total orders per city
  TODO: Calculate average order value per city

Exercise 4: Add New Review
  TODO: Create INSERT statement for new review
  TODO: Add your own review with rating
  TODO: Verify by selecting it back

Exercise 5: Statistics Query
  TODO: Write query to get average rating from reviews
  TODO: Get count of reviews by review_source
  TODO: Find highest rated review

HINTS:
- Always use %s for parameterized queries (prevents SQL injection!)
- Use cursor.fetchall() for multiple rows
- Use cursor.fetchone() for single row
- Don't forget connection.commit() after INSERT/UPDATE/DELETE!
""")

print("\n✅ Day 5 Complete!")
print("Next: Day 6 - Jupyter Notebooks for interactive analysis")
print("\n" + "=" * 70)
print("NEXT STEPS:")
print("=" * 70)
print("""
1. Make sure your MySQL database is running
2. Update .env file with your actual credentials
3. Run this script to test your connection:
   python day5_mysql/mysql_basics.py

4. You should see:
   ✅ Connection established
   📋 Available tables
   📊 Sample queries from your database
""")
