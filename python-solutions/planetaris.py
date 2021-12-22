def main():
    n, a = map(int, input().split())
    other_ships = sorted(list(map(int,input().split())))
    count = 0
    while a > 0 and count < n:
        cost = other_ships[count] + 1
        if a - cost < 0:
            break
        a -= cost
        count += 1
    print(count)


if __name__ == '__main__':
    main()