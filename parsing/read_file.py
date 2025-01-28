import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        retVal = func(*args, **kwargs)
        end = time.time()
        print(f"Function took {end-start} seconds.")
        return retVal
    return wrapper

def readlines(filename: str):
    # open the file in read mode
    with open(filename, 'r') as f:
        for line in f:
            yield line
    return ""

@timer
def parse(filename: str) -> None:
    length = 0
    for line in readlines(filename):
        length += len(line)
    print(length)

@timer
def parseTwo(filename: str) -> None:
    with open(filename, "r") as f:
        lines = f.readlines()
        length = 0
        for line in lines:
            length += len(line)
        print(length)

def main():
    filename: str = "apache_logs.txt"
    parse(filename)
    parseTwo(filename)

    with open(filename, 'r') as f:
        lines = f.readlines()

    lines = lines*50
    with open("logs.txt", 'w') as f:
        f.writelines(lines)

if __name__ == "__main__":
    main()