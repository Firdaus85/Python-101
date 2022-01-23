# DAY 8 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is reading and writing files
#close: closes the file
# read: Reads the contents of the file
# readline: reads ust one line of the text file
# write: writes to the file
# seek: Moves the read/write to the location specified


from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.") #thhis line of code prints out the name of the file you assigned to argv
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file....")
target = open(filename, 'w') #opens the file and assigns it to the variable target and the 'w' opens the file in a write mode, write mode overwrites te data present in the file

print("Truncating the file. Goodbye!")
target.truncate() #erases everything in the target which contains the file txt  

print("Now I'm going to ask you for three lines.")

line1= input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

#this lines of codes writes the requested inputs to the target  
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

#easy way of writing to the file, much easier than the above line of codes
target.write(f"""
{line1},
{line2},
{line3}
""")

print("And finally, we close it.")
target.close()


