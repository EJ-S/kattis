def main():
    n, c = map(int, input().split())
    values = list(map(int,input().split()))
    values_set = list(set(values))
    values_count = []
    for value in values_set:
        values_count.append(values.count(value))
    while len(values_count) != 0:
        max = 0
        max_i = 0
        for i, v in enumerate(values_count):
            if v > max:
                max_i = i
                max = v
        for j in range(max):
            print(values_set[max_i],end=" ")
        values_set.pop(max_i)
        values_count.pop(max_i)
        


if __name__ == '__main__':
    main()
