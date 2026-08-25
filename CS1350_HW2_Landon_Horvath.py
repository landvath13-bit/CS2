# CS1350 Homework 2
# Dictionaries
# Units 1.1 - 2.3


# ============================================================
# UNIT 1.1 
# ============================================================

# -------------------------
# Beginner
# -------------------------

my_info = {
    "name": "Landon",
    "age": 19,
    "major": "Cybersecurity and Criminal Justice"
}

print("Unit 1.1 Beginner")
print(my_info)


# -------------------------
# Intermediate
# -------------------------

menu = {
    "burger": 8.99,
    "fries": 3.49,
    "pizza": 10.99,
    "soda": 1.99
}

course_credits = {
    "CS1350": 3,
    "MATH201": 3,
    "ENGL101": 3,
    "CRIM101": 3
}

print("\nUnit 1.1 Intermediate")
print(menu)
print(course_credits)


# -------------------------
# Advanced
# -------------------------

weekly_temps = dict(
    Monday=72,
    Tuesday=75,
    Wednesday=68,
    Thursday=70,
    Friday=74,
    Saturday=78,
    Sunday=76
)

print("\nUnit 1.1 Advanced")
print(weekly_temps)


# ============================================================
# UNIT 1.2 
# ============================================================

# -------------------------
# Beginner
# -------------------------

pet = {
    "name": "Buddy",
    "type": "dog",
    "age": 3
}

print("\nUnit 1.2 Beginner")
print(pet["name"])
print(pet["age"])


# -------------------------
# Intermediate
# -------------------------

print("\nUnit 1.2 Intermediate")

color = pet.get("color", "unknown")
print(color)

grades = {
    "Alice": 85,
    "Bob": 92,
    "Carol": 78
}

grade = grades.get("Alice", 0)

if grade >= 70:
    print("Student passed the course")
else:
    print("Student failed the course")


# -------------------------
# Advanced
# -------------------------

products = {
    "laptop": 999.99,
    "mouse": 29.99,
    "keyboard": 79.99
}

print("\nUnit 1.2 Advanced")

product_name = "laptop"
price = products.get(product_name)

if price is not None:
    print(price)
else:
    print("Product not available")

product_name = "phone"
price = products.get(product_name)

if price is not None:
    print(price)
else:
    print("Product not available")


# ============================================================
# UNIT 1.3 
# ============================================================

# -------------------------
# Beginner
# -------------------------

inventory = {}

inventory["apples"] = 10
inventory["bananas"] = 15
inventory["oranges"] = 12

print("\nUnit 1.3 Beginner")
print(inventory)


# -------------------------
# Intermediate
# -------------------------

scores = {
    "Team A": 45,
    "Team B": 38
}

scores["Team B"] = 52
scores["Team C"] = 41

removed_score = scores.pop("Team A")

print("\nUnit 1.3 Intermediate")
print("Team A score:", removed_score)
print(scores)


# -------------------------
# Advanced
# -------------------------

cart = {}

cart["burger"] = 8.99
cart["fries"] = 3.49
cart["soda"] = 1.99

cart["burger"] = 9.99

removed_item = cart.pop("fries")

print("\nUnit 1.3 Advanced")
print("Removed price:", removed_item)

print("Final cart:", cart)

total = sum(cart.values())
print("Total price:", total)


# ============================================================
# UNIT 2.1 
# ============================================================

# -------------------------
# Beginner
# -------------------------

print("\nUnit 2.1 Beginner")

# a) "student_name"
# Valid because strings are immutable and hashable.

# b) [1, 2, 3]
# Invalid because lists are mutable and not hashable.

# c) 100
# Valid because numbers are immutable and hashable.

# d) ("x", "y")
# Valid because tuples are immutable and hashable.

# e) {"a": 1}
# Invalid because dictionaries are mutable and not hashable.

# f) frozenset({1, 2})
# Valid because frozensets are immutable and hashable.

print("a) valid - strings are immutable and hashable")
print("b) invalid - lists are mutable and not hashable")
print("c) valid - numbers are immutable and hashable")
print("d) valid - tuples are immutable and hashable")
print("e) invalid - dictionaries are mutable and not hashable")
print("f) valid - frozensets are immutable and hashable")


# -------------------------
# Intermediate
# -------------------------

locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}

print("\nUnit 2.1 Intermediate")

data = {
    "a": 1,
    "b": 2,
    "a": 3,
    "b": 4
}

print(data)
print(len(data))

