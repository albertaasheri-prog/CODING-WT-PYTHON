sandwich_orders = ['sardine', 'chicken', 'vegetables', 'beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)

sandwich_orders = ['pastrami', 'chicken', 'pastrami', 'beef', 'pastrami', 'sardine']
finished_sandwiches = []

print("\nSorry, the deli has run out of pastrami.\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nSandwiches that were made:")
for sandwich in finished_sandwiches:
    print(sandwich)