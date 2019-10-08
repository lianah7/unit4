# by Liana Hill
# last updated October 3, 2019
# daily exercises

import random

# exercise one
number = int(input("Pick a number"))
if (number % 2) == 1:
    print("The number is odd")
else:
    print("The number is even")

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
    is_triangle(side1, side2, side3)


# rock paper scissors
def computer_input():
    print("Let's play rock, paper, scissors!")
    print("Pick rock, paper, or scissors")
    random.randint(1, 3)
    rock = 1
    paper = 2
    scissors = 3


def rock_paper_scissors(rock, paper, scissors):
    computer_input()


def main():
    num = int(input("Pick a number"))
    check = int(input("Pick another number"))
    if is_divisible(num, check):
        print("True")
    else:
        print("False")
    triangle_input()
    rock_paper_scissors()

main()