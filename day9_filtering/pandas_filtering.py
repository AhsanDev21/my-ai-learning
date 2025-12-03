# DAY 9: Filtering & Selecting Data
# MOST IMPORTANT: How to get specific rows based on conditions
# This is like SQL WHERE clauses!

print("=" * 70)
print("DAY 9: FILTERING & SELECTING DATA")
print("=" * 70)

import pandas as pd
import csv

# ==========================================
# 1. CREATE SAMPLE DATA
# ==========================================

print("\n1. Creating sample order data...\n")

orders_data = [
    ["order_id", "customer_name", "service_type", "city", "amount", "status", "date"],
    [1, "Ali Hassan", "windshield_replacement", "Lahore", 3500, "completed", "2024-01-15"],
    [2, "Fatima Khan", "windshield_repair", "Karachi", 1500, "pending", "2024-01-20"],
    [3, "Hassan Ali", "windshield_replacement", "Islamabad", 3500, "completed", "2024-01-18"],
    [4, "Ayesha Malik", "windshield_repair", "Lahore", 1500, "in_progress", "2024-01-22"],
    [5, "Muhammad Karim", "windshield_replacement", "Rawalpindi", 3500, "pending", "2024-01-25"],
    [6, "Sara Ahmed", "windshield_replacement", "Karachi", 3500, "completed", "2024-01-19"],
    [7, "Usman Khan", "windshield_repair", "Islamabad", 1500, "completed", "2024-01-21"],
    [8, "Zainab Ali", "windshield_replacement", "Lahore", 3500, "pending", "2024-01-24"],
    [9, "Omar Hassan", "windshield_repair", "Rawalpindi", 1500, "in_progress", "2024-01-23"],
    [10, "Rabia Khan", "windshield_replacement", "Karachi", 3500, "completed", "2024-01-26"],
]

csv_file = "orders.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(orders_data)

df = pd.read_csv(csv_file)
print(f"✓ Loaded {len(df)} orders\n")

# ==========================================
# 2. UNDERSTANDING FILTERING
# ==========================================

print("=" * 70)
print("2. HOW FILTERING WORKS")
print("=" * 70)

print("""
Filtering is like SQL WHERE clauses:

SQL:                                    Pandas:
SELECT * FROM orders                   df
WHERE status = 'completed'             df[df['status'] == 'completed']

WHERE amount > 3000                    df[df['amount'] > 3000]

WHERE city = 'Lahore' AND amount > 2000  df[(df['city'] == 'Lahore') & (df['amount'] > 2000)]

KEY POINTS:
✓ Use == for equality (single =)
✓ Use != for not equal
✓ Use > < >= <= for comparisons
✓ Use & for AND, | for OR
✓ Always use PARENTHESES around conditions!
""")

# ==========================================
# 3. SIMPLE FILTERING - EQUALITY
# ==========================================

print("\n" + "=" * 70)
print("3. SIMPLE FILTERING - EQUALITY")
print("=" * 70)

print("\n📌 Filter: Get all COMPLETED orders")
print("-" * 70)
completed = df[df['status'] == 'completed']
print(f"Found {len(completed)} completed orders:")
print(completed[['order_id', 'customer_name', 'status']])

print("\n📌 Filter: Get all orders from LAHORE")
print("-" * 70)
lahore = df[df['city'] == 'Lahore']
print(f"Found {len(lahore)} orders from Lahore:")
print(lahore[['order_id', 'customer_name', 'city']])

print("\n📌 Filter: Get all WINDSHIELD_REPLACEMENT orders")
print("-" * 70)
replacements = df[df['service_type'] == 'windshield_replacement']
print(f"Found {len(replacements)} replacement orders:")
print(replacements[['order_id', 'customer_name', 'service_type']])

# ==========================================
# 4. FILTERING - COMPARISON OPERATORS
# ==========================================

