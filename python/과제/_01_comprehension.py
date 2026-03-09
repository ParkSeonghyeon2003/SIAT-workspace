orders_data = [
    {"user": "Alice", "items": [15000, 20000, 5000]}, 
    {"user": "Bob", "items": [50000, 70000]},         
    {"user": "Charlie", "items": [3000, 2000]},       
    {"user": "Alice", "items": [10000]},              
]

price_sum = {}
for order in orders_data:
    name = order["user"]
    total_spent = sum(order["items"])
    price_sum[name] = price_sum.get(name, 0) + total_spent

final_data = {
    name: (total_spent, "SILVER" if total_spent < 30000 else
                        "GOLD" if total_spent < 100000 else "VIP")
    for name, total_spent in price_sum.items()
}

print(f"고객명\t총 구매액\t회원 등급")
print("-" * 40)
[print(f"{name}\t{total_spent:>7,}원\t{grade}")
 for name, (total_spent, grade) in final_data.items()]
print()