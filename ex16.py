from sys import argv

script, filename = argv

print("We are going to erase {filename!r}".format(filename=filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally, we close it.")
target.close()

print('\n')

# Printing the file
target = open(filename, 'r')

txt = target.read()

print("This is content of the file {filename!r} you've just created:".format(filename=filename))
print(txt)

target.close()
