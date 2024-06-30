rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

gameimg = [rock, paper, scissors]
play = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if play < 0 or play > 2:
    print("Invalid choice. You lose!")
else:
    print("You chose:")
    print(gameimg[play])

    comp = random.randint(0, 2)
    print("Computer chose:")
    print(gameimg[comp])

    if play == comp:
        print("It's a draw")
    elif (play == 0 and comp == 2) or (play == 1 and comp == 0) or (play == 2 and comp == 1):
        print("You win!")
    else:
        print("You lose!")