print("\n\n" + "=" * 70)
print("4. FILTERING - COMPARISON OPERATORS")
print("=" * 70)

print("\n💰 Filter: Get orders with amount > 3000")
print("-" * 70)
high_value = df[df['amount'] > 3000]
print(f"Found {len(high_value)} high-value orders:")
print(high_value[['customer_name', 'amount']])

print("\n💰 Filter: Get orders with amount <= 1500")
print("-" * 70)
low_value = df[df['amount'] <= 1500]
print(f"Found {len(low_value)} orders <= Rs.1500:")
print(low_value[['customer_name', 'amount']])

print("\n📊 Filter: Get orders with amount == 3500")
print("-" * 70)
exact = df[df['amount'] == 3500]
print(f"Found {len(exact)} orders for exactly Rs.3500:")
print(f"Count: {len(exact)}")

# ==========================================
# 5. FILTERING - NOT EQUAL
# ==========================================

print("\n\n" + "=" * 70)
print("5. FILTERING - NOT EQUAL (!= operator)")
print("=" * 70)

print("\n📌 Filter: Get all orders that are NOT 'pending'")
print("-" * 70)
not_pending = df[df['status'] != 'pending']
print(f"Found {len(not_pending)} non-pending orders:")
print(not_pending[['customer_name', 'status']])

print("\n🏙️  Filter: Get all orders NOT from 'Lahore'")
print("-" * 70)
not_lahore = df[df['city'] != 'Lahore']
print(f"Found {len(not_lahore)} orders from other cities:")
print(not_lahore[['customer_name', 'city']])

# ==========================================
# 6. FILTERING - MULTIPLE CONDITIONS (AND)
# ==========================================

print("\n\n" + "=" * 70)
print("6. MULTIPLE CONDITIONS - AND (&)")
print("=" * 70)

print("\n📌 Filter: Completed orders in Lahore")
print("-" * 70)
condition = (df['status'] == 'completed') & (df['city'] == 'Lahore')
result = df[condition]
print(f"Found {len(result)} completed orders in Lahore:")
print(result[['customer_name', 'city', 'status']])

print("\n📌 Filter: High-value orders (>3000) that are completed")
print("-" * 70)
condition = (df['amount'] > 3000) & (df['status'] == 'completed')
result = df[condition]
print(f"Found {len(result)} high-value completed orders:")
print(result[['customer_name', 'amount', 'status']])

print("\n📌 Filter: Replacement orders (>3000) from Karachi or Lahore")
print("-" * 70)
condition = (df['service_type'] == 'windshield_replacement') & (df['amount'] > 2000) & ((df['city'] == 'Karachi') | (df['city'] == 'Lahore'))
result = df[condition]
print(f"Found {len(result)} orders:")
print(result[['customer_name', 'city', 'amount']])

# ==========================================
# 7. FILTERING - MULTIPLE CONDITIONS (OR)
# ==========================================

print("\n\n" + "=" * 70)
print("7. MULTIPLE CONDITIONS - OR (|)")
print("=" * 70)

print("\n📌 Filter: Orders from Lahore OR Karachi")
print("-" * 70)
condition = (df['city'] == 'Lahore') | (df['city'] == 'Karachi')
result = df[condition]
print(f"Found {len(result)} orders from Lahore or Karachi:")
print(result[['customer_name', 'city']])

print("\n📌 Filter: Orders that are pending OR in_progress")
print("-" * 70)
condition = (df['status'] == 'pending') | (df['status'] == 'in_progress')
result = df[condition]
print(f"Found {len(result)} orders pending or in progress:")
print(result[['customer_name', 'status']])

# ==========================================
# 8. FILTERING - USING .isin()
# ==========================================

print("\n\n" + "=" * 70)
print("8. FILTERING - USING .isin() FOR MULTIPLE VALUES")
print("=" * 70)

