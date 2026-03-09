score = 95

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

if score < 70:
    print("F")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A")

age = 0;
if age < 19:
    print("청소년 요금 적용")
else:
    if age < 65:
        print("성인 요금 적용")
    else:
        print("노인 요금 적용")