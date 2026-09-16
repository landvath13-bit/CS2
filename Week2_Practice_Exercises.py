# Week 2 Lecture 1: Dictionary III

# Unit 3.1 Practice Exercises

# Beginner
inventory = {"apples": 50, "bananas": 30, "oranges": 25}

for product in inventory:
    print(product)

total_items = sum(inventory.values())
print(total_items)

for product, quantity in inventory.items():
    print(product, quantity)

# Intermediate
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}

for product in sorted(prices):
    print(product, prices[product])

for product in sorted(prices, key=prices.get):
    print(product, prices[product])

most_expensive_item = ""
most_expensive_price = 0

for product, price in prices.items():
    if price > most_expensive_price:
        most_expensive_item = product
        most_expensive_price = price

print(most_expensive_item, most_expensive_price)

# Advanced
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

average_temp = sum(temps.values()) / len(temps)
print(average_temp)

hottest_day = ""
hottest_temp = 0
coldest_day = ""
coldest_temp = 1000

for day, temp in temps.items():
    if temp > hottest_temp:
        hottest_day = day
        hottest_temp = temp

    if temp < coldest_temp:
        coldest_day = day
        coldest_temp = temp

print("Hottest:", hottest_day, hottest_temp)
print("Coldest:", coldest_day, coldest_temp)

above_average = 0

for temp in temps.values():
    if temp > average_temp:
        above_average += 1

print(above_average)


# Unit 3.2 Practice Exercises

# Beginner
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}

print(products["laptop"]["price"])

for product, info in products.items():
    print(product, info["stock"])

# Intermediate
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = {}

for country, capital in zip(countries, capitals):
    country_capitals[country] = capital

print(country_capitals)

products["tablet"] = {"price": 449, "stock": 30}
print(products)

for product, info in list(products.items()):
    if info["stock"] < 20:
        del products[product]

print(products)

# Advanced
company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

for department, employees in company.items():
    for employee, salary in employees.items():
        print(employee, salary)

for department, employees in company.items():
    average_salary = sum(employees.values()) / len(employees)
    print(department, average_salary)

highest_paid_employee = ""
highest_salary = 0

for department, employees in company.items():
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_paid_employee = employee
            highest_salary = salary

print(highest_paid_employee, highest_salary)


# Unit 3.3 Practice Exercises

# Beginner
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}
celsius = {day: (temp - 32) * 5/9 for day, temp in temps.items()}
print(celsius)

# Intermediate
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

passing = {name: score for name, score in scores.items() if score >= 70}
print(passing)

def to_letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"

letter_grades = {name: to_letter(score) for name, score in scores.items()}
print(letter_grades)

student_ids = {"Alice": 101, "Bob": 102}
id_lookup = {student_id: name for name, student_id in student_ids.items()}
print(id_lookup)

# Advanced
sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]

sales_by_region = {}

for region, person, amount in sales:
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

sales_by_person = {}

for region, person, amount in sales:
    sales_by_person[person] = sales_by_person.get(person, 0) + amount

print(sales_by_person)

nested_sales = {}

for region, person, amount in sales:
    if region not in nested_sales:
        nested_sales[region] = {}

    nested_sales[region][person] = nested_sales[region].get(person, 0) + amount

print(nested_sales)


# Week 2 Lecture 2: Sets

# Unit 1 Practice Exercises

# Beginner
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

numbers = set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print(len(numbers))

empty = set()
print(empty)

# Intermediate
text = "mississippi"
unique_characters = set(text)
print(unique_characters)
print(len(unique_characters))

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))
print(unique_emails)

# s = {[1, 2], [3, 4]}
# This fails because lists are unhashable and cannot be set elements.

# Advanced
big_set = set(range(1000000))
big_list = list(range(1000000))

print(999999 in big_set)
print(999999 in big_list)

frozen = frozenset([1, 2, 3])
frozen_dict = {frozen: "value"}
print(frozen_dict)

edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
nodes = set()

for edge in edges:
    nodes.add(edge[0])
    nodes.add(edge[1])

print(nodes)


# Unit 2 Practice Exercises

# Beginner
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)

# Intermediate
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_shifts = morning_shift & evening_shift & weekend_shift
print(all_shifts)

at_least_one_shift = morning_shift | evening_shift | weekend_shift
print(at_least_one_shift)

morning_only = morning_shift - evening_shift - weekend_shift
print(morning_only)

exactly_one_shift = (
    (morning_shift - evening_shift - weekend_shift)
    | (evening_shift - morning_shift - weekend_shift)
    | (weekend_shift - morning_shift - evening_shift)
)
print(exactly_one_shift)

# Advanced
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

eligible = prereqs_met & has_space & paid_tuition
print(eligible)

prereqs_not_paid = prereqs_met - paid_tuition
print(prereqs_not_paid)

all_students = prereqs_met | has_space | paid_tuition
missing_prereqs_or_tuition = all_students - (prereqs_met & paid_tuition)
print(missing_prereqs_or_tuition)


# Unit 3 Practice Exercises

# Beginner
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(1)
print(numbers)

evens = {x for x in range(21) if x % 2 == 0}
print(evens)

numbers = {1, 2, 3}
numbers.discard(4)
print(numbers)

# Intermediate
data = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
seen = set()
unique = []

for item in data:
    if item not in seen:
        seen.add(item)
        unique.append(item)

print(unique)

sentence = "To be or not to be that is the question"
unique_words = {word for word in sentence.lower().split()}
print(unique_words)

expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
missing = expected - actual
print(missing)

# Advanced
def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates

print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

all_three = alice & bob & carol
print(all_three)

only_alice = alice - bob - carol
print(only_alice)

all_skills = alice | bob | carol
print(all_skills)

def common_chars(string1, string2):
    return set(string1) & set(string2)

print(common_chars("hello", "world"))
