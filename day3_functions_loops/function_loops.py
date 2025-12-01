# DAY 3: Functions & Loops for Laravel Developers
# Think of functions like Laravel helper functions or controller methods

print("=" * 50)
print("Day 3: Functions & Loops")
print("=" * 50)

# ==========================================
# 1. BASIC FUNCTIONS
# ==========================================

# PHP: function greet($name) { return "Hello $name"; }
# Python:
def greet(name):
    return f"Hello {name}"

print(greet("Ahmed"))


# Function with multiple parameters
def calculate_total(price, tax_rate=0.17):  # 17% tax default
    """
    Calculate total with tax
    (This docstring is like PHPDoc comments)
    """
    tax = price * tax_rate
    total = price + tax
    return total

print(f"Total with tax: Rs.{calculate_total(1000)}")
print(f"Total with custom tax: Rs.{calculate_total(1000, 0.20)}")


# ==========================================
# 2. FUNCTIONS RETURNING MULTIPLE VALUES
# ==========================================

def get_order_stats(orders):
    """Like a Laravel repository method that calculates stats"""
    total_orders = len(orders)
    total_revenue = sum(order['amount'] for order in orders)
    avg_order = total_revenue / total_orders if total_orders > 0 else 0
    
    return total_orders, total_revenue, avg_order  # Returns a tuple

# Sample data
orders = [
    {"id": 1, "amount": 300},
    {"id": 2, "amount": 450},
    {"id": 3, "amount": 250}
]

# Unpack the tuple (like Laravel's list())
count, revenue, average = get_order_stats(orders)
print(f"\nStats: {count} orders, Rs.{revenue} revenue, Rs.{average:.2f} average")


# ==========================================
# 3. FOR LOOPS (Like foreach in PHP)
# ==========================================

print("\n" + "=" * 50)
print("FOR LOOPS")
print("=" * 50)

# Loop through list
technicians = ["Ahmed", "Ali", "Fatima", "Hassan"]

print("\nTechnicians:")
for tech in technicians:
    print(f"  - {tech}")


# Loop through list with index (like Laravel's foreach with keys)
print("\nTechnicians with numbers:")
for index, tech in enumerate(technicians, start=1):
    print(f"  {index}. {tech}")


# Loop through dictionary
order = {"id": 1, "customer": "John", "amount": 299.99, "status": "completed"}

print("\nOrder details:")
for key, value in order.items():
    print(f"  {key}: {value}")


# Loop through list of dictionaries (typical Laravel collection)
windshield_orders = [
    {"id": 1, "customer": "Ali", "amount": 299, "status": "completed", "time_taken": 45},
    {"id": 2, "customer": "Sara", "amount": 399, "status": "completed", "time_taken": 60},
    {"id": 3, "customer": "Ahmed", "amount": 249, "status": "pending", "time_taken": None}
]

print("\nProcessing orders:")
for order in windshield_orders:
    if order['status'] == 'completed':
        print(f"Order #{order['id']}: {order['customer']} - Rs.{order['amount']} ({order['time_taken']} mins)")


# ==========================================
# 4. WHILE LOOPS
# ==========================================

print("\n" + "=" * 50)
print("WHILE LOOPS")
print("=" * 50)

# Simple counter
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1


# Practical example: Process orders until queue is empty
order_queue = ["Order1", "Order2", "Order3"]

print("\nProcessing order queue:")
while order_queue:  # While list is not empty
    current_order = order_queue.pop(0)  # Remove first item
    print(f"Processing: {current_order}")


# ==========================================
# 5. LIST COMPREHENSIONS (Python's powerful feature)
# ==========================================

print("\n" + "=" * 50)
print("LIST COMPREHENSIONS (Python Magic!)")
print("=" * 50)

# PHP way:
# $amounts = [];
# foreach($orders as $order) {
#     $amounts[] = $order['amount'];
# }

# Python way (one line!):
amounts = [order['amount'] for order in windshield_orders]
print(f"All amounts: {amounts}")

# With condition (filter completed orders only)
completed_amounts = [order['amount'] for order in windshield_orders if order['status'] == 'completed']
print(f"Completed order amounts: {completed_amounts}")


# ==========================================
# PRACTICE EXERCISE 1: Calculate Technician Stats
# ==========================================

