# DAY 11 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is funtions
# A function can take arguments, names, and commands
# You can create a function by using the word def


def cheese_and_crackers(cheese_count, boxes_of_crackers): #This is a function with a name cheese and crackers which takes arguments of variable name cheese count and boxes of crackers
    print(f"You have {cheese_count} cheeses! ")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enoughh for a party")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30) #this line of code calls the function cheese and crackers and passes values to the arguments of the function

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)