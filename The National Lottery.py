import random

print('''               
THE NATIONAL LOTTERY SPIN YOUR WAY TO $1 MILLION                                                          
''')

print('You have to choose 6 numbers!')
print()

valid_numbers = []
chosen_numbers = []

for num in range(1, 51):
    valid_numbers.append(num)

rotation = 0

while True:
    try:
        player_number = int(input('Please choose a number between 1 and 50: '))
        if player_number <= 0 or player_number > 50:
            print('Please enter a valid number!')
            continue
        elif player_number in chosen_numbers:
            print('This number is already chosen')
            continue
        chosen_numbers.append(player_number)
    except ValueError:
        print('Invalid values, try again!')
        continue
    rotation += 1
    if rotation == 6:
        break

winning_numbers = set()

# Every time here I generate random number
while len(winning_numbers) != 6:
    random_number = random.randint(1, 50)
    winning_numbers.add(random_number)

print()
print(f'These are your numbers: {", ".join([str(num) for num in chosen_numbers])}')

print(f'These are the winning numbers: {", ".join([str(num) for num in winning_numbers])}')
print()

count_equal_numbers = 0
# Here I check how many equal numbers we have
for num in chosen_numbers:
    if num in winning_numbers:
        count_equal_numbers += 1

if count_equal_numbers == 1:
    print(f'You Guessed only {count_equal_numbers} Number!')

elif count_equal_numbers == 2:
    print(f'You Guessed only {count_equal_numbers} Numbers!')

else:
    print(f'You Guessed {count_equal_numbers} Numbers!')

if count_equal_numbers == 3:
    print('Not Too Bad!')
    print('You Won 50 USD!')

elif count_equal_numbers == 4:
    print('Good Game!')
    print('You Won 150 USD!')

elif count_equal_numbers == 5:
    print('Very Good!')
    print('You Won 5000 USD!')

elif count_equal_numbers == 6:
    print('Congratulations!')
    print('You Won 1 000 000 USD!')
else:
    print('Better Luck Next Time!')
