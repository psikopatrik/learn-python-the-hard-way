i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i:d}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)

    print(f"At the bottom i is {i:d}")

print("The numbers: ")

for num in numbers:
    print(num)
