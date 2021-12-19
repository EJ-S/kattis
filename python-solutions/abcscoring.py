def main():
    nums = sorted(map(int, input().split()))
    abc = input()
    loc_a = abc.index('A')
    loc_b = abc.index('B')
    loc_c = abc.index('C')
    out_nums = [0, 0, 0]
    out_nums[loc_a] = nums[0]
    out_nums[loc_b] = nums[1]
    out_nums[loc_c] = nums[2]
    output = ''
    for i in out_nums:
        output += str(i) + ' '
    print(output)


if __name__ == '__main__':
    main()