print("\n" + "=" * 50)
print("PRACTICE: Technician Performance")
print("=" * 50)

def calculate_avg_time(technician_orders):
    """
    Calculate average completion time for a technician
    Like a Laravel helper: TechnicianHelper::getAverageTime()
    """
    if not technician_orders:
        return 0
    
    total_time = 0
    completed_count = 0
    
    for order in technician_orders:
        if order['time_taken'] is not None:
            total_time += order['time_taken']
            completed_count += 1
    
    return total_time / completed_count if completed_count > 0 else 0


# Test data
ahmed_orders = [
    {"id": 1, "time_taken": 45},
    {"id": 2, "time_taken": 50},
    {"id": 3, "time_taken": 40}
]

avg_time = calculate_avg_time(ahmed_orders)
print(f"Ahmed's average time: {avg_time:.1f} minutes")


# ==========================================
# PRACTICE EXERCISE 2: Iterate All Orders
# ==========================================

def process_all_orders(orders):
    """Process orders and generate report"""
    print("\nOrder Processing Report:")
    print("-" * 50)
    
    total_revenue = 0
    completed_count = 0
    
    for order in orders:
        print(f"Order #{order['id']}: {order['customer']} - {order['status']}")
        
        if order['status'] == 'completed':
            completed_count += 1
            total_revenue += order['amount']
    
    print("-" * 50)
    print(f"Completed: {completed_count}/{len(orders)}")
    print(f"Total Revenue: Rs.{total_revenue}")
    
    return {
        "total_orders": len(orders),
        "completed_orders": completed_count,
        "total_revenue": total_revenue
    }


# Run the function
result = process_all_orders(windshield_orders)
print(f"\nResult object: {result}")


# ==========================================
# PRACTICE EXERCISE 3: Your Turn!
# ==========================================

print("\n" + "=" * 50)
print("YOUR TURN: Complete these exercises")
print("=" * 50)

# Exercise 1: Write a function that calculates total revenue by city
def revenue_by_city(orders):
    """
    TODO: 
    1. Loop through orders
    2. Group by city
    3. Sum amounts for each city
    4. Return a dictionary like: {"Lahore": 1000, "Karachi": 1500}
    """
    city_revenue = {}
    
    for order in orders:
        city = order.get('city', 'Unknown')
        amount = order.get('amount', 0)
        
        if city in city_revenue:
            city_revenue[city] += amount
        else:
            city_revenue[city] = amount
    
    return city_revenue


# Test data
test_orders = [
    {"id": 1, "city": "Lahore", "amount": 300},
    {"id": 2, "city": "Karachi", "amount": 400},
    {"id": 3, "city": "Lahore", "amount": 250},
    {"id": 4, "city": "Islamabad", "amount": 350}
]

city_stats = revenue_by_city(test_orders)
print("\nRevenue by city:")
for city, revenue in city_stats.items():
    print(f"  {city}: Rs.{revenue}")


# Exercise 2: Filter orders by status
def filter_by_status(orders, status):
    """Return only orders with specific status"""
    # Using list comprehension (Python way)
    return [order for order in orders if order['status'] == status]
    
    # OR using traditional loop:
    # filtered = []
    # for order in orders:
    #     if order['status'] == status:
    #         filtered.append(order)
    # return filtered


# ==========================================
# KEY TAKEAWAYS
# ==========================================

print("\n" + "=" * 50)
print("Python vs PHP Functions & Loops:")
print("=" * 50)
print("""
PHP                              |  Python
---------------------------------|----------------------------------
function myFunc($param) {}       |  def my_func(param):
foreach($arr as $item) {}        |  for item in arr:
foreach($arr as $k => $v) {}     |  for k, v in arr.items():
while($condition) {}             |  while condition:
$x++                             |  x += 1
count($arr)                      |  len(arr)
array_sum($arr)                  |  sum(arr)
return [$a, $b]                  |  return a, b (tuple)

INDENTATION IS SYNTAX IN PYTHON! (No curly braces needed)
""")

print("\n✅ Day 3 Complete!")
print("Next steps:")
print("1. Run this file: python day2_functions_loops.py")
print("2. Modify the exercises")
print("3. Create your own functions for WindshieldHub logic")
print("4. Move to Day 4: File Handling")