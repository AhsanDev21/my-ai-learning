# DAY 7: Mini Project - Order Performance Analysis
# 🎯 Complete project: Load → Analyze → Report
# Uses: File handling, data structures, loops, functions

print("=" * 70)
print("DAY 7: MINI PROJECT - WindshieldHub Order Performance Report")
print("=" * 70)

import csv
from datetime import datetime

# ==========================================
# PART 1: CREATE SAMPLE DATA
# ==========================================

print("\n📝 STEP 1: Creating sample order data...\n")

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

# Write to CSV
csv_file = "orders_data.csv"
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(orders_data)

print(f"✓ Created {csv_file} with {len(orders_data)-1} orders\n")

# ==========================================
# PART 2: LOAD AND ANALYZE DATA
# ==========================================

print("📊 STEP 2: Loading and analyzing orders...\n")

# Read CSV into list of dictionaries
orders = []
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert amount to integer for calculations
        row['amount'] = int(row['amount'])
        orders.append(row)

print(f"✓ Loaded {len(orders)} orders\n")

# ==========================================
# CALCULATE METRICS
# ==========================================

print("📈 STEP 3: Calculating performance metrics...\n")

# 1. Total Revenue
total_revenue = sum(order['amount'] for order in orders)
print(f"💰 Total Revenue: Rs.{total_revenue:,}")

# 2. Orders by Status
status_counts = {}
for order in orders:
    status = order['status']
    if status not in status_counts:
        status_counts[status] = {'count': 0, 'revenue': 0}
    status_counts[status]['count'] += 1
    status_counts[status]['revenue'] += order['amount']

print(f"\n📌 Orders by Status:")
for status in sorted(status_counts.keys()):
    count = status_counts[status]['count']
    revenue = status_counts[status]['revenue']
    percentage = (count / len(orders)) * 100
    print(f"   {status}: {count} orders ({percentage:.1f}%) - Rs.{revenue:,}")

# 3. Revenue by City
city_stats = {}
for order in orders:
    city = order['city']
    if city not in city_stats:
        city_stats[city] = {'count': 0, 'revenue': 0}
    city_stats[city]['count'] += 1
    city_stats[city]['revenue'] += order['amount']

print(f"\n🏙️  Revenue by City:")
for city in sorted(city_stats.keys(), key=lambda x: city_stats[x]['revenue'], reverse=True):
    count = city_stats[city]['count']
    revenue = city_stats[city]['revenue']
    avg = revenue // count
    print(f"   {city}: {count} orders - Rs.{revenue:,} (avg: Rs.{avg})")

# 4. Performance by Technician
tech_stats = {}
for order in orders:
    tech = order['technician']
    if tech not in tech_stats:
        tech_stats[tech] = {'completed': 0, 'pending': 0, 'in_progress': 0, 'revenue': 0}
    tech_stats[tech][order['status']] += 1
    tech_stats[tech]['revenue'] += order['amount']

print(f"\n👨‍🔧 Technician Performance:")
for tech in sorted(tech_stats.keys()):
    stats = tech_stats[tech]
    total_orders = stats['completed'] + stats['pending'] + stats['in_progress']
    completion_rate = (stats['completed'] / total_orders * 100) if total_orders > 0 else 0
    print(f"   {tech}:")
    print(f"      Total orders: {total_orders}")
    print(f"      Completed: {stats['completed']}")
    print(f"      Pending: {stats['pending']}")
    print(f"      In Progress: {stats['in_progress']}")
    print(f"      Completion Rate: {completion_rate:.0f}%")
    print(f"      Revenue: Rs.{stats['revenue']:,}")

# 5. Service Type Performance
service_stats = {}
for order in orders:
    service = order['service_type']
    if service not in service_stats:
        service_stats[service] = {'count': 0, 'revenue': 0}
    service_stats[service]['count'] += 1
    service_stats[service]['revenue'] += order['amount']

print(f"\n🔧 Service Type Performance:")
for service in sorted(service_stats.keys()):
    count = service_stats[service]['count']
    revenue = service_stats[service]['revenue']
    avg = revenue // count
    print(f"   {service}: {count} orders - Rs.{revenue:,} (avg: Rs.{avg})")

# ==========================================
# GENERATE REPORT
# ==========================================

print("\n\n📄 STEP 4: Generating performance report...\n")

report_content = []
report_content.append("=" * 70)
report_content.append("WINDSHIELDHUB ORDER PERFORMANCE REPORT")
report_content.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report_content.append("=" * 70)
report_content.append("")

report_content.append("EXECUTIVE SUMMARY")
report_content.append("-" * 70)
report_content.append(f"Total Orders: {len(orders)}")
report_content.append(f"Total Revenue: Rs.{total_revenue:,}")
report_content.append(f"Average Order Value: Rs.{total_revenue // len(orders):,}")
report_content.append("")

