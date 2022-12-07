# Letter Counter
import string

file_contents = []
letters = {}

def get_filename():
    file_name = input('Enter a file name: ')
    return file_name

def get_sorted_letters(current_letters):
    sorted_letters = {}
    for letter in sorted(current_letters.keys()):
        sorted_letters[letter] = current_letters[letter]
    return sorted_letters

def main():
    with open(get_filename(), encoding='utf8') as the_file:
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

    sorted_letters = get_sorted_letters(letters)
    print("Alphabetic:")
    for letter in sorted_letters.keys():
        print(f'{letter} : {sorted_letters[letter]}')

    print("Percentages:")
    total_letters = 0
    for letter in letters.keys():
        total_letters += letters[letter]
    print(f'Total letters: {total_letters}')

    distributions = {}
    print("Percentages:")
    for letter in sorted_letters.keys():
        print(f'{letter} : {round((letters[letter] * 100) / total_letters)}')
        distributions[letter] = round((letters[letter] * 100) / total_letters)

    for letter in distributions.keys():
        print(f'{letter} : {distributions[letter]} : {"*" * distributions[letter]}')

if __name__ == '__main__':
    main()