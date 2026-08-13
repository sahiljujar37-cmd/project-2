import random
number = 7

print("guess the number in range of 1 to 100")
guess= int(input("enter your guess number"))

if guess == number:
    print("you guess a rigth number")
elif guess < number:
    print("too low")
else:
    print("too high")

    print("number is ",number)


