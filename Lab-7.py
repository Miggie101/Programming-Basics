# Miguel Madrigal
# Mar. 2023
# Lab 7
# This program will put a fruit based off of the letter the user has chosen from A, B, and C.

# start loop
run = "Y"
while run == "Y":
#user greeting
  print("Please enter an A, B, or C to display a fruit with the corresponding letter.")
  print()

  # user input
  choice = input("Please enter a letter A, B, or C: ").upper()

  # error user input message
  while choice not in ("A", "B", "C"):
    choice = input("ERROR. Please input A, B, or C: ").upper()
  print()

  # user output
  if choice == "A":
    print("You got a Apple!!!!")
  elif choice == "B":
    print("You got a Banana!!!!")
  else:
    print("You got a Coconut!!!!")
  print()

  # exit loop or restart
  run = input("Do you want to find out the other letters? (Y/N): ").upper()
  while run not in ("Y", "N"):
    run = input ("ERROR! Please enter a Y or N: ").upper()
  print()

# exit message
print("Have a nice day!!!")
print()
