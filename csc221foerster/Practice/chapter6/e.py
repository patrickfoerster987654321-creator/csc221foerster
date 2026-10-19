import string
i = input("Please enter a text file: ")

file = open(i, 'r')
text = file.read()
file.close()

cleaned_text = ""
for char in text:
    if char not in string.punctuation:
        cleaned_text += char
    else:
        cleaned_text += " "

words = cleaned_text.split()
total_words = len(words)
count = 0

for word in words:
    if 'e' in word.lower():
        count += 1


if total_words > 0:
    percentage = (count/total_words)*100
else:
    percentage = 0.0

print(f"Your text contains {total_words} words, of which {count} ({percentage:.1f}%) contain an 'e'.")
