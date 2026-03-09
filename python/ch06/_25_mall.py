orders = [120000, 45000, 200000, 95000, 150000]

comp = [
    x if x < 100000 else x * 0.9
    for x in orders
]

for i in range(len(orders)):
    print(f"{orders[i]} => {comp[i]}")

"""
filtered_orders = filter(lambda x: x >= 100000, orders)
final_orders = list(map(lambda x: x * 0.9, filtered_orders))
print(final_orders)

final_orders = list(map(lambda x: x * 0.9, filter(lambda x: x >= 100000, orders)))
print(final_orders)

comp = [x * 0.9 for x in orders if x >= 100000]
print(comp)
"""
