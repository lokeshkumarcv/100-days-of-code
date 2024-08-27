import random

choices=['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
print("What do you choose.type 0 for rock, 1 for paper or 2 for scissors.")
a= int(input())
if a>=0 and a<=2:
    print(f"your chose:{choices[a]}")
else:
    print("invalid choice.you lose by default")
    exit()

b = random.randint(0,2)
print(f"Computer choose:{choices[b]}")

if a == b :
    print("It's a Draw")

elif (a==1 and b==0) or (a==2 and b==1)or (a==0 and b==2):
    print("you win")

elif (a==0 and b==1)  or (a==1 and b==2) or (a==2 and b==0):
    print("you lose")
