# Miguel Madrigal
# Feb. 2023
# Lab 4 

# user greeting
print('This program will let you enter two integer values that show you all the\
npossibble answers.')
print('Please enter ONLY whole numbers!!!')
print()

# user input numbers
fNumber = int(input('Please enter your first number: '))
sNumber = int(input('Please eneter your second number: '))
print() 


# do calculations
addAnswer = fNumber + sNumber
subAnswer = fNumber - sNumber
multAnswer = fNumber * sNumber
divAnswer = fNumber / sNumber
trugAnswer = fNumber // sNumber
modAnswer = fNumber % sNumber
expoAnswer = fNumber ** sNumber


# display the results
print(fNumber, '+' , sNumber, '=', format(addAnswer, ','))
print(fNumber, '-' , sNumber, '=', format(subAnswer, ','))
print(fNumber, '*' , sNumber, '=', format(multAnswer, ','))
print(fNumber, '/' , sNumber, '=', format(divAnswer, ',.2f'))
print(fNumber, '//' , sNumber, '=', format(trugAnswer, ','))
print(fNumber, '%' , sNumber, '=', format(modAnswer, ',')) 
print(fNumber, '**' , sNumber, '=', format(expoAnswer, ','))
print()

# exit message
print('Have a great day :)!!')
