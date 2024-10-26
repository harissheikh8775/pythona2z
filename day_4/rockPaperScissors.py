import random

rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

arr=[rock,paper,scissors]

you_choose=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

comp_choose=random.randint(0,len(arr)-1)
print(f"Computer chose {comp_choose}")
print(arr[comp_choose])

print(f"You chose : {you_choose}")
print(arr[you_choose])
if you_choose>=3 or you_choose<0:
    print("You typed an invalid number. You lose!")
elif you_choose==0 and comp_choose==2:
    print("You win!")
elif comp_choose==0 and you_choose==2:
    print("You lose!")
elif comp_choose>you_choose:
    print("You lose!")
elif you_choose> comp_choose:
    print("You win!")
elif comp_choose==you_choose:
    print("It's a draw!")




