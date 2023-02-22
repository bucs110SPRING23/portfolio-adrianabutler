import random
num = random.randrange(1,11)
for i in range(3):
    guess = int(input("Guess the number 1 through 10:"))
if guess == num:
    print("You guessed it! My number was", num)
elif guess < num:
    print("Too Low!")
elif guess > num:
    print("Too High!")