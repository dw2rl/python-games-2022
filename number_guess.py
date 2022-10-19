import random
welcome_message = '''This is a number guessing game.
Select range to guess on:
    0 for (1, 10)
    1 for (1, 50)
    2 for (1, 100)'''
print(welcome_message)
# Initial
guess_limit = 3
guess_count = 0

try:
    limit = int(input('Enter limit: '))
except TypeError:
    print('Unsupported operation')
limits = {
    0: 10,
    1: 50,
    2: 100
}

computer_guess = random.randint(1, limits[limit])
print(computer_guess)
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    if guess > computer_guess:
        print('Lower')
    elif guess < computer_guess:
        print('Higher')
    else:
        print('Correct')
        break
    guess_count += 1
else:
    print('You used all your guesses.')
