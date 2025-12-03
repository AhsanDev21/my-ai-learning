# DAY 10: GroupBy & Aggregations
# How to group data and calculate totals, averages, counts, etc.
# Like SQL GROUP BY!

print("=" * 70)
print("DAY 10: GROUPBY & AGGREGATIONS")
print("=" * 70)

import pandas as pd
import csv

# ==========================================
# 1. CREATE SAMPLE DATA
# ==========================================

print("\n1. Creating sample order data...\n")

orders_data = [
    ["order_id", "customer_name", "service_type", "city", "amount", "status", "date", "technician"],
    [1, "Ali Hassan", "windshield_replacement", "Lahore", 3500, "completed", "2024-01-15", "Ahmed"],
    [2, "Fatima Khan", "windshield_repair", "Karachi", 1500, "pending", "2024-01-20", "Hassan"],
    [3, "Hassan Ali", "windshield_replacement", "Islamabad", 3500, "completed", "2024-01-18", "Ahmed"],
    [4, "Ayesha Malik", "windshield_repair", "Lahore", 1500, "in_progress", "2024-01-22", "Hassan"],
    [5, "Muhammad Karim", "windshield_replacement", "Rawalpindi", 3500, "pending", "2024-01-25", "Ahmed"],
    [6, "Sara Ahmed", "windshield_replacement", "Karachi", 3500, "completed", "2024-01-19", "Hassan"],
    [7, "Usman Khan", "windshield_repair", "Islamabad", 1500, "completed", "2024-01-21", "Hassan"],
    [8, "Zainab Ali", "windshield_replacement", "Lahore", 3500, "pending", "2024-01-24", "Ahmed"],
    [9, "Omar Hassan", "windshield_repair", "Rawalpindi", 1500, "in_progress", "2024-01-23", "Hassan"],
    [10, "Rabia Khan", "windshield_replacement", "Karachi", 3500, "completed", "2024-01-26", "Ahmed"],
]

csv_file = "orders.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(orders_data)

df = pd.read_csv(csv_file)
print(f"✓ Loaded {len(df)} orders\n")
print("Sample data:")
print(df.head(3))

# ==========================================
# 2. UNDERSTANDING GROUPBY
# ==========================================

print("\n\n" + "=" * 70)
print("2. WHAT IS GROUPBY?")
print("=" * 70)

print("""
GroupBy is like SQL GROUP BY:
- Groups rows by a column value
- Then applies aggregation (sum, count, average, etc.)

Example SQL:
  SELECT city, COUNT(*) as count, SUM(amount) as total
  FROM orders
  GROUP BY city

Pandas:
  df.groupby('city')['amount'].sum()
  df.groupby('city').size()
  df.groupby('city')['amount'].agg(['sum', 'count', 'mean'])
""")

# ==========================================
# 3. GROUP BY SINGLE COLUMN
# ==========================================

print("\n" + "=" * 70)
print("3. GROUP BY SINGLE COLUMN")
print("=" * 70)

print("\n📊 Count of orders by status:")
print("-" * 70)
status_counts = df['status'].value_counts()
print(status_counts)

print("\n📊 Revenue by city:")
print("-" * 70)
city_revenue = df.groupby('city')['amount'].sum().sort_values(ascending=False)
print(city_revenue)

print("\n📊 Count of orders by city:")
print("-" * 70)
city_counts = df.groupby('city').size()
print(city_counts)

print("\n📊 Count of orders by service type:")
print("-" * 70)
service_counts = df.groupby('service_type').size()
print(service_counts)

# ==========================================
# 4. MULTIPLE AGGREGATION FUNCTIONS
# ==========================================

print("\n\n" + "=" * 70)
print("4. MULTIPLE AGGREGATIONS ON ONE COLUMN")
print("=" * 70)

print("\n💰 City statistics (count, sum, mean, min, max):")
print("-" * 70)
city_stats = df.groupby('city')['amount'].agg(['count', 'sum', 'mean', 'min', 'max'])
print(city_stats)

print("\n💰 Service type statistics:")
print("-" * 70)
service_stats = df.groupby('service_type')['amount'].agg(['count', 'sum', 'mean'])
print(service_stats)

print("\n💰 Status statistics:")
print("-" * 70)
status_stats = df.groupby('status')['amount'].agg(['count', 'sum', 'mean'])
print(status_stats)

# ==========================================
# 5. GROUP BY MULTIPLE COLUMNS
# ==========================================

print("\n\n" + "=" * 70)
print("5. GROUP BY MULTIPLE COLUMNS")
print("=" * 70)

print("\n📊 Revenue by city and status:")
print("-" * 70)
city_status = df.groupby(['city', 'status'])['amount'].sum().sort_values(ascending=False)
print(city_status)

print("\n📊 Count by service type and status:")
print("-" * 70)
service_status = df.groupby(['service_type', 'status']).size()
print(service_status)

print("\n📊 Average amount by city and service type:")
print("-" * 70)
city_service = df.groupby(['city', 'service_type'])['amount'].mean()
print(city_service)

