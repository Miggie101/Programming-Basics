# Miguel Madrigal
# Jan.2023
# Lab 3

# This program will let the user raise any integer to any power


# user greeting
print('This program will let you raise any interger to any interger power.')
print('Hello user, Welcome to Power Caculator')
print('Remeber to only use WHOLE numbers!!')
print()

# base number
base = int(input('Please enter the base number: '))

# exponent number
exponent = int(input('Please enter the power number for ' + str(base) + ': '))

# configure base into a integer
# base = int(base)
print()


# calculation raising the power with the base
answer = base ** exponent


# user final answer as a sentence
print(base, 'raised to the power of', exponent, 'equals', format(answer, ','))
print()


# exit message
print('Thank you for using my Power Calculator,\nHave a nice day')
# print('Have a nice day :)')





        
