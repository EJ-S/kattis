import itertools

nums_list = []
for _ in range(9):
    nums_list.append(int(input()))

possibilities = list(itertools.combinations(nums_list, 7))
for possibility in possibilities:
    s = sum(possibility)
    if s == 100:
        for n in possibility:
            print(n)
        exit(0)

