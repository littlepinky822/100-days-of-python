import random

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

all_choices = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
if 0 <= player_choice < 3:
    print(all_choices[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{all_choices[computer_choice]}")

if player_choice < 0 or player_choice >= 3:
    print("You typed in an invalid number. You lose.")
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif player_choice == 2 and computer_choice == 1:
    print("You win")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == computer_choice:
    print("Draw")
else:
    print('You lose')