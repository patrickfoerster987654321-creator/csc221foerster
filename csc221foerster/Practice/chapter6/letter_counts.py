s = input("Please enter a string: ")
s = s.lower()

d = {}

for letter in s:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1



output_list = []
for letter in sorted(d.keys()):
    output_list.append(f"{letter} {d[letter]}\n")


print(" ".join(output_list))
