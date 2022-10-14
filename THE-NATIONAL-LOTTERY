import random
print(
    '''##################################################
#              THE NATIONAL LOTTERY              #
#                                                #
#           SPIN YOUR WAY TO £1 MILLION          #
#                                                #
#         All you need is to guess 6 numbers     #
#                                                #
#                  GOOD LUCK!                    # 
#                                                #
#                                                #
##################################################
''')

number_one = int(input('Please enter a number between 0 and 49: '))
if number_one > 49:
    raise SystemExit('Invalid Input. The number should be between 0 and 49... Try again')
number_two = int(input('Please enter a number between 0 and 49: '))
if number_two > 49:
    raise SystemExit('Invalid Input. The number should be between 0 and 49... Try again')
number_three = int(input('Please enter a number between 0 and 49: '))
if number_three > 49:
    raise SystemExit('Invalid Input. The number should be between 0 and 49... Try again')
number_four = int(input('Please enter a number between 0 and 49: '))
if number_four > 49:
    raise SystemExit('Invalid Input. The number should be between 0 and 49... Try again')
number_five = int(input('Please enter a number between 0 and 49: '))
if number_five > 49:
    raise SystemExit('Invalid Input. The number should be between 0 and 49... Try again')
number_six = int(input('Please enter a number between 0 and 49: '))
if number_one > 49:
    raise SystemExit('Invalid Input. The number should be between 0 and 49... Try again')

list_of_numbers = [number_one, number_two, number_three, number_four, number_five, number_six]

# Here I convert int to str
string_list_of_numbers = [str(int) for int in list_of_numbers]
count_equal_numbers = 0

# Every time here I generate random numbers
national_lottery = range(0, 49)
copy_list = (random.choices(national_lottery, k=6))

# Here I convert int to str
string_copy_list = [str(int) for int in copy_list]
print()
print(f'These are your numbers: {", ".join(string_list_of_numbers)}')

print(f'These are the winning numbers: {", ".join(string_copy_list)}')
print()

# Here I check how many equal numbers we have
for num in list_of_numbers:
    if num in copy_list:
        count_equal_numbers += 1
if count_equal_numbers == 1:
    print(f'You Guessed {count_equal_numbers} Number!')
else:
    print(f'You Guessed {count_equal_numbers} Numbers!')

if count_equal_numbers == 3:
    print('Not Too bad!')
    print('You Won 50 GBP!')
elif count_equal_numbers == 4:
    print('Good Game!')
    print('You Won 150 GBP!')
elif count_equal_numbers == 5:
    print('Very Good!')
    print('You Won 5000 GBP!')
elif count_equal_numbers == 6:
    print('Congratulations!')
    print('You Won 1 000 000 GBP!')
else:
    print('Better Luck Next Time!')
