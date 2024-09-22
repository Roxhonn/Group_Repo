# Swap two integer numbers using a temporary variable.

q = 20
r = 30
print("before swap")
print("q =", r)
print("r =", q)

temp = q
q = r 
r = temp

print("after swap")
print("q =", r)
print("r =", q)


# Repeat the exercise using the code format: a, b = b, a. Verify your results in both the cases.

# Initialize two integers
a = 5
b = 10

# Display original values
print("Before swap:")
print("a =", a)
print("b =", b)

# Swap using tuple assignment
a, b = b, a

# Display swapped values
print("After swap:")
print("a =", a)
print("b =", b)
