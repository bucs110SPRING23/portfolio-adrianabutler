def find_max():
    print("Please enter 3 numbers: ")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))

    max = a
    if b > max:
        max = b
    if c > max:
        max = c

print(max)
