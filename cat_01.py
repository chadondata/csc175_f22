import sys

def main(file_name):
    f = open(file_name, "rt")
    print(f.read())

if __name__ == '__main__':
    n = len(sys.argv)
    file_name = "cat_text.txt"
    if n > 1:
        file_name = sys.argv[1]
    
    main(file_name)