print("\n🏙️  Filter: Orders from specific cities (using list)")
print("-" * 70)
cities_list = ['Lahore', 'Karachi']
result = df[df['city'].isin(cities_list)]
print(f"Found {len(result)} orders from {cities_list}:")
print(result[['customer_name', 'city']])

print("\n📌 Filter: Orders with specific statuses")
print("-" * 70)
statuses = ['completed', 'in_progress']
result = df[df['status'].isin(statuses)]
print(f"Found {len(result)} orders with statuses {statuses}:")
print(result[['customer_name', 'status']])

# ==========================================
# 9. FILTERING - USING .str FOR TEXT MATCHING
# ==========================================

print("\n\n" + "=" * 70)
print("9. FILTERING - TEXT MATCHING (.str methods)")
print("=" * 70)

print("\n📝 Filter: Customer names containing 'Ali'")
print("-" * 70)
result = df[df['customer_name'].str.contains('Ali', case=False)]
print(f"Found {len(result)} customers with 'Ali':")
print(result[['customer_name']])

print("\n📝 Filter: Service types containing 'replacement'")
print("-" * 70)
result = df[df['service_type'].str.contains('replacement')]
print(f"Found {len(result)} replacement orders:")
print(result[['customer_name', 'service_type']])

# ==========================================
# 10. SELECTING SPECIFIC COLUMNS
# ==========================================

print("\n\n" + "=" * 70)
print("10. SELECTING SPECIFIC COLUMNS")
print("=" * 70)

print("\n📋 Select only customer_name and amount:")
subset = df[['customer_name', 'amount']]
print(subset.head())

print("\n📋 Select columns AND filter:")
result = df[(df['status'] == 'completed')][['customer_name', 'amount', 'status']]
print(f"\nCompleted orders (name, amount, status):")
print(result)

# ==========================================
# 11. FILTERING WITH .loc AND .iloc
# ==========================================

print("\n\n" + "=" * 70)
print("11. FILTERING WITH .loc AND .iloc")
print("=" * 70)

print("\n.iloc - Get by position (0-based index):")
print(f"  First row: {df.iloc[0]['customer_name']}")
print(f"  5th row: {df.iloc[4]['customer_name']}")

print("\n.loc - Get by label/condition:")
result = df.loc[df['status'] == 'completed']
print(f"  Completed orders: {len(result)} found")

# ==========================================
# 12. PRACTICAL EXAMPLES
# ==========================================

print("\n\n" + "=" * 70)
print("12. PRACTICAL BUSINESS EXAMPLES")
print("=" * 70)

print("\n💡 Example 1: Find pending orders that need follow-up")
pending = df[df['status'] == 'pending']
print(f"   {len(pending)} pending orders:")
print(pending[['customer_name', 'city', 'date']])

print("\n💡 Example 2: Find your top customers (high-value orders)")
top_orders = df[df['amount'] == df['amount'].max()]
print(f"   Top order value: Rs.{df['amount'].max()}")
print(top_orders[['customer_name', 'amount']])

print("\n💡 Example 3: Find repair jobs (quick revenue)")
repairs = df[df['service_type'] == 'windshield_repair']
print(f"   {len(repairs)} repair orders, total: Rs.{repairs['amount'].sum()}")

print("\n💡 Example 4: City performance - which city has most orders")
city_counts = df['city'].value_counts()
top_city = city_counts.idxmax()
print(f"   Best city: {top_city} with {city_counts[top_city]} orders")

# ==========================================
# LARAVEL vs PANDAS - WHERE CLAUSES
# ==========================================

print("\n\n" + "=" * 70)
print("🔄 LARAVEL WHERE vs PANDAS FILTERING")
print("=" * 70)

