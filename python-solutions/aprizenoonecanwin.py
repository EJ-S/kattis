import sys


def main():
    cin = sys.stdin.readlines()
    thresh = int(cin[0].split()[1])
    num = int(cin[0].split()[0])
    prices = sorted(map(int, cin[1].split()))
    if num == 1:
        return 1
    else:
        for i in range(num-1):
            if int(prices[i]) + int(prices[i+1]) > thresh:
                return i+1
        return num


if __name__ == '__main__':
    print(main())
