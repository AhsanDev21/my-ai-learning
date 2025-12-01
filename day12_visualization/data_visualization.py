# DAY 12: Data Visualization
# Create charts and graphs to visualize your data
# A picture is worth a thousand numbers!

print("=" * 70)
print("DAY 12: DATA VISUALIZATION WITH MATPLOTLIB")
print("=" * 70)

import pandas as pd
import matplotlib.pyplot as plt
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
# 2. MATPLOTLIB BASICS
# ==========================================

print("=" * 70)
print("2. MATPLOTLIB BASICS")
print("=" * 70)

print("""
Matplotlib is the most popular visualization library for Python.

Key concepts:
- Figure: The entire image/window
- Axes: The plot area where data is drawn
- plt.show(): Display the plot

Common chart types:
✓ Bar Chart      - Compare categories
✓ Line Chart     - Show trends over time
✓ Pie Chart      - Show proportions
✓ Histogram      - Show distribution
✓ Scatter Plot   - Show relationships

Installation: pip install matplotlib
""")

# ==========================================
# 3. BAR CHART - ORDERS BY CITY
# ==========================================

print("\n\n" + "=" * 70)
print("3. BAR CHART - ORDERS BY CITY")
print("=" * 70)

print("\n📊 Creating bar chart...\n")

# Prepare data
city_counts = df['city'].value_counts().sort_values(ascending=False)

# Create figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart
ax.bar(city_counts.index, city_counts.values, color='steelblue', edgecolor='black')

# Customize
ax.set_title('Number of Orders by City', fontsize=14, fontweight='bold')
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Number of Orders', fontsize=12)
ax.grid(axis='y', alpha=0.3)

