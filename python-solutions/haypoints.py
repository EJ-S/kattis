def main():
    m, n = map(int, input().split())
    hay_value = dict()
    for _ in range(m):
        k, v = input().split()
        hay_value.update({k : int(v)})

    for __ in range(n):
        descript = []
        cost = 0
        while True:
            line = input()
            if line == ".":
                break
            for w in line.split():
                descript.append(w)
        for word in descript:
            cost += hay_value.get(word, 0)
        print(cost)


if __name__ == "__main__":
    main()
