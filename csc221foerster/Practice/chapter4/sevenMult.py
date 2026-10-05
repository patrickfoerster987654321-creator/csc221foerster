list = [3, 4, 5, 6]
foundOne = False

for item in list:
    if item % 7 == 0:
        foundOne = True
        print(f"{item} is the first multiple of 7")
        break


if foundOne == False:
    print("No multiples of 7 found");
