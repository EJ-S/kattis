import sys


def main():
    for line in sys.stdin:
        line = line.split()
        print(abs(int(line[0]) - int(line[1])))


if __name__ == '__main__':
    main()
