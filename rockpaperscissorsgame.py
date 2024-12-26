import random
print("Welcome to the rock paper scissors game!")
playerMove = input("What is your move - Rock,Paper or Scissors? Type with no spaces!!!.... ")

if playerMove.lower() == 'rock':
    move = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
elif playerMove.lower() == 'scissors':
    move = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
elif playerMove.lower() == 'paper':
    move = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

computerMove = random.randint(1, 3)
if computerMove == 1:
    computerMove = 'rock'
    computer = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
elif computerMove == 2:
    computerMove = 'paper'
    computer = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
elif computerMove == 3:
    computerMove = 'scissors'
    computer = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


if playerMove.lower() == 'rock':
    if computerMove == 'rock':
        print(f'You chose {move}, \nComputer chose {computer},\nTie!')
    elif computerMove == 'paper':
        print(f'You chose {move}, \nComputer chose {computer},\nYou lose')
    elif computerMove == 'scissors':
        print(f'You chose {move}, \nComputer chose {computer},\nYou win')
elif playerMove.lower() == 'paper':
    if computerMove == 'paper':
        print(f'You chose {move}, \nComputer chose {computer},\nTie!')
    elif computerMove == 'scissors':
        print(f'You chose {move}, \nComputer chose {computer},\nYou lose')
    elif computerMove == 'rock':
        print(f'You chose {move}, \nComputer chose {computer},\nYou win')
elif playerMove.lower() == 'scissors':
    if computerMove == 'scissors':
        print(f'You chose {move}, \nComputer chose {computer},\nTie!')
    elif computerMove == 'rock':
        print(f'You chose {move}, \nComputer chose {computer},\nYou lose')
    elif computerMove == 'paper':
        print(f'You chose {move}, \nComputer chose {computer},\nYou win')
else:
    print('Invalid move!')