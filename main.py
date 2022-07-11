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

#Write your code below this line 👇

# Rules of the game
# Rock0 wins against scissors2: 👊
# Scissors2 wins against paper1: ✋
# Papper1 wins agaist Rock0: ✌️

# Rock = 👊0
# Paper = ✋1
# Scissors = ✌️2

import random

Player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:\n "))

if Player >= 3 or Player < 0:
 print("You typed an invalid number, You lose!")



# For Player 
if Player == 0: 
   print(rock)  
elif Player == 1:
  print(paper)
elif Player == 2:
  print(scissors) 

  
# For Computer
computer = random.randint(0, 2)
if computer == 0:
  print("Computer chose:")
  print(rock)
elif computer == 1:
  print("Computer chose:")
  print(paper)
elif computer == 2:
  print("Computer chose:")
  print(scissors)



  
# For the Game
  
if Player == 0 and computer == 2:
  print("You win!")
elif computer == 0 and Player == 2:
  print("You lose!")
elif Player == 2 and computer == 1:
  print("You win!")
elif computer == 2 and Player == 1:
  print("You lose!")  
elif Player == 1 and computer == 0:
  print("You win!")
elif computer == 1 and Player == 0:
  print("You lose!")  
elif computer == Player:
  print("Its a draw!")



  
  
  

  
   





  
  


 
  
  

