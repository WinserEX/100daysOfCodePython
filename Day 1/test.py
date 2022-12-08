a = 10
b = 100

print(a, b)

if a != b:
    c = a + b
    a = c - a
    b = c - b

print(a, b)