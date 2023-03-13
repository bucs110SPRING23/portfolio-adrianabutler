# strings - list of characters - immutable
# lists - list of any set of objects - mutable
# tuples - immutable list of any set of objects
#mytuple = (5,2,3,6,1)
# mytuple[0] = 1 ERROR!!!
# dictionaries - used to store using key/value pairs
#mydictionary = {"a":1, "b":2, "c":3}
#mydictionary["a"]
#mydictionary["b"]
# while loop
# while <boolean conditions>
#       <code block>
# otherwise skips it

def find_max():
    print("Please enter 3 numbers: ")
    a = int(input(":"))
    b = int(input(":"))
    c = int(input(":"))

    max = a
    if b > max:
        max = b
    if c > max:
        max = c

print(max)