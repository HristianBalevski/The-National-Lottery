import random


def get_numbers():
    chosen_numbers = []

    while len(chosen_numbers) < 6:
        try:
            player_number = int(input('Please choose a number between 1 and 49: '))
            if player_number < 1 or player_number > 49:
                print('Please enter a valid number!')
                continue
            elif player_number in chosen_numbers:
                print('This number is already chosen')
                continue
            chosen_numbers.append(player_number)
        except ValueError:
            print('Invalid values, try again!')
            continue
    return chosen_numbers


def generate_winning_numbers():
    win_numbers = set()

    # Every time here I generate random number
    while len(win_numbers) < 6:
        random_number = random.randint(1, 49)
        win_numbers.add(random_number)

    return win_numbers


def count_win_numbers():
    count_equal_numbers = 0
    # Here I check how many equal numbers we have
    for num in player_numbers:
        if num in winning_numbers:
            count_equal_numbers += 1

    return count_equal_numbers


def check_for_reward(numbers):
    if numbers == 3:
        return 'Not Too Bad!\nYou Won 50 USD!'

    elif numbers == 4:
        return 'Good Game!\nYou Won 150 USD!'

    elif numbers == 5:
        return 'Very Good!\nYou Won 5000 USD!'

    elif numbers == 6:
        return 'Congratulations!\nYou Won 1 000 000 USD!'
    else:
        return 'Better Luck Next Time!'


print('''               
THE NATIONAL LOTTERY SPIN YOUR WAY TO $1 MILLION                                                          
''')

print('You have to choose 6 numbers!')
print()

player_numbers = get_numbers()
winning_numbers = generate_winning_numbers()

print()
print(f'These are your numbers: {", ".join([str(num) for num in player_numbers])}')

print(f'These are the winning numbers: {", ".join([str(num) for num in winning_numbers])}')
print()

equal_numbers = count_win_numbers()

if equal_numbers == 1:
    print(f'You Guessed only {equal_numbers} Number!')

elif equal_numbers == 2:
    print(f'You Guessed only {equal_numbers} Numbers!')

else:
    print(f'You Guessed {equal_numbers} Numbers!')

print(check_for_reward(equal_numbers))
