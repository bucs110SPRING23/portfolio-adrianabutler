num = int(input("Enter an upper limit:"))
for i in range(num+1):
    print("number:", i)
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('buzz')
