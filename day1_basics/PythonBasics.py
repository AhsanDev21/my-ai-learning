# DAY 1-2: Python Basics for Laravel Developers
# You already know programming concepts - this is just new syntax!

print("=" * 50)
print("Welcome to Python Basics!")
print("=" * 50)

# ==========================================
# 1. VARIABLES (Like PHP, but no $ sign!)
# ==========================================

# PHP: $name = "John";
# Python:
name = "John"
age = 25
price = 99.99
is_active = True  # Note: Capital T, not lowercase

print(f"\nName: {name}, Age: {age}")  # f-strings are like PHP interpolation


# ==========================================
# 2. STRINGS (Similar to PHP)
# ==========================================

# Concatenation
full_name = "John" + " " + "Doe"
print(f"Full name: {full_name}")

# String methods (like PHP's str_* functions)
text = "  hello world  "
print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Stripped: '{text.strip()}'")
print(f"Replaced: '{text.replace('world', 'Python')}'")


# ==========================================
# 3. LISTS (Like PHP arrays with numeric keys)
# ==========================================

# PHP: $orders = ["pending", "completed", "cancelled"];
# Python:
orders = ["pending", "completed", "cancelled"]

print(f"\nOrders: {orders}")
print(f"First order: {orders[0]}")  # Index starts at 0
print(f"Last order: {orders[-1]}")  # Negative index from end

# Add item (like PHP array_push)
orders.append("processing")
print(f"After append: {orders}")

# Length (like PHP count())
print(f"Total orders: {len(orders)}")


# ==========================================
# 4. DICTIONARIES (Like PHP associative arrays - SUPER IMPORTANT!)
# ==========================================

# PHP: $order = ["id" => 1, "customer" => "John", "amount" => 299.99];
# Python:
order = {
    "id": 1,
    "customer": "John",
    "amount": 299.99,
    "status": "pending"
}

print(f"\nOrder: {order}")
print(f"Customer: {order['customer']}")
print(f"Amount: ${order['amount']}")

# Add new key
order["technician"] = "Mike"
print(f"Updated order: {order}")

# Check if key exists (like PHP isset())
if "customer" in order:
    print("Customer exists!")


# ==========================================
# 5. LIST OF DICTIONARIES (Your typical database result)
# ==========================================

# This is like what you get from Laravel's DB::select()
orders_list = [
    {"id": 1, "customer": "John", "amount": 299.99, "status": "completed"},
    {"id": 2, "customer": "Sarah", "amount": 399.99, "status": "pending"},
    {"id": 3, "customer": "Mike", "amount": 199.99, "status": "completed"}
]

print("\n" + "=" * 50)
print("All Orders:")
print("=" * 50)

# Loop through orders (like foreach in PHP)
for order in orders_list:
    print(f"Order #{order['id']}: {order['customer']} - ${order['amount']} ({order['status']})")


# ==========================================
# 6. TUPLES (Immutable lists - can't be changed)
# ==========================================

# Use for fixed data that shouldn't change
coordinates = (40.7128, -74.0060)  # NYC coordinates
print(f"\nCoordinates: {coordinates}")
print(f"Latitude: {coordinates[0]}, Longitude: {coordinates[1]}")


# ==========================================
# PRACTICE EXERCISE 1: Create Your Own Order
# ==========================================

print("\n" + "=" * 50)
print("PRACTICE: Create your order record")
print("=" * 50)

# TODO: Create a dictionary for a windshield order
my_order = {
    "order_id": 101,
    "customer_name": "Your Name",
    "service_type": "windshield_replacement",
    "vehicle": "Toyota Camry 2020",
    "amount": 350.00,
    "status": "scheduled",
    "technician": "Ahmed",
    "location": {
        "city": "Lahore",
        "lat": 31.5204,
        "lon": 74.3587
    }
}

print(f"My Order: {my_order}")
print(f"Service: {my_order['service_type']}")
print(f"Location: {my_order['location']['city']}")


# ==========================================
# PRACTICE EXERCISE 2: List of Orders
# ==========================================

windshield_orders = [
    {"id": 1, "customer": "Ali", "amount": 299, "city": "Lahore"},
    {"id": 2, "customer": "Fatima", "amount": 399, "city": "Karachi"},
    {"id": 3, "customer": "Hassan", "amount": 249, "city": "Islamabad"}
]

print("\n" + "=" * 50)
print("WindshieldHub Orders:")
print("=" * 50)

total_revenue = 0
for order in windshield_orders:
    print(f"Order #{order['id']}: {order['customer']} in {order['city']} - Rs.{order['amount']}")
    total_revenue += order['amount']

print(f"\nTotal Revenue: Rs.{total_revenue}")


# ==========================================
# KEY DIFFERENCES FROM PHP/LARAVEL:
# ==========================================

print("\n" + "=" * 50)
print("PHP vs Python Quick Reference:")
print("=" * 50)
print("""
PHP                          |  Python
-----------------------------|---------------------------
$variable                    |  variable (no $)
$arr = array()              |  arr = []
$dict = ["key" => "value"]  |  dict = {"key": "value"}
echo $name                   |  print(name)
foreach($arr as $item)      |  for item in arr:
count($arr)                  |  len(arr)
array_push($arr, $item)     |  arr.append(item)
isset($arr['key'])          |  'key' in arr
$arr['key']                  |  arr['key']
true/false                   |  True/False (capital!)
null                         |  None
. (concat)                   |  + (concat)
""")

print("\n✅ Day 1-2 Complete!")
print("Next: Run this file and understand each section")
print("Then move to day2_functions_loops.py")