# ==========================================
# 6. TECHNICIAN PERFORMANCE
# ==========================================

print("\n\n" + "=" * 70)
print("6. REAL-WORLD EXAMPLE: TECHNICIAN PERFORMANCE")
print("=" * 70)

print("\n👨‍🔧 Total orders and revenue by technician:")
print("-" * 70)
tech_stats = df.groupby('technician')['amount'].agg(['count', 'sum', 'mean'])
tech_stats.columns = ['Total Orders', 'Total Revenue', 'Average Order']
print(tech_stats)

print("\n👨‍🔧 Technician performance by status:")
print("-" * 70)
tech_status = df.groupby(['technician', 'status']).size().unstack(fill_value=0)
print(tech_status)

print("\n👨‍🔧 Calculate completion rate by technician:")
print("-" * 70)
completed = df[df['status'] == 'completed'].groupby('technician').size()
total = df.groupby('technician').size()
completion_rate = (completed / total * 100).fillna(0)
print("Completion Rate (%):")
print(completion_rate)

# ==========================================
# 7. COMMON AGGREGATION FUNCTIONS
# ==========================================

print("\n\n" + "=" * 70)
print("7. COMMON AGGREGATION FUNCTIONS")
print("=" * 70)

print("""
.sum()       - Total
.count()     - Count of non-null values
.size()      - Count including null values
.mean()      - Average
.median()    - Middle value
.min()       - Minimum
.max()       - Maximum
.std()       - Standard deviation
.var()       - Variance
.first()     - First value
.last()      - Last value
""")

print("\n📊 Example: Using different aggregation functions on amount column:")
print("-" * 70)
city_agg = df.groupby('city')['amount'].agg({
    'Count': 'count',
    'Total': 'sum',
    'Average': 'mean',
    'Min': 'min',
    'Max': 'max',
})
print(city_agg)

# ==========================================
# 8. FILTERING GROUPED DATA
# ==========================================

print("\n\n" + "=" * 70)
print("8. FILTERING GROUPED DATA")
print("=" * 70)

print("\n📊 Find cities with more than 2 orders:")
print("-" * 70)
city_counts = df.groupby('city').size()
cities_with_many = city_counts[city_counts > 2]
print(cities_with_many)

print("\n💰 Find cities with total revenue > 7000:")
print("-" * 70)
city_revenue = df.groupby('city')['amount'].sum()
high_revenue_cities = city_revenue[city_revenue > 7000]
print(high_revenue_cities)

# ==========================================
# 9. SORTING GROUPED RESULTS
# ==========================================

print("\n\n" + "=" * 70)
print("9. SORTING GROUPED RESULTS")
print("=" * 70)

print("\n💰 Cities sorted by total revenue (highest first):")
print("-" * 70)
city_revenue = df.groupby('city')['amount'].sum().sort_values(ascending=False)
print(city_revenue)

print("\n📊 Statuses sorted by order count (highest first):")
print("-" * 70)
status_counts = df['status'].value_counts().sort_values(ascending=False)
print(status_counts)

print("\n📊 Service types sorted by average amount (highest first):")
print("-" * 70)
service_avg = df.groupby('service_type')['amount'].mean().sort_values(ascending=False)
print(service_avg)

# ==========================================
# 10. ADVANCED: CUSTOM AGGREGATIONS
# ==========================================

print("\n\n" + "=" * 70)
print("10. CUSTOM AGGREGATIONS WITH LAMBDA")
print("=" * 70)

print("\n🔢 Calculate range (max - min) by city:")
print("-" * 70)
city_range = df.groupby('city')['amount'].agg(lambda x: x.max() - x.min())
print(city_range)

print("\n📊 Count of high-value (>3000) orders by city:")
print("-" * 70)
high_value_counts = df.groupby('city')['amount'].agg(lambda x: (x > 3000).sum())
print(high_value_counts)

# ==========================================
# 11. PRACTICAL BUSINESS EXAMPLES
# ==========================================

print("\n\n" + "=" * 70)
print("11. PRACTICAL BUSINESS EXAMPLES")
print("=" * 70)

print("\n💡 Example 1: Monthly revenue report")
print("-" * 70)
# Note: We don't have date column grouped, so using status as example
status_revenue = df.groupby('status')['amount'].sum().sort_values(ascending=False)
print("Revenue by Status:")
for status, revenue in status_revenue.items():
    print(f"   {status}: Rs.{revenue:,}")

print("\n💡 Example 2: Which service type is most profitable?")
print("-" * 70)
service_profit = df.groupby('service_type')['amount'].sum()
best_service = service_profit.idxmax()
print(f"   Best service: {best_service} - Rs.{service_profit[best_service]:,}")

print("\n💡 Example 3: Best performing technician")
print("-" * 70)
tech_revenue = df.groupby('technician')['amount'].sum()
best_tech = tech_revenue.idxmax()
print(f"   Best technician: {best_tech} - Rs.{tech_revenue[best_tech]:,}")

