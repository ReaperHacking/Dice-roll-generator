#Dice Roll Generator (1-6, 6-12, 12-1000)
import random

#Intro and Options
print(
  "Hello! Welcome to this dice roll generator! Choose between 3 options below! \n"
)

print("> Roll 1 - Random Number 1-6")
print("> Roll 2 - Random Number 6-12")
print("> Roll 3 - Random Number 12-1000\n")

#Setting Computerized Variables
computer_roll1 = random.randint(1, 6)
computer_roll2 = random.randint(6, 12)
computer_roll3 = random.randint(12, 1000)


def roll_function(roll):
  if roll == '1':
    print(f'{computer_roll1}!')
  elif roll == '2':
    print(f'{computer_roll2}!')
  elif roll == '3':
    print(f'{computer_roll3}!')
  else:
    print("Sorry, invalid option between 1, 2, 3, error :/ \n")


#While Loop and Conditions
roll_again = 'Y'
while roll_again == 'Y':
  roll = input("Roll 1, 2, or 3? (1, 2, 3): ")
  roll_function(roll)

  re_roll = input("Would you like to re-roll? (Y/N): ").upper()
  if re_roll == 'N':
    print("Thank you for playing my game! Have a good one!")
    break
  elif re_roll == 'Y':
    continue
  else:
    print("ERROR, didn't pick Y or N :/")
    break
