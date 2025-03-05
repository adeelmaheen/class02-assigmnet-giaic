# Example of bitwise operators
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101

# AND operator: Performs bitwise AND operation on the binary representations of a and b
print("AND:", a & b)    # 12 = 0000 1100

# OR operator: Performs bitwise OR operation on the binary representations of a and b
print("OR:", a | b)     # 61 = 0011 1101

# NOT operator: Performs bitwise NOT operation on the binary representation of a
print("NOT:", ~a)       # -61 = 1100 0011

# LEFT SHIFT operator: Shifts the bits of a to the left by 2 positions
print("LEFT SHIFT:", a << 2)  # 240 = 1111 0000

# RIGHT SHIFT operator: Shifts the bits of a to the right by 2 positions
print("RIGHT SHIFT:", a >> 2) # 15 = 0000 1111