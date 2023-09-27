# Miguel Madrigal
# Lab 8
# Mar. 2023
# This program will let you calculate any 2 numbers with any math you choose.
# user greeting
print("This program will let you calculate any 2 numbers with any math you
choose.")
print()
# loop starts
run = "Y"
while run == "Y":
        # user input for math problem
        choice = input("What type of math would you like to do? Please enter the first letter of the calculation: ").upper()
        if choice not in ("A", "S", "M", "D", "T", "E"):
                choice = input("ERROR!!! Please type A to add, S for sub, M to multiply, D to divide, T to truncate, E for exponent: ")
# user input
print()
  firstNumber = float(input("Enter first number: "))
  secondNumber = float(input("Enter seond number: "))
  print()
  # do calculation
if choice == "A":
          typevari = "plus"
          variAnswer = firstNumber + secondNumber
  elif choice == "S":
          typevari = "subtracted by"
          variAnswer = firstNumber - secondNumber
  elif choice == "M":
          typevari = "multiplied by"
          variAnswer = firstNumber * secondNumber
  elif choice == "D":
          typevari = "divided by"
		variAnswer = firstNumber / secondNumber
	elif choice == "T":
		typevari = "truncated by"
		variAnswer = firstNumber // secondNumber
	else:
		typevari = "raised to the power of"
		variAnswer = firstNumber ** secondNumber
		# user outputs
	print(firstNumber, typevari, secondNumber, "equals", format(variAnswer, ','))
	print()
	# restart or exit
	run = input("Would you like to try another problem? (Y/N): ").upper()
	# error loop
	while run not in ("Y", "N"):
		run = input("ERROR!!! Please type a Y or N!!: ").upper()
# exit message
print("Have a nice day!!")
print()
