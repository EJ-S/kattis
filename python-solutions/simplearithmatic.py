from decimal import *

def main():
    a, b, c = map(Decimal, input().split())
    print('{:.10f}'.format(a*b/c))


if __name__ == '__main__':
    main()
