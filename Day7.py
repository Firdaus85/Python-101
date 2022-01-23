# DAY 7 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is Asking questions or inputs from users by using input() and passing variable to a script by importing argv form sys
#The argv is an argument variable
#This variable holds the arguments you pass to your python script

from sys import argv
from typing import Counter







#This prompting is simpler and different from what I did yesterday on day 6
#It prompts the user and puts the results in a variable
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh")

print(f"So, you are {age} old, {height} tall and {weight} heavy")




script, first, second, third = argv


print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


#Exercise - Combine input with argv to make a script that gets more input from a user.

script, name, course, level= argv

script = input("Which script should I pass these values to?") 
name= input("What is your name?")
course= input("What course are you offering?")
level = input("What level?")


print(f"So, your name is {name}, studying {course}, in {level}.")
