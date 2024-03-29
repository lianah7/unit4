# by Liana Hill
# last updated October 3, 2019
# daily exercises

import random


# # exercise one
# number = int(input("Pick a number"))
# if (number % 2) == 1:
#     print("The number is odd")
# else:
#     print("The number is even")

# exercise two

def is_divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


# problem three
def is_triangle(side1, side2, side3):
    if (side1 >= side2 + side3) or (side3 >= side1 + side2) or (side2 >= side3 + side1):
        print("No")
    else:
        print("Yes")


def triangle_input():
    side1 = int(input("Please enter a length for a side"))
    side2 = int(input("Enter another length for the second side"))
    side3 = int(input("Enter another length for the third side"))
    print("Can you form a triangle?")
    is_triangle(side1, side2, side3)


# rock paper scissors
def computer_input():
    print("Let's play rock, paper, scissors!")
    print("Pick rock, paper, or scissors")
    computer_choice = random.randint(1, 3)
    print(computer_choice)
    if computer_choice == 1:
        print("The computer picked rock")
    elif computer_choice == 2:
        print("The computer chose paper")
    else:
        print("The computer picked scissors")


def rock_paper_scissors(computer_choice):
    computer_input()
    user_choice = int(input("Pick a number between 1 and 3"))
    if user_choice == 1:
        print("You picked rock")
    elif user_choice == 2:
        print("You picked paper")
    else:
        print("You chose scissors")
    if user_choice == computer_choice:
        print("Draw")
    elif user_choice >= computer_choice:
        print("You lost! Try again")
    else:
        print("You won!")


def driving(speed, birthday):
    if birthday:
        speed = speed - 5
    if speed <= 61:
        return 0
    elif 61 <= speed <= 80:
        return 1
    else:
        return 2


def main():
    num = int(input("Pick a number"))
    check = int(input("Pick another number"))
    if is_divisible(num, check):
        print("True")
    else:
        print("False")
    triangle_input()
    computer_choice = random.randint(1, 3)
    rock_paper_scissors(computer_choice)
    print(driving(75, True))


main()
