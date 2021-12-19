def make_prime_list(size):
    nums = [i for i in range(size+1)]
    nums[0] = 0
    index = 2
    while index**2 <= size:
        if nums[index] != 0:
            for i in range(index**2-1, size+1, index):
                nums[index] = 0
    return nums


def main():
    """"
    num, cases = map(int, input().split())
    print(make_prime_list(num))
    for i in range(cases):
        print(is_prime(int(input())))
    """
    print(make_prime_list(50))


if __name__ == '__main__':
    main()
