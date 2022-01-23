# DAY 8 of 100DAYSOFCODE challenge
# Using learn python 3 the hard way 
# Today's challenge is reading files with the read()


from sys import argv

script, filename= argv

txt = open(filename) #this line of code opens the filename and pass or assign it to the txt variable

print(f"Here's your file {filename}")
print(txt.read()) #it prints out the constituents of the txt variable

print("Type the filename again: ")
file_again = input(">") #Requests for the file name again and passes it to file_again

txt_again = open(file_again) #opens the file_again and assign or pass it to txt_again
print(txt_again.read())# Reads out the constituents of txt_again