str1 = "python"
str2 = "nohtyp"

print(f"""
길이는 str1={len(str1)}과 str2={len(str2)}이고,
str2를 뒤집으면 {str2[::-1]}이므로... : """, end="")

print(len(str1) == len(str2) and (str1 == str2[::-1]))
print()