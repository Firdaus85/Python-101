# DAY 5 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is more printing and escaping sequences 
# \t - adds a tab of space
# \" - adds double-quotes
# \' - adds a single quote
# \\ - adds backlash
# A variable is a reserved memory location for storing values



days= "Mon Tue Wed Thu Fri Sat Sun"
months= "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec" #the \n puts the character on to a new line

print("Here are the days: ", days)
print("Here are the months: ", months)

print(""" With the three double-quotes, we will be able to type as much as we like. Even 4 lines if we want, or 5 or 6""")

print("I am 6'2\" tall.") #this line of code prints out 6'2", without the \", python will throw an error cuz it'll think the " is ending the string

tabby_cat= "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backlash_cat = "I'm \\ a \\ cat."

fat_cat= """
I'll do a list;
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backlash_cat)
print(fat_cat)