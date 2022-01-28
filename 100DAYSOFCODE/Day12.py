# DAY 12 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is funtions and files
# A function can take arguments, names, and commands
# You can create a function by using the word def

from sys import argv

script, input_file = argv

def print_all(f): #creates a funtion call print all with an argument of f as the name
    print(f.read())#reads the argument f and prints it out

def rewind(f): #creates a function name rewind and also has an argument name f
    f.seek(0) #using the seek function(it moves to the desired position given)

def print_a_line(line_count, f): #creates a funtion print a line and takes an argument of line count and f
    print(line_count, f.readline()) #prints out line count and f which read a complete line 

current_file = open(input_file) #opens the input file and stores or passes it to the variable current_file
print("First let's print the whole file:\n") 

print_all(current_file) #prints out the input file

print("Now let's rewind, kind of a tape.")
rewind(current_file)

print("Let's print three lines:")

current_line = 1 #line count stored or passed on to the variable current line
print_a_line(current_line, current_file) #calls the funtion print a line and passes the values of current line and a complete line of current file

current_line  += 1 #has the value of current line and adds 1 and stores it
print_a_line(current_line, current_file)#calls the funtion print a line and passes the values of current line and a complete line of current file

current_line  += 1 #has the value of current line and adds 1 and stores it
print_a_line(current_line, current_file)#calls the funtion print a line and passes the values of current line and a complete line of current file