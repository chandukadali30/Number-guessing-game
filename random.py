import random
num=random.randrange(1,10)
guess=int(input("enter the number:"))

if guess==num:
          print("correct,you guessed it!")
elif guess>num:
    print("the guess is too high")
elif guess<num:
    print("the guess is too low")
else:
    print("wrong!The number is:", num)