print("""
FILTER TASK                        | LARAVEL (PHP/Eloquent)         | PANDAS (Python)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHERE status = 'completed'         | Order::where('status',         | df[df['status'] == 'completed']
                                  | 'completed')->get()            |

WHERE amount > 3000                | Order::where('amount', '>'    | df[df['amount'] > 3000]
                                  | 3000)->get()                   |

WHERE amount >= 3000               | Order::where('amount', '>='   | df[df['amount'] >= 3000]
                                  | 3000)->get()                   |

WHERE status != 'pending'          | Order::where('status', '!='   | df[df['status'] != 'pending']
                                  | 'pending')->get()              |

WHERE status IN ('pending', 'new') | Order::whereIn('status',       | df[df['status'].isin(['pending','new'])]
                                  | ['pending', 'new'])->get()     |

WHERE NOT IN                       | Order::whereNotIn('status',   | df[~df['status'].isin(['pending'])]
                                  | ['pending'])->get()            |

WHERE col LIKE '%text%'            | Order::where('name', 'like',  | df[df['name'].str.contains('text')]
                                  | '%text%')->get()               |

WHERE city = 'Lahore' AND          | Order::where('city', 'Lahore')| df[(df['city']=='Lahore') &
      amount > 3000                |     ->where('amount', '>', 3k) |  (df['amount']>3000)]
                                  |     ->get()                    |

WHERE status='done' OR city='NYC'  | Order::where('status', 'done')| df[(df['status']=='done') |
                                  |     ->orWhere('city', 'NYC')   |  (df['city']=='NYC')]
                                  |     ->get()                    |

Get first matching record           | Order::where(...)->first()     | df[df['status']=='completed'].iloc[0]

Count matching records             | Order::where(...)->count()     | len(df[df['status']=='completed'])

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PANDAS FILTERING RULES (IMPORTANT!):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Use () around each condition:    (df['col'] == value)
2. Use & for AND (not 'and'):       (df['a']==1) & (df['b']==2)
3. Use | for OR (not 'or'):         (df['a']==1) | (df['b']==2)
4. Use ~ for NOT:                   ~(df['status']=='pending')
5. Use == for equals (not =):       df['status'] == 'value'

EXAMPLE COMPARISONS:
Laravel:  Order::where('status', 'completed')
Pandas:   df[df['status'] == 'completed']

Laravel:  Order::where('city', 'Lahore')->where('amount', '>', 3000)
Pandas:   df[(df['city']=='Lahore') & (df['amount']>3000)]

Laravel:  Order::whereIn('status', ['pending', 'completed'])
Pandas:   df[df['status'].isin(['pending', 'completed'])]

SPEED COMPARISON:
✓ Pandas is 10-100x faster on large datasets
✓ Laravel better for real-time web queries
✓ For analysis: Always use Pandas
""")

# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Using the 'df' DataFrame, practice these filters:

Exercise 1: Basic Filtering
  TODO: Get all pending orders
  TODO: Get all orders from Islamabad
  TODO: Get all repair orders (windshield_repair)

Exercise 2: Comparison Filtering
  TODO: Get orders with amount >= 3500
  TODO: Get orders with amount < 2000
  TODO: Get orders NOT from Lahore

Exercise 3: Multiple Conditions
  TODO: Get completed orders from Karachi
  TODO: Get pending or in_progress orders
  TODO: Get all orders from Lahore AND Rawalpindi

Exercise 4: Complex Filtering
  TODO: Get high-value (>3000) completed orders
  TODO: Get pending orders with amount < 2000
  TODO: Get replacement orders from any city except Lahore

Exercise 5: Column Selection
  TODO: Get only customer names and amounts for completed orders
  TODO: Get only city and status for orders > 2500

HINTS:
- Use == for equals, != for not equal
- Use > < >= <= for comparison
- Use & for AND, | for OR (with parentheses!)
- Use .isin([list]) for multiple values
- Use .str.contains() for text matching
- Always parenthesize conditions!
""")

print("\n✅ Day 9 Complete!")
print("🎯 Filtering is THE MOST IMPORTANT skill for data analysis!")
print("\nNext: Day 10 - GroupBy & Aggregations (sum, count, average)")
