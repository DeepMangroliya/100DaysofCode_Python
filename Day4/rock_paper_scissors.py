# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# #Write your code below this line 👇
# import random

# choice_list = [rock, paper, scissors]

# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# computer_choice = random.randint(0, 2)
# print("Computer Choose")
# if user_choice == 0:
#     print(choice_list[0])
#     if computer_choice == 2:
#         print(choice_list[2])
#         print("You Win!\n")
#     elif computer_choice == 1:
#         print(choice_list[1])
#         print("You Lose!\n")
#     else: 
#         print(choice_list[0])
#         print("Draw")
        
# elif user_choice == 1:
#     print(choice_list[1])
#     if computer_choice == 0:
#         print(choice_list[0])
#         print("You Win!\n")
#     elif computer_choice == 2:
#         print(choice_list[2])
#         print("You Lose!\n")
#     else: 
#         print(choice_list[1])
#         print("Draw")
# else: 
#     print(choice_list[2])
#     if computer_choice == 1:
#         print(choice_list[1])
#         print("You Win!\n")
#     elif computer_choice == 0:
#         print(choice_list[0])
#         print("You Lose!\n")
#     else: 
#         print(choice_list[2])
#         print("Draw")


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

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")