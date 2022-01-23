# DAY 4 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge Embedding variables inside a string by using a special {} and then put the variable inside and i have to always start the string with a letter f which stands for format

# A variable is a reserved memory location for storing values


my_name = "Firdaus Abdul-Kareem"
my_age = 24
my_height = 74 #inches
my_height_in_centimeter = my_height * 2.54 #converts my height which is in inches to centimeters and stores it here
my_weight =150 #pounds
my_weight_in_kilograms = my_weight / 2.205 #converts my weight which is in pounds to kilogram and stores it here
my_eyes = "Brown"
my_teeth ="White"
my_hair = "Black"


print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.") 
print("OR")
print(f"He's {my_height_in_centimeter} centimeters tall.")
print(f"He's {my_weight} pounds heavy")
print("OR")
print(f"He's {my_weight_in_kilograms} kilogram heavy")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")


total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get a total of {total}.")






print("Mary had a little lamb.")
print("It's fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # it prints out . 10 times


end1="c"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"

print(end1 + end2 + end3 + end4 + end5 + end6, end='')
print(end7 + end8 + end9 + end10 + end11 + end12)