def multiply_nums(x, y):
    multiply = 0
    for i in range (y):
        multiply = multiply + x
    return multiply
    
def exponent(x, y):
    exponent = 1
    for i in range(y):
        exponent = exponent * x
    return exponent

def square(x):
    return exponent(x, 2)

def main():
    x = int(input("Enter a number:"))
    y = int(input("Enter a number (will be the exponent):"))
    result = multiply_nums(x, y)
    print (" Your number multiplied is:" + str(result))
    result = exponent (x, y)
    print (" Your numbers exponentiated is:" + str(result))
    result = square(x)
    print (" Your number squared is:" + str(result))

main()