# Add value labels on bars
for i, (city, count) in enumerate(city_counts.items()):
    ax.text(i, count + 0.1, str(count), ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('01_orders_by_city.png')
print("✓ Saved: 01_orders_by_city.png")
plt.close()

# ==========================================
# 4. BAR CHART - REVENUE BY CITY
# ==========================================

print("\n" + "=" * 70)
print("4. BAR CHART - REVENUE BY CITY")
print("=" * 70)

print("\n📊 Creating revenue chart...\n")

city_revenue = df.groupby('city')['amount'].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(city_revenue.index, city_revenue.values, color='green', alpha=0.7, edgecolor='black')

ax.set_title('Total Revenue by City', fontsize=14, fontweight='bold')
ax.set_xlabel('City', fontsize=12)
ax.set_ylabel('Revenue (Rs.)', fontsize=12)
ax.grid(axis='y', alpha=0.3)

# Add value labels
for i, (city, revenue) in enumerate(city_revenue.items()):
    ax.text(i, revenue + 200, f'Rs.{int(revenue):,}', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('02_revenue_by_city.png')
print("✓ Saved: 02_revenue_by_city.png")
plt.close()

# ==========================================
# 5. PIE CHART - ORDERS BY STATUS
# ==========================================

print("\n" + "=" * 70)
print("5. PIE CHART - ORDERS BY STATUS")
print("=" * 70)

print("\n📊 Creating pie chart...\n")

status_counts = df['status'].value_counts()

fig, ax = plt.subplots(figsize=(8, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99']
ax.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%',
       colors=colors, startangle=90, explode=(0.05, 0.05, 0.05))

ax.set_title('Order Status Distribution', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('03_status_distribution.png')
print("✓ Saved: 03_status_distribution.png")
plt.close()

# ==========================================
# 6. HORIZONTAL BAR CHART - SERVICE TYPE
# ==========================================

print("\n" + "=" * 70)
print("6. HORIZONTAL BAR CHART - REVENUE BY SERVICE TYPE")
print("=" * 70)

print("\n📊 Creating horizontal bar chart...\n")

service_revenue = df.groupby('service_type')['amount'].sum()

fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(service_revenue.index, service_revenue.values, color='coral', edgecolor='black')

ax.set_title('Revenue by Service Type', fontsize=14, fontweight='bold')
ax.set_xlabel('Revenue (Rs.)', fontsize=12)
ax.grid(axis='x', alpha=0.3)

# Add value labels
for i, (service, revenue) in enumerate(service_revenue.items()):
    ax.text(revenue + 200, i, f'Rs.{int(revenue):,}', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('04_revenue_by_service.png')
print("✓ Saved: 04_revenue_by_service.png")
plt.close()

# ==========================================
# 7. MULTIPLE SUBPLOTS
# ==========================================

print("\n" + "=" * 70)
print("7. MULTIPLE SUBPLOTS - DASHBOARD")
print("=" * 70)

print("\n📊 Creating multi-chart dashboard...\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('WindshieldHub Order Dashboard', fontsize=16, fontweight='bold')

# 1. Orders by City
ax1 = axes[0, 0]
city_counts.plot(kind='bar', ax=ax1, color='steelblue', edgecolor='black')
ax1.set_title('Orders by City', fontweight='bold')
ax1.set_ylabel('Count')
ax1.tick_params(axis='x', rotation=45)

# 2. Revenue by Status
ax2 = axes[0, 1]
status_revenue = df.groupby('status')['amount'].sum()
status_revenue.plot(kind='bar', ax=ax2, color='green', alpha=0.7, edgecolor='black')
ax2.set_title('Revenue by Status', fontweight='bold')
ax2.set_ylabel('Revenue (Rs.)')
ax2.tick_params(axis='x', rotation=45)

# 3. Amount Distribution (Histogram)
ax3 = axes[1, 0]
ax3.hist(df['amount'], bins=5, color='orange', alpha=0.7, edgecolor='black')
ax3.set_title('Order Amount Distribution', fontweight='bold')
ax3.set_xlabel('Amount (Rs.)')
ax3.set_ylabel('Frequency')

# 4. Status Pie Chart
ax4 = axes[1, 1]
status_counts.plot(kind='pie', ax=ax4, autopct='%1.1f%%')
ax4.set_title('Status Distribution', fontweight='bold')
ax4.set_ylabel('')

plt.tight_layout()
plt.savefig('05_dashboard.png', dpi=150)
print("✓ Saved: 05_dashboard.png")
plt.close()

# ==========================================
# 8. STATISTICS VISUALIZATION
# ==========================================

print("\n" + "=" * 70)
print("8. STATISTICS VISUALIZATION")
print("=" * 70)

print("\n📊 Creating statistics charts...\n")

# Box plot for amount distribution
fig, ax = plt.subplots(figsize=(10, 6))
box_data = [df[df['city'] == city]['amount'].values for city in df['city'].unique()]
ax.boxplot(box_data, labels=df['city'].unique())
ax.set_title('Amount Distribution by City', fontsize=14, fontweight='bold')
ax.set_ylabel('Amount (Rs.)')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('06_amount_distribution.png')
print("✓ Saved: 06_amount_distribution.png")
plt.close()

# ==========================================
# 9. USING PANDAS BUILT-IN PLOTTING
# ==========================================

print("\n" + "=" * 70)
print("9. PANDAS BUILT-IN PLOTTING")
print("=" * 70)

print("""
Pandas has built-in plotting methods (simpler!):

df['column'].plot(kind='bar')          # Bar chart
df['column'].plot(kind='line')         # Line chart
df.groupby('col1')['col2'].sum().plot(kind='bar')  # Grouped bar
df['column'].plot(kind='hist')         # Histogram
df['column'].value_counts().plot(kind='pie')       # Pie chart
""")

print("\n📊 Creating pandas plots...\n")

# Simple bar chart using pandas
fig, ax = plt.subplots(figsize=(10, 6))
city_counts.plot(kind='bar', ax=ax, color='teal', edgecolor='black')
ax.set_title('Orders by City (Using Pandas)', fontsize=14, fontweight='bold')
ax.set_ylabel('Number of Orders')
ax.set_xlabel('City')
plt.tight_layout()
plt.savefig('07_pandas_bar_chart.png')
print("✓ Saved: 07_pandas_bar_chart.png")
plt.close()

# ==========================================
# 10. EXPORT & DISPLAY SUMMARY
# ==========================================

print("\n\n" + "=" * 70)
print("10. VISUALIZATION SUMMARY")
print("=" * 70)

print("""
Charts created:
✓ 01_orders_by_city.png        - Bar chart: Orders per city
✓ 02_revenue_by_city.png       - Bar chart: Revenue per city
✓ 03_status_distribution.png   - Pie chart: Order status breakdown
✓ 04_revenue_by_service.png    - Horizontal bar: Service type revenue
✓ 05_dashboard.png             - Multi-panel dashboard
✓ 06_amount_distribution.png   - Box plot: Amount variation by city
✓ 07_pandas_bar_chart.png      - Pandas built-in plotting

All charts saved to current directory!
""")

# ==========================================
# 11. COMMON VISUALIZATION PATTERNS
# ==========================================

print("\n" + "=" * 70)
print("11. MATPLOTLIB COMMON PATTERNS")
print("=" * 70)

print("""
CHART TYPE              USE CASE                      MATPLOTLIB CODE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Bar Chart              Compare categories             plt.bar(x, y)
Line Chart             Show trends over time          plt.plot(x, y)
Pie Chart              Show proportions/percentages   plt.pie(values, labels=labels)
Histogram              Show data distribution         plt.hist(data, bins=10)
Scatter Plot           Show correlations              plt.scatter(x, y)
Box Plot               Show data spread               plt.boxplot(data)
Horizontal Bar         Compare when labels are long   plt.barh(x, y)

CUSTOMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Set title              ax.set_title('Title')
Set labels             ax.set_xlabel('X'), ax.set_ylabel('Y')
Set colors             color='steelblue'
Add grid               ax.grid(alpha=0.3)
Add legend             ax.legend()
Rotate labels          ax.tick_params(axis='x', rotation=45)
Set figure size        fig, ax = plt.subplots(figsize=(10, 6))
Save figure            plt.savefig('filename.png')
Show figure            plt.show()
""")

# ==========================================
# 12. INTERACTIVE PLOTTING TIPS
# ==========================================

print("\n" + "=" * 70)
print("12. TIPS FOR BETTER VISUALIZATIONS")
print("=" * 70)

print("""
✓ Choose the right chart type for your data
✓ Make titles clear and descriptive
✓ Label axes with units (Rs., %, etc.)
✓ Use colors to highlight important data
✓ Keep charts simple - avoid clutter
✓ Use appropriate scales (not too zoomed in/out)
✓ Add value labels for precise reading
✓ Use consistent colors across related charts
✓ Test your charts are color-blind friendly
✓ Save high-resolution (dpi=150+) for printing

For INTERACTIVE charts, explore:
- Plotly: plotly.com (interactive, web-based)
- Seaborn: Built on matplotlib (prettier defaults)
- Dash: Web dashboards with Python
""")

# ==========================================
# PRACTICE EXERCISES
# ==========================================

print("\n\n" + "=" * 70)
print("PRACTICE EXERCISES")
print("=" * 70)

print("""
Using the 'df' DataFrame, create these visualizations:

Exercise 1: Basic Charts
  TODO: Create bar chart of orders by city
  TODO: Create pie chart of order statuses
  TODO: Create histogram of order amounts

Exercise 2: Customization
  TODO: Add title, labels, grid to a chart
  TODO: Change colors to match WindshieldHub branding
  TODO: Add value labels on bars

Exercise 3: Grouped Analysis
  TODO: Create bar chart of revenue by status
  TODO: Create bar chart of avg amount by city
  TODO: Create bar chart comparing service types

Exercise 4: Dashboard
  TODO: Create 2x2 subplot with 4 different charts
  TODO: Make each chart show different analysis
  TODO: Add overall title to dashboard

Exercise 5: Export
  TODO: Save all charts as PNG files
  TODO: Create a 'reports' folder
  TODO: Save charts with descriptive names

HINTS:
- Use fig, ax = plt.subplots() for more control
- ax.bar(), ax.pie(), ax.hist() for different charts
- .plot(kind='bar') is simpler for basic charts
- plt.savefig('name.png') to save
- plt.show() to display (works in notebooks)
- Use figsize=(width, height) to set size
""")

print("\n✅ Day 12 Complete!")
print("🎯 Visualization turns raw data into insights!")
print("\n" + "=" * 70)
print("CONGRATULATIONS! YOU'VE COMPLETED 2 WEEKS OF PYTHON!")
print("=" * 70)

print("""
What you've learned:
✓ Day 1-2:   Python Basics (variables, lists, dicts)
✓ Day 3:     Functions & Loops
✓ Day 4:     File Handling & CSV
✓ Day 5:     MySQL Database Connections
✓ Day 6:     Jupyter Notebooks
✓ Day 7:     Mini Project (complete analysis)
✓ Day 8:     Pandas DataFrames
✓ Day 9:     Data Filtering & Selection
✓ Day 10:    GroupBy & Aggregations
✓ Day 11:    Data Cleaning
✓ Day 12:    Data Visualization

What's next?
→ Apply these skills to your WindshieldHub business data
→ Build automated reports and dashboards
→ Move into Machine Learning & AI (with these fundamentals)
→ Learn advanced topics: APIs, Web Frameworks, Deployment

You have the foundation. Keep practicing!
""")
