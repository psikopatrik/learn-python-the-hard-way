from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {from_file} to {to_file}..."
      .format(from_file=from_file, to_file=to_file))

in_file = open(from_file)
in_data = in_file.read()
# we could do these two on one line too:
# in_file = open(from_file); in_data = in_file.read()
# or
# in_data = open(from_file).read()  # then one should omit in_file.close() at the end of this script

print("The input file is {data_length} bytes long.".format(data_length=len(in_data)))

print("Does the output file exist? {!r}".format(exists(to_file)))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Alright, all done.")

out_file.close()
in_file.close()

