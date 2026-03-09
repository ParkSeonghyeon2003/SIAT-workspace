a = 10
b = 3
print(f"{a} / {b} = {a / b :.2f}")

val = 100000000
print(f"{val:,}")
print(f"{val:,.2f}")

val = 1234567
print(f"{val:_}")

val = 1234567.89
print(f"￦{val:,.0f}")

amount = 9876543.21

print(f"금액: ￦{amount:>20,.0f}")
print(f"금액: {amount:>20,.2f}")
print(f"금액: {amount:*>20,.2f}")

print(f"금액: ￦{amount:<20,.0f}")
print(f"금액: {amount:<20,.2f}")
print(f"금액: {amount:*<20,.2f}")