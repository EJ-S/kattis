import sys


def main():
    cin = sys.stdin.readlines()
    out = ''
    for i in range(int(cin[0])+1):
        if i % 2 == 1:
            out += cin[i]
    print(out)


if __name__ == "__main__":
    main()
