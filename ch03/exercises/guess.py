import random
x = random.randrange(1,11)
for i in range(3):
    guess = int(input("Guess the number 1 through 10:"))
    if guess < x:
        print("Too Low")
    elif guess > x:
        print("Too High")
    else:
        print("Correct!!")
    exit()
exit()