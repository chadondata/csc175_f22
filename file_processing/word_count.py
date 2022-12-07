# Word Counter
import string

file_contents = []
words = {}

with open('alice.txt', encoding='utf8') as the_file:
    this_line = the_file.readline() # Priming read
    while this_line:
        file_contents.append(this_line)
        this_line = the_file.readline()

for line in file_contents:
    new_string = line.translate(str.maketrans('', '', string.punctuation))
    new_string = new_string.strip()
    new_string = new_string.lower()
    line_words = new_string.split(" ")
    for word in line_words:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1

for key in words.keys():
    if "mad" in key:
        print(f'{key} {words[key]}')
print(f"{ words['mad']}")
