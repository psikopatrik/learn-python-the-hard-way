# run the program like this (with three command line arguments):
# $ python ex13.py first 2nd 3rd

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
