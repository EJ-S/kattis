import statistics


def op1():
    nums = tuple(map(int, input().split()))
    nums = set(nums)
    for n in nums:
        if 7777-n in nums:
            return "Yes"
    return "No"


def op2():
    nums = tuple(map(int, input().split()))
    set_nums = set(nums)
    if len(set_nums) == len(nums):
        return("Unique")
    return("Contains duplicate")


def op3(l):
    nums = tuple(map(int, input().split()))
    try:
        m = statistics.mode(nums)
    except statistics.StatisticsError:
        return -1
    if nums.count(m) > l/2:
        return m
    return -1


def op4(l):
    nums = sorted(map(int, input().split()))
    if l % 2 == 1:
        return [nums[l//2]]
    return [nums[(l//2) - 1], nums[l//2]]


def op5():
    nums = map(int, input().split())
    return sorted(filter(lambda n: 99 < n < 1000, nums))


def main():
    l, f = map(int, input().split())
    if f == 1:
        print(op1())
    elif f == 2:
        print(op2())
    elif f == 3:
        print(op3(l))
    elif f == 4:
        print(*op4(l))
    else:
        print(*op5())



if __name__ == "__main__":
    main()