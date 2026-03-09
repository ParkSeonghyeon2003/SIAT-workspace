sample = "abcde"
old_id = id(sample)
print(f"처음 주소: {old_id}")

sample = "f" + sample[1:]
print(sample)
new_id = id(sample)
print(f"나중 주소: {new_id}")

print(f"주소가 같은가요? {old_id == new_id}")