report_content.append("ORDER STATUS BREAKDOWN")
report_content.append("-" * 70)
for status in sorted(status_counts.keys()):
    count = status_counts[status]['count']
    revenue = status_counts[status]['revenue']
    percentage = (count / len(orders)) * 100
    report_content.append(f"{status.upper()}: {count} orders ({percentage:.1f}%) - Rs.{revenue:,}")
report_content.append("")

report_content.append("REVENUE BY CITY")
report_content.append("-" * 70)
for city in sorted(city_stats.keys(), key=lambda x: city_stats[x]['revenue'], reverse=True):
    count = city_stats[city]['count']
    revenue = city_stats[city]['revenue']
    avg = revenue // count
    report_content.append(f"{city}: {count} orders - Rs.{revenue:,} (avg: Rs.{avg})")
report_content.append("")

report_content.append("TECHNICIAN PERFORMANCE")
report_content.append("-" * 70)
for tech in sorted(tech_stats.keys()):
    stats = tech_stats[tech]
    total_orders = stats['completed'] + stats['pending'] + stats['in_progress']
    completion_rate = (stats['completed'] / total_orders * 100) if total_orders > 0 else 0
    report_content.append(f"{tech}:")
    report_content.append(f"  Total Orders: {total_orders}")
    report_content.append(f"  Completed: {stats['completed']} ({completion_rate:.0f}%)")
    report_content.append(f"  Pending: {stats['pending']}")
    report_content.append(f"  In Progress: {stats['in_progress']}")
    report_content.append(f"  Revenue Generated: Rs.{stats['revenue']:,}")
report_content.append("")

report_content.append("SERVICE TYPE ANALYSIS")
report_content.append("-" * 70)
for service in sorted(service_stats.keys()):
    count = service_stats[service]['count']
    revenue = service_stats[service]['revenue']
    avg = revenue // count
    percentage = (count / len(orders)) * 100
    report_content.append(f"{service}: {count} orders ({percentage:.0f}%) - Rs.{revenue:,} (avg: Rs.{avg})")
report_content.append("")

report_content.append("INSIGHTS & RECOMMENDATIONS")
report_content.append("-" * 70)

# Find top performing city
top_city = max(city_stats.keys(), key=lambda x: city_stats[x]['revenue'])
report_content.append(f"✓ Best performing city: {top_city} with Rs.{city_stats[top_city]['revenue']:,}")

# Find top technician
top_tech = max(tech_stats.keys(), key=lambda x: tech_stats[x]['revenue'])
report_content.append(f"✓ Top technician: {top_tech} with Rs.{tech_stats[top_tech]['revenue']:,}")

# Pending orders
pending_count = status_counts.get('pending', {}).get('count', 0)
report_content.append(f"⚠️  Pending orders requiring follow-up: {pending_count}")

report_content.append("")
report_content.append("=" * 70)
report_content.append("END OF REPORT")
report_content.append("=" * 70)

# ==========================================
# SAVE REPORT TO FILE
# ==========================================

report_file = "performance_report.txt"
with open(report_file, 'w') as file:
    file.write("\n".join(report_content))

print(f"✓ Report saved to {report_file}\n")

# ==========================================
# DISPLAY REPORT
# ==========================================

print("\n" + "\n".join(report_content))

# ==========================================
# SAVE FILTERED DATA
# ==========================================

print("\n\n📊 STEP 5: Saving filtered results...\n")

# Save only completed orders
completed_orders = [order for order in orders if order['status'] == 'completed']

completed_file = "completed_orders_report.csv"
if completed_orders:
    with open(completed_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=completed_orders[0].keys())
        writer.writeheader()
        writer.writerows(completed_orders)
    print(f"✓ Saved {len(completed_orders)} completed orders to {completed_file}")

# Save pending orders
pending_orders = [order for order in orders if order['status'] == 'pending']

pending_file = "pending_orders_followup.csv"
if pending_orders:
    with open(pending_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=pending_orders[0].keys())
        writer.writeheader()
        writer.writerows(pending_orders)
    print(f"✓ Saved {len(pending_orders)} pending orders to {pending_file}")

# ==========================================
# SUMMARY
# ==========================================

print("\n\n" + "=" * 70)
print("✅ PROJECT COMPLETE!")
print("=" * 70)

print(f"""
Summary of what we did:
1. ✓ Created sample CSV file with {len(orders)} orders
2. ✓ Loaded data from CSV into Python
3. ✓ Calculated key metrics:
   - Total revenue: Rs.{total_revenue:,}
   - Orders by status
   - Revenue by city
   - Technician performance
   - Service type analysis
4. ✓ Generated performance report saved to {report_file}
5. ✓ Created filtered CSV files:
   - {completed_file} ({len(completed_orders)} orders)
   - {pending_file} ({len(pending_orders)} orders)

This is exactly what you'll do in real data analysis!

Next: Week 2 - Pandas (the most important data science library)
""")
