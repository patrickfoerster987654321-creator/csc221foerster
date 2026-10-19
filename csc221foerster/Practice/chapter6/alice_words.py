file = open('alice_in_wonderland.txt', 'r')

word_counts = {}

for line in file:
    words = line.split()
    for word in words:
        cleaned_word = word.strip("!\"#$%&'()*+-./:;<=>?@[\\]^_`{|}~,").lower()
        if cleaned_word:
            if cleaned_word in word_counts:
                word_counts[cleaned_word] += 1
            else:
                word_counts[cleaned_word] = 1


file.close()

sorted_words = sorted(word_counts.keys())
out_file = open('alice_words.txt', 'w')
out_file.write(f"{'Word':<20}{'Count':<10}\n")
out_file.write("=" * 23 + "\n")

for word in sorted_words:
    out_file.write(f"{word:<20}{word_counts[word]:<10}\n")

out_file.close()

alice_count = word_counts.get("alice",0)

longest_word = ""
for word in word_counts:
    if len(word) > len(longest_word):
        longest_word = word

print("alice_words.txt has been created")
print(f"1. The word 'alice' occurs {alice_count} times in the book.")
print(f"2. The longest word is '{longest_word}' with {len(longest_word)} characters.")
