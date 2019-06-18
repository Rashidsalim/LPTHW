# Parameters, Unpacking, Variables

#Line 3 shows "import". This is how you add features(modules) to your script from the Python feature set.
from sys import argv

# read the WYSS section for how to run this
script, first, second, third = argv

print(">>>> argv=", repr(argv))

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:",second)
print("Your third variable is:", third)