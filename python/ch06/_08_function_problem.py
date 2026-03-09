def calc(a, b, op="+"):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "//":
        return a // b
    elif op == "%":
        return a % b
    elif op == "**":
        return a ** b
    else:
        return None

print(calc(10, 5))
print(calc(10, 5, "-"))
print(calc(10, 5, "*"))
print(calc(10, 5, "/"))
print(calc(b=20, a=7))