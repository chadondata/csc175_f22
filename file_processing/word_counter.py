# Word Counter
the_lines = []
the_words = {}

with open('alice.txt', encoding='utf8') as the_file:
    the_line = the_file.readline()
    while the_line:
        the_lines.append(the_line)
        the_line = the_file.readline()
    
for line in the_lines:
    line_words = line.split(" ")
    for word in line_words:
        the_words[word] = 1

for key in the_words.keys():
    print(f'{key} {the_words[key]}')

