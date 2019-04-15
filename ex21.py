def add(a, b):
    print("ADDING {a:d} + {b:d}".format(a=a, b=b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING {a:d} - {b:d}".format(a=a, b=b))
    return a - b


def multiply(a, b):
    print("MULTIPLYING {a:d} * {b:d}".format(a=a, b=b))
    return a * b


def divide(a, b):
    print("DIVIDING {a:d} // {b:d}".format(a=a, b=b))
    return a // b


print("Let's do some math with just functions!")

age = add(30, 5)  # 35
height = subtract(78, 4)  # 74
weight = multiply(90, 2)  # 180
iq = divide(100, 2)  # 50

print("Age: {:d}, Height: {:d}, Weight: {:d}, IQ: {:d}".format(age, height, weight, iq))

# A puzzle for the extra credit, type it enyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# what = 35 + (74 - (180 * (50 // 2))) = 4395

print("That becomes:", what, "Can you do it by hand?")
