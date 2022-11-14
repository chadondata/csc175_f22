import sys

def main(file_name):
    f = open(file_name, "rt")
    contents = f.read()
    print(contents)

if __name__ == '__main__':
    n = len(sys.argv)
    if n > 1:
        file_name = sys.argv[1]
        main(file_name)
    else:
        print("Missing argument: file name")
        print("Usage:")
        print("python cat.py <file_name>")
        