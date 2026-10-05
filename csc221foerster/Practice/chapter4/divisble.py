print("Num   Div by 2 and/or 3?")
print("---   ------------------")
num = 2;
while num < 21:
    if num % 2 == 0 and num % 3 == 0:
        print(f"{num}            both")
    elif num % 2 == 0 and num % 3 != 0:
        print(f"{num}            by 2")
    elif num % 3 == 0 and num % 2 != 0:
        print(f"{num}            by 3")
    else:
        print(f"{num}            neither")

    num += 1




