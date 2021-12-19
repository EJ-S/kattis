def main():
    x, y = map(int, input().split())
    if y % 2 == 0:
        print('possible')
    else:
        print('impossible')


if __name__ == '__main__':
    main()
