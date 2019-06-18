
# More Variables and Printing

# You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters.
# f for "format" as in f"Hello {somevar}". This is for python to put these variables in there.

name = 'Rashid A. Salim'
age = 20 # not a lie
height = 75 #inches
cm = 2.54
kg = 0.45
weight = 180 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'


print (f"Lets talk about {name}.")
print (f"Hes got {hair} hair.")
print(f"He's {weight * kg} kilograms heavy.")
print("Actually not that heavy.")
print(f"He's {height*cm} centimetres tall.")
print(f"He's got {eyes} eyes and {hair} hair. ")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")