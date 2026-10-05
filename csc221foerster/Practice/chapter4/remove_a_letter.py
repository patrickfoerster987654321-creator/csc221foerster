s = input("Enter a string: ")
s2 = ''

letter = input("Enter a letter to remove: ")

for i in s:
    if i != letter:
        s2 += i


print(s2)

