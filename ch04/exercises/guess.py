import random
num = random.randrange(1,10)
tries = 0
for i in range(10):
    guess = int(input("Guess the number 1 through 1000:"))
if guess == num:
    print("You guessed it! My number was", num, "it took you", tries, "tries to guess")
elif guess < num:
    print("Too Low!")
    tries = tries + 1
elif guess > num:
    print("Too High!")
    tries = tries + 1