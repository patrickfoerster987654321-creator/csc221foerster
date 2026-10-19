file = open("/usr/share/dict/words", "r")

current_letter = 'a'
count = 0

line = file.readline()

while line != "" and current_letter <= "z":
    word = line.strip().lower()

    if word and word[0] == current_letter:
        print(current_letter.upper() + ": " + word)
        count += 1

        if count == 3:
            current_letter = chr(ord(current_letter) + 1)
            count = 0

    line = file.readline()

file.close()
