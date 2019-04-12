my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# str.format()
print("Let's talk about {my_name}.".format(my_name=my_name))  # Let's talk about Zed A. Shaw.
print("He's {my_height:d} inches tall.".format(my_height=my_height))  # He's 74 inches tall.
print("He's {my_weight:d} pounds heavy.".format(my_weight=my_weight))  # He's 180 pounds heavy.
print("Actually that's not too heavy.")  # Actually that's not too heavy.
print("He's got {my_eyes} eyes and {my_hair} hair.".format(my_eyes=my_eyes, my_hair=my_hair))  # He's got Blue eyes and Brown hair.
print("His teeth are usually {my_teeth} depending on the coffee.".format(my_teeth=my_teeth))  # His teeth are usually White depending on the coffee.
# this line is tricky, try to get it exactly right
print("If I add {0}, {1}, and {2} I get {sum_attr}.".format(my_age, my_height, my_weight, sum_attr=my_age + my_height + my_weight))  # If I add 35, 74, and 180 I get 289.

print()

# format string literals
print(f"Let's talk about {my_name}.")
print(f"He's {my_height:d} inches tall.")
print(f"He's {my_weight:d} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# this line is tricky, try to get it exactly right
print(f"If I add {my_age:d}, {my_height:d}, and {my_weight} I get {my_age + my_height + my_weight}.")
