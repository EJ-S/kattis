def calc(l):
    v = 0
    for num in l:
        v ^= num
    return v
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for num in nums:
    print("XOR FOR {}:".format(num), calc(range(1,num+1)), list(range(1,num+1)))
"""
t = int(input())
for _ in range(t):
    m = int(input())

    if m == 1:
        print("1\n1")
    elif m == 2:
        print("1\n2")
    else:
        if m % 4 == 0:
            solution = list(range(1,m+1))
        elif m % 4 == 1:
            solution = list(range(1,m-1))
            solution.append(m)
        elif m % 4 == 2:
            solution = list(range(2,m+1))
        else:
            solution = list(range(1,m))
        print(len(solution))
        print(*solution)
