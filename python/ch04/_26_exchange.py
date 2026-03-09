lst = [1, 2, 3]
t = tuple(lst)
print(t) # (1, 2, 3)

t2 = (4, 5, 6)
lst2 = list(t2)
print(lst2) # [4, 5, 6]

# list to dict
lst = [("a", 1), ("b", 2)]
d = dict(lst)
print(d) # {"a": 1, "b": 2}

# tuple to dict
t = (("x", 10), ("y", 20))
d2 = dict(t)
print(d2) # {"x": 10, "y": 20}

##### dict to list/tuple #####
d = {"a": 1, "b": 2}

# key
keys_list = list(d.keys()) # dict_keys to list
keys_tuple =tuple(d.keys()) # dict_keys to tuple
print(keys_list) # ["a", "b"]
print(keys_tuple) # ("a", "b")

# value
values_list = list(d.values()) # dict_values to list
values_tuple = tuple(d.values()) # dict_values to tuple
print(values_list) # [1, 2]
print(values_tuple) # (1, 2)

# pair
items_list = list(d.items()) # dict_items to list
items_tuple = tuple(d.items()) # dict_items to tuple
print(items_list) # [("a", 1), ("b", 2)]
print(items_tuple) # (("a", 1), ("b", 2))