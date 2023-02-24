# Miguel Madriga
# Feb. 2023
# Lab 5

# This program will convert Celsius to degree Fahrenheit.

# user greeting
print('This program will convert degree Celsius to Degree Fahrenheight.')
print('Please enter the tempature in degree Celsius; you may use decimals.')
print()

# user input tempature in celsius
celsius = float(input('Enter a tempature in degrees Celsius: '))

# do calculation
fahrenheit  =  (celsius  *  9 / 5)  +  32
print()

# the results 
print(celsius, 'degrees in Celsius is equal to', format(fahrenheit, '.1f'), 
'degrees Fahrenheit.')
print()

# exit message
print('Have a nice day!!')
