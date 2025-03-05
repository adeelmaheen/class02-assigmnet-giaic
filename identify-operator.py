
# Identity operators in Python
# 'is' and 'is not' are the identity operators in Python.
# They are used to check if two values (or variables) are located on the same part of the memory.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# 'is' operator: Returns True if both variables point to the same object
print(a is b)  # True, because b is assigned to a

# 'is not' operator: Returns True if both variables do not point to the same object
print(a is not c)  # True, because c is a different object with the same content
