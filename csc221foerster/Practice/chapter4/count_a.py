s = input("Enter a sentence: ")
count = 0

for letter in s:
    if letter == 'a' or letter == 'A':
        count+=1
    

if count > 1:
    print(f"The letter 'a' appears in your sentence {count} times.")
elif count == 1:
    print(f"The letter 'a' appears in your sentence {count} time.")
else:
    print("The letter 'a' does not appear in your sentence.")
