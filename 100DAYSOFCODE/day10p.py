from sys import argv
from os.path import exists


script, from_file, to_file = argv

print(f"Copying from {from_file}, to {to_file}")

in_file = open(from_file) #opens from_file and assigns in to in_file
indata = in_file.read() #reads in_file and assigns it to indata

print(f"The input file is {len(indata)} bytes long")#prints out the length of constituents of indata

print(f"Does the output file exist? {exists(to_file)}")# checks to see if the file exist(returns true or false)
print("Ready, hit return to continue, CTRL-C to abort")
input("?")

out_file= open(to_file, 'w') #opens to_file and assign it to the variable out_file in write mode
out_file.write(indata) #indata is then written to out_file

print("All done.....")

out_file.close()
in_file.close()
