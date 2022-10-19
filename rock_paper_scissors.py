import random
welcome_message = '''This is a rock-paper-scissor game.
Select:
    0 for rock
    1 for paper
    2 for scissor
Type:
    any string to stop the game'''
print(welcome_message)

# Initial values
values = {
    'rock': 0,
    'paper': 1,
    'scissor': 2
}
key_list = list(values.keys())
val_list = list(values.values())

# Initial score
user_score = 0
computer_score = 0
cmd = 1

while cmd:
    computer_guess = random.randint(0, 2)
    try:
        user_guess = int(input('> '))
        if (user_guess == values['rock'] and computer_guess == values['scissor']) or (user_guess == values['paper'] and computer_guess == values['rock']) or (user_guess == values['scissor'] and computer_guess == values['paper']):
            print(
                f'You won! You: {key_list[val_list.index(user_guess)]} and Computer: {key_list[val_list.index(computer_guess)]}')
            user_score += 1
            print(
                f'Overall score is you:{user_score} and computer:{computer_score}.')
        elif (computer_guess == values['rock'] and user_guess == values['scissor']) or (computer_guess == values['paper'] and user_guess == values['rock']) or (computer_guess == values['scissor'] and user_guess == values['paper']):
            print(
                f'Computer won! You: {key_list[val_list.index(user_guess)]} and Computer: {key_list[val_list.index(computer_guess)]}')
            computer_score += 1
            print(
                f'Overall score is you:{user_score} and computer:{computer_score}.')

        elif user_guess > 2:
            cmd = 0
            print('Please enter only numbers between 0 and 2.')
        else:
            print(
                f'Draw! You: {key_list[val_list.index(user_guess)]} and Computer: {key_list[val_list.index(computer_guess)]}')
            print(
                f'Overall score is you:{user_score} and computer:{computer_score}.')
    except:
        cmd = 0
        print('Please enter only numbers between 0 and 2.')
