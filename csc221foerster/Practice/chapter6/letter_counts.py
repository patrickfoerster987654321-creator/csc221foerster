s = input("Please enter a string: ")
s = s.lower()

d = {}

for letter in s:
    if letter in s:
        d[letter] += 1
    else:
        d[letter] = 1
