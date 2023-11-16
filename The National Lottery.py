import random


def get_valid_number(chosen_numbers):
    while True:
        try:
            player_number = int(input('Please choose a number between 1 and 49: '))
            validate_number(player_number, chosen_numbers)
            return player_number
        except ValueError:
            print('Invalid values, try again!')


def validate_number(player_number, chosen_numbers):
    if player_number < 1 or player_number > 49:
        print('Please enter a valid number.')

    if player_number in chosen_numbers:
        print('This number is already chosen')


def get_numbers():
    chosen_numbers = []

    while len(chosen_numbers) < 6:
        player_number = get_valid_number(chosen_numbers)
        chosen_numbers.append(player_number)

    return chosen_numbers


def generate_winning_numbers():
    # Generate 6 unique random numbers in the range [1, 49]
    return random.sample(range(1, 50), 6)


def count_win_numbers(player_numbers, winning_numbers):
    # Count the number of equal numbers between player's and winning numbers
    return len(set(player_numbers) & set(winning_numbers))


def check_for_reward(numbers):
    # Check the number of matches and return the corresponding message
    if numbers == 3:
        return 'Not Too Bad!\nYou Won $50!'
    elif numbers == 4:
        return 'Good Game!\nYou Won $150!'
    elif numbers == 5:
        return 'Very Good!\nYou Won $5000!'
    elif numbers == 6:
        return 'Congratulations!\nYou Won $1,000,000!'
    else:
        return 'Better Luck Next Time!'


if __name__ == "__main__":
    print('''
    THE NATIONAL LOTTERY SPIN YOUR WAY TO $1 MILLION                                                          
    ''')

    print('You have to choose 6 numbers!\n')

    # Getting the user's numbers
    player_numbers = get_numbers()

    # Generating winning numbers
    winning_numbers = generate_winning_numbers()

    # Display the user's numbers and winning numbers
    print(f'\nThese are your numbers: {", ".join(map(str, player_numbers))}')
    print(f'These are the winning numbers: {", ".join(map(str, winning_numbers))}\n')

    # Number of matching numbers
    equal_numbers = count_win_numbers(player_numbers, winning_numbers)

    # Display a message about the matches
    if equal_numbers in (1, 2):
        print(f'You Guessed only {equal_numbers} Number!')
    else:
        print(f'You Guessed {equal_numbers} Numbers!')

    # Reward check and message output
    print(check_for_reward(equal_numbers))