print("Hash value of my name:", hash("Landon"))
print("Hash value of 100:", hash(100))


# -------------------------
# Advanced
# -------------------------

game_scores = {
    ("Alice", "Game1"): 100,
    ("Bob", "Game1"): 125,
    ("Carol", "Game2"): 150
}

print("\nUnit 2.1 Advanced")

print(game_scores[("Alice", "Game1")])

import time

big_list = list(range(100000))
big_dict = {i: i for i in range(100000)}

start = time.time()
result = 99999 in big_list
list_time = time.time() - start

start = time.time()
result = 99999 in big_dict
dict_time = time.time() - start

print("List search:", list_time)
print("Dictionary search:", dict_time)

if list_time > dict_time:
    print("Dictionary is faster")
else:
    print("List is faster")


# ============================================================
# UNIT 2.2 
# ============================================================

# -------------------------
# Beginner
# -------------------------

temps = {
    "Monday": 72,
    "Tuesday": 75,
    "Wednesday": 68
}

print("\nUnit 2.2 Beginner")

print(temps.keys())
print(temps.values())
print(len(temps))


# -------------------------
# Intermediate
# -------------------------

print("\nUnit 2.2 Intermediate")

print("Highest temperature:", max(temps.values()))
print("Lowest temperature:", min(temps.values()))

if "Friday" in temps:
    print("Friday is in the dictionary")
else:
    print("Friday is not in the dictionary")

temps.setdefault("Thursday", 70)

print(temps)

keys_view = temps.keys()

temps["Friday"] = 74

print(keys_view)


# -------------------------
# Advanced
# -------------------------

prices = {
    "laptop": 999,
    "phone": 699,
    "tablet": 449,
    "watch": 299
}

print("\nUnit 2.2 Advanced")

total_value = sum(prices.values())
average_price = total_value / len(prices)

print("Total value:", total_value)
print("Average price:", average_price)

most_expensive = max(prices.values())
least_expensive = min(prices.values())

for name, price in prices.items():
    if price == most_expensive:
        print("Most expensive:", name, price)

for name, price in prices.items():
    if price == least_expensive:
        print("Least expensive:", name, price)

import sys

keys_view = prices.keys()
keys_list = list(prices.keys())

print("View size:", sys.getsizeof(keys_view))
print("List size:", sys.getsizeof(keys_list))

prices.update({
    "headphones": 199,
    "keyboard": 99,
    "mouse": 49
})

print("All products:", prices)


# ============================================================
# UNIT 2.3
# ============================================================

# -------------------------
# Beginner
# -------------------------

colors = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple"
}

print("\nUnit 2.3 Beginner")

for fruit, color in colors.items():
    print(f"The {fruit} is {color}")

print(list(colors.items()))


# -------------------------
# Intermediate
# -------------------------

prices = {
    "coffee": 4.50,
    "tea": 3.00,
    "juice": 5.25
}

print("\nUnit 2.3 Intermediate")

for item, price in prices.items():
    tax = price * 0.10
    total = price + tax
    print(f"{item}: ${price:.2f} + tax = ${total:.2f}")

count = 0

for item, price in prices.items():
    if price > 4.00:
        count += 1

print("Items costing more than $4.00:", count)

x = 10
y = 20

x, y = y, x

print("x:", x)
print("y:", y)

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# -------------------------
# Advanced
# -------------------------

scores = {
    "Alice": 88,
    "Bob": 65,
    "Carol": 92,
    "Dave": 71,
    "Eve": 58
}

print("\nUnit 2.3 Advanced")

best_name, best_score = max(
    scores.items(),
    key=lambda x: x[1]
)

print("Highest score:", best_name, best_score)

passed = {}
failed = {}

for name, score in scores.items():
    if score >= 70:
        passed[name] = score
    else:
        failed[name] = score

print("Passed:", passed)
print("Failed:", failed)

average = sum(scores.values()) / len(scores)

print("Class average:", average)

deviations = {}

for name, score in scores.items():
    deviations[name] = score - average

print("Deviations:", deviations)

big_dict = {i: i * 2 for i in range(50000)}

start = time.time()

for key, value in big_dict.items():
    result = key + value

items_time = time.time() - start

start = time.time()

for key in big_dict.keys():
    value = big_dict[key]
    result = key + value

keys_time = time.time() - start

print("items() time:", items_time)
print("keys() + lookup time:", keys_time)

if items_time < keys_time:
    print("items() is faster")
else:
    print("keys() + lookup is faster")