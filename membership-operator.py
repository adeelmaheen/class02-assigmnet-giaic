# Membership operators in Python
# 'in' and 'not in' are the membership operators in Python.
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary).

a = [1, 2, 3, 4, 5]
b = 3
c = 10

# 'in' operator: Returns True if the value is found in the sequence
print(b in a)  # True, because 3 is in the list a

# 'not in' operator: Returns True if the value is not found in the sequence
print(c not in a)  # True, because 10 is not in the list a