print("\n💡 Example 4: City ranking by total orders")
print("-" * 70)
city_counts = df.groupby('city').size().sort_values(ascending=False)
for rank, (city, count) in enumerate(city_counts.items(), 1):
    print(f"   {rank}. {city}: {count} orders")

# ==========================================
# LARAVEL vs PANDAS - GROUP BY & AGGREGATIONS
# ==========================================

print("\n\n" + "=" * 70)
print("🔄 LARAVEL GROUP BY vs PANDAS GROUPBY")
print("=" * 70)

print("""
AGGREGATION TASK                   | LARAVEL (PHP/Eloquent)           | PANDAS (Python)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Count by group                     | Order::selectRaw('city, count(*)  | df.groupby('city').size()
                                  | as count')->groupBy('city')      | df['city'].value_counts()

Sum by group                       | Order::selectRaw('city,           | df.groupby('city')['amount'].sum()
                                  | sum(amount) as total')            |
                                  | ->groupBy('city')->get()          |

Average by group                  | Order::selectRaw('city,           | df.groupby('city')['amount'].mean()
                                  | avg(amount) as avg_amount')       | df.groupby('city')['amount'].agg('mean')
                                  | ->groupBy('city')->get()          |

Min/Max by group                  | Order::selectRaw('city,           | df.groupby('city')['amount'].min()
                                  | min(amount), max(amount)')        | df.groupby('city')['amount'].max()
                                  | ->groupBy('city')->get()          |

Multiple aggregations              | Order::selectRaw('city,           | df.groupby('city')['amount'].agg(['sum',
                                  | count(*) as cnt,                  | 'count', 'mean', 'min', 'max'])
                                  | sum(amount), avg(amount), ...') |

Group by multiple columns         | Order::groupBy('city', 'status')  | df.groupby(['city', 'status']).size()
                                  | ->selectRaw('count(*) as cnt')    |

Get max per group (top N)         | Order::where('amount',            | df.groupby('city')['amount']
                                  | Order::selectRaw('max(amount)')   | .nlargest(1)
                                  | ->groupBy('city'))->get()         |

Sort group results                | Order::groupBy('city')            | df.groupby('city')['amount'].sum()
                                  | ->selectRaw('sum(amount)')        | .sort_values(ascending=False)
                                  | ->orderByDesc('sum')              |

Count nulls per group             | Order::selectRaw('city,           | df.groupby('city')['col_name']
                                  | count(col) as cnt')               | .apply(lambda x: x.isnull().sum())

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PANDAS GROUPBY SYNTAX CHEAT SHEET:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Single group, single metric
df.groupby('city')['amount'].sum()

# Single group, multiple metrics
df.groupby('city')['amount'].agg(['sum', 'count', 'mean', 'min', 'max'])

# Multiple groups
df.groupby(['city', 'status']).size()

# Named aggregations (cleaner)
df.groupby('city')['amount'].agg(
    total='sum',
    count='count',
    average='mean'
)

# Custom aggregation
df.groupby('city')['amount'].agg(lambda x: x.max() - x.min())

# Get top value per group
df.groupby('city').apply(lambda x: x.nlargest(1, 'amount'))

REAL EXAMPLES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Laravel:  DB::table('orders')
            ->select(DB::raw('city, count(*), sum(amount)'))
            ->groupBy('city')
            ->orderByDesc(DB::raw('sum(amount)'))
            ->get()

Pandas:   df.groupby('city')['amount'].agg(['count', 'sum'])
            .sort_values('sum', ascending=False)

PERFORMANCE NOTES:
✓ Pandas groupby: 50-500x faster than Laravel
✓ Great for millions of rows
✓ In-memory processing (faster but needs RAM)
✓ Laravel better for streaming large datasets
""")

# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Using the 'df' DataFrame, practice these groupby operations:

Exercise 1: Basic GroupBy
  TODO: Count orders by city
  TODO: Sum revenue by status
  TODO: Count orders by service_type

Exercise 2: Multiple Aggregations
  TODO: Get count, sum, and mean for each city
  TODO: Get count, sum, and mean for each service type
  TODO: Get max and min amount for each status

Exercise 3: Multiple Columns
  TODO: Group by city and status, show total revenue
  TODO: Group by technician and status, show count
  TODO: Group by city and service_type, show count

Exercise 4: Sorting
  TODO: Cities ranked by total revenue (highest first)
  TODO: Statuses ranked by number of orders (highest first)
  TODO: Service types ranked by average amount (highest first)

Exercise 5: Business Questions
  TODO: Which city has the most revenue?
  TODO: Which technician has completed the most orders?
  TODO: What's the average order value?

HINTS:
- df.groupby('column')['amount'].sum() - total by column
- df.groupby('column').size() - count by column
- df.groupby('column')['amount'].mean() - average by column
- .sort_values(ascending=False) - highest first
- df.groupby(['col1','col2']) - group by multiple columns
- .agg(['sum','count','mean']) - multiple aggregations
""")

print("\n✅ Day 10 Complete!")
print("🎯 GroupBy & aggregations are CRITICAL for business analytics!")
print("\nNext: Day 11 - Data Cleaning (handling missing data, invalid values)")
