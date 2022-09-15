import itertools

case = 1
while True:
    try:
        n = int(input())
    except:
        break
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    possible = itertools.combinations(nums, 2)
    possible_sums = []
    for combin in possible:
        possible_sums.append(combin[0] + combin[1])
    print("Case {}:".format(case))
    test = int(input())
    for _ in range(test):
        closest = 0
        closestabs = 100000000000
        t = int(input())
        for s in possible_sums:
            if abs(t - s) < closestabs:
                closestabs = abs(t-s)
                closest = s
        print("Closest sum to {} is {}.".format(t, closest))
    case += 1
