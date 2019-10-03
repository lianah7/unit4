# by Liana Hill
# last updated October 3, 2019
# daily exercises

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


def main():
    num = int(input("Pick a number"))
    check = int(input("Pick another number"))
    if is_divisible(num, check):
        print("True")
    else:
        print("False")


main()