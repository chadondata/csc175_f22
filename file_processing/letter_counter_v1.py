# Letter Counter
import string

file_contents = []
letters = {}

with open('alice.txt', encoding='utf8') as the_file:
    this_line = the_file.readline() # Priming read
    while this_line:
        file_contents.append(this_line)
        this_line = the_file.readline()

for line in file_contents:
    for char in line:
        if char.isalpha():
            char = char.lower()
            if char in letters.keys():
                letters[char] += 1
            else:
                letters[char] = 1

for letter in letters.keys():
    print(f'{letter} : {letters[letter]}')

print("Alphabetic:")
for letter in sorted(letters.keys()):
    print(f'{letter} : {letters[letter]}')

print("Percentages:")
total_letters = 0
for letter in letters.keys():
    total_letters += letters[letter]
print(f'Total letters: {total_letters}')

distributions = {}
print("Percentages:")
for letter in sorted(letters.keys()):
    print(f'{letter} : {round((letters[letter] * 100) / total_letters)}')
    distributions[letter] = round((letters[letter] * 100) / total_letters)

for letter in distributions.keys():
    print(f'{letter} : {distributions[letter]} : {"*" * distributions[letter]}')
