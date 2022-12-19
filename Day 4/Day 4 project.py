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
plays = [rock, paper, scissors]
#Write your code below this line 👇

play = input("Type 1 for rock, 2 for paper and 3 for scissors ")

if play == "1":
    print(plays[0])
elif play == "2":
    print(plays[1])
else:
    print(plays[2])

index = random.randint(0,2)

print(plays[index])

if play == str(index + 1):
    print("It's a draw")
elif play == "1" and str(index + 1) == "2":
    print("You lose!, Paper beats Rock!")
elif play == "1" and str(index + 1) == "3":
    print("You win!, Rock beats Scissors!")
elif play == "2" and str(index + 1) == "1":
    print("You win!, Paper beats Rock!")
elif play == "2" and str(index + 1) == "3":
    print("You lose!, Paper is cut by Scissors!")
elif play == "3" and str(index + 1) == "1":
    print("You lose!, Rock smashes Scissors!")
elif play == "3" and str(index + 1) == "2":
    print("You win!, Scissors cut Paper!")
else:
    print(f'These plays were not recorded: Play = {play}, Index = {str(index + 1)}')






