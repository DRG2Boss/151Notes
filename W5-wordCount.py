import string
file1 = open("W5-warAndPeace.txt", 'r', encoding='UTF8')
# Based on how we set this up, warAndPeace could be swapped with almost any text file and work fine like wordFile.
all_lines = file1.readlines()

word_counts = {"the": 0}

for line in all_lines:
    words_in_line = line.split(" ")
    # Within each word for words_in_line, we need to REMOVE any punctuation characters and weird whitespaces/formatting
    for word in words_in_line:
        word = word.replace(string.punctuation, '')
        # This is a "string" command, which is built into Python. Still NEED to include "import string" line however.
        word = word.strip()
        word = word.lower()
        if word_counts.get(word):
            word_counts[word] += 1
        else:
            word_counts[word] = 1
for word, count in word_counts.items():
    print(f"{word}:\t {count}")
# Like how \n inserts a new line, \t inserts a new tab.
