print("=== Phase 1: Quick Contacts ===")

quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"

print(quick_contacts)

print("--- Access and Modify ---")
print("Mom's number:", quick_contacts["Mom"])

quick_contacts["Dad"] = "555-4321"
quick_contacts["Dentist"] = "555-2222"

print("Looking up Grandma:", quick_contacts.get("Grandma", "Contact not found"))
print("Updated contacts:", quick_contacts)

print("--- Delete and Analyze ---")
del quick_contacts["Pizza Place"]
old_work = quick_contacts.pop("Work")
print("Removed work number:", old_work)
print("Contacts remaining:", len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone numbers:", list(quick_contacts.values()))

# Contact records: name -> dictionary of details
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

# Call log: name -> {month -> minutes talked that month}
# Note: not every contact was called every month.
call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}

print("=== Phase 2: Contact Activity ===")

total_minutes = {}

for name, months in call_log.items():
    month_count = len(months)
    total = sum(months.values())
    average = total / month_count

    busiest_month = ""
    busiest_minutes = 0

    for month, minutes in months.items():
        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month

    total_minutes[name] = total

    print(f"{name}: {month_count} month(s), {total} min total, avg: {average:.2f}, busiest: {busiest_month} ({busiest_minutes})")

print("=== Phase 3: Aggregations ===")

month_stats = {}

for name, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {"minutes": [], "total": 0, "avg": 0, "contacts": 0}

        month_stats[month]["minutes"].append(minutes)
        month_stats[month]["total"] += minutes
        month_stats[month]["contacts"] += 1

for month, stats in month_stats.items():
    stats["avg"] = stats["total"] / stats["contacts"]

print("Monthly summary (sorted by average, highest first):")
for month, stats in sorted(month_stats.items(), key=lambda item: item[1]["avg"], reverse=True):
    print(f"{month}: {stats['total']} min total, {stats['avg']:.2f} avg ({stats['contacts']} contacts)")

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}

for name, total in total_minutes.items():
    details = contact_book[name]
    category = details["category"]
    city = details["city"]

    minutes_by_category[category] = minutes_by_category.get(category, 0) + total
    minutes_by_city[city] = minutes_by_city.get(city, 0) + total
    contacts_per_city[city] = contacts_per_city.get(city, 0) + 1

print("Minutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)

print("=== Phase 4: Comprehensions ===")

phone_book = {name: details["phone"] for name, details in contact_book.items()}
local_contacts = {name: details["phone"] for name, details in contact_book.items() if details["city"] == "Fort Wayne"}
activity_level = {name: "Frequent" if minutes >= 200 else "Occasional" for name, minutes in total_minutes.items()}

print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)

print("=== Phase 5: Tier Report ===")

# Return the tier for a contact based on total minutes.
def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"


for name, minutes in total_minutes.items():
    print(f"{name}: {minutes} min ({get_tier(minutes)})")

print("--- Tier Distribution ---")

tier_counts = {
    "Platinum": 0,
    "Gold": 0,
    "Silver": 0,
    "Bronze": 0,
    "Inactive": 0,
}

for name, minutes in total_minutes.items():
    if minutes >= 400:
        tier_counts["Platinum"] += 1
    elif minutes >= 200:
        tier_counts["Gold"] += 1
    elif minutes >= 100:
        tier_counts["Silver"] += 1
    elif minutes >= 50:
        tier_counts["Bronze"] += 1
    else:
        tier_counts["Inactive"] += 1

for tier, count in tier_counts.items():
    print(f"{tier}: {count}")

print("--- Top and Bottom ---")

most_contacted = ""
most_minutes = 0
least_contacted = ""
least_minutes = 999999

for name, minutes in total_minutes.items():
    if minutes > most_minutes:
        most_minutes = minutes
        most_contacted = name

    if minutes < least_minutes:
        least_minutes = minutes
        least_contacted = name

grand_total = sum(total_minutes.values())
average_per_contact = grand_total / len(total_minutes)

print(f"Most contacted: {most_contacted} ({most_minutes} min)")
print(f"Least contacted: {least_contacted} ({least_minutes} min)")
print("Total minutes:", grand_total)
print(f"Average per contact: {average_per_contact:.2f}")

print("--- Above Average Contacts ---")
for name, minutes in total_minutes.items():
    if minutes > average_per_contact:
        print(f"{name}: {minutes}")

print("=== Phase 6: Contact Hub Report ===")
print(f"{'Name':<12} {'Category':<10} {'City':<14} {'Minutes':>8} {'Tier'}")
print("-------------------------------------------------------")

for name, total in sorted(total_minutes.items(), key=lambda item: item[1], reverse=True):
    category = contact_book[name]["category"]
    city = contact_book[name]["city"]
    tier = get_tier(total)
    print(f"{name:<12} {category:<10} {city:<14} {total:>8} {tier}")

print("-------------------------------------------------------")
print(f"{len(total_minutes)} contacts | {grand_total} total minutes | {average_per_contact:.2f} average")
