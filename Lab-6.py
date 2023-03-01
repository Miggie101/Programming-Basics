# Miguel Madrigal
# Mar. 2023
# Lab 6


# This program will let you know the cost of your travel with the disctance being miles.

# program loop
run = 'y'
while run == 'y':
    # user greeting
    print('This Program will calculate the cost of your travel in miles. You may use decimal points.')
    print()


    # user inputs
    distance = float(input('Please input the distance of your trip in miles: '))
    cpg = float(input('Please enter the Cost Per Gallon: '))
    mpg = float(input('Please enter the Miles Per Gallon: '))
    print()

    # do calculations
    answer = distance / mpg
    totalCost = answer * cpg
    
    # output to user
    print('The total cost of your trip is, $', format(totalCost, ',.2f'))

    # user input to loop or exit
    run = input('Would you like to find out the cost for another trip? (y or n): ').lower()
    
    # user error message if input is not y or n
    while run != 'y' and run != 'n':
        run = input('ERROR TEXT: Please enter a y or n: ').lower()

    print()
    

# exit message
print('Have a nice day!!')
