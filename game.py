import random

# Put your code here
name = input("Howdy, what's your name?")
print(name + ", I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
num = random.randint(1, 100)

def guess_game():
    while True:
        count = 0
        user_guess = input("Your guess?")
        guess = int(user_guess)
        if guess < num:
            count += 1
            print("Your guess is too low, try again.")
        elif guess > num:
            count += 1
            print("Your guess is too high, try again.")
        else:
            count += 1
            print(f"Well done, {name}! You found my number in {count} tries!")
            break


guess_game()
