import random


def leave_the_game():
    raise SystemExit('Invalid Input. Please enter a valid number')


def repeated_number():
    raise SystemExit('You can not choose the same number two times. Please try again.')


print('''               
                THE NATIONAL LOTTERY                                                 
            SPIN YOUR WAY TO $1 MILLION                                                          
''')

valid_symbols = []
chosen_numbers = []

for num in range(1, 51):
    valid_symbols.append(str(num))

number_one = input('Please enter a number between 1 and 50: ')
chosen_numbers.append(number_one)

if number_one not in valid_symbols:
    leave_the_game()

number_two = input('Please enter a number between 1 and 50: ')

if number_two in chosen_numbers:
    repeated_number()

if number_two not in valid_symbols:
    leave_the_game()
chosen_numbers.append(number_two)

number_three = input('Please enter a number between 1 and 50: ')

if number_three in chosen_numbers:
    repeated_number()

if number_three not in valid_symbols:
    leave_the_game()
chosen_numbers.append(number_three)

number_four = input('Please enter a number between 1 and 50: ')

if number_four in chosen_numbers:
    repeated_number()

if number_four not in valid_symbols:
    leave_the_game()
chosen_numbers.append(number_four)

number_five = input('Please enter a number between 1 and 50: ')

if number_five in chosen_numbers:
    repeated_number()

if number_five not in valid_symbols:
    leave_the_game()
chosen_numbers.append(number_five)

number_six = input('Please enter a number between 1 and 50: ')

if number_six in chosen_numbers:
    repeated_number()

if number_six not in valid_symbols:
    leave_the_game()

list_of_numbers = [number_one, number_two, number_three, number_four, number_five, number_six]
count_equal_numbers = 0

# Every time here I generate random numbers
copy_list = random.sample(range(1, 51), 6)

# Here I convert int to str
copy_list = [str(int) for int in copy_list]
print()
print(f'These are your numbers: {", ".join(list_of_numbers)}')

print(f'These are the winning numbers: {", ".join(copy_list)}')
print()

# Here I check how many equal numbers we have
for num in list_of_numbers:
    if num in copy_list:
        count_equal_numbers += 1
        
if count_equal_numbers == 1:
    print(f'You Guessed only {count_equal_numbers} Number!')
    
elif count_equal_numbers == 2:
    print(print(f'You Guessed only {count_equal_numbers} Numbers!'))
    
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
