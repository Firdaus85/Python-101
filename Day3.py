# DAY 3 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is Variables and Names 

# A variable is a reserved memory location for storing values

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity= cars_driven * space_in_a_car
average_passengers_per_car = passengers/cars_driven


print("There are", cars, "cars available.")# this line of code will print out 100 cuz 100 was assigned to cars variable
print("There are only", drivers, "drivers available") #this line will print out 30 cuz 30 was assigned to drivers variable
print("There will be", cars_not_driven, "empty cars today.")# this line of code prints out the results assigned to cars_not_driven of which the values assigned to cars minus the value assigned to drivers
print("We can transport", carpool_capacity, " people today.")#this line of code prints out the results assigned to carpool_capacity from values assigned to cars_driven multiplied by values assigned to space_in_a_car
print ("We need to put about", average_passengers_per_car, "in each car")#this line of code prints out thhe results assigned to average_passengers_per_car which is passengers divided by cars driven