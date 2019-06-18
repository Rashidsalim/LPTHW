
# Printing, Printing

# Variable with an Array?
formatter = "{} {} {} {}"

# Function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))

print(formatter.format(
    "So heavy, California",
    "I will love you, can't afford you,",
    "They say heaven's waiting for you,",
    "So I'm headed to California"
))
