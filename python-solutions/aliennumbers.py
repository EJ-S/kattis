import sys
import math


def source_to_numbers(num, source):
    out_num = []
    for i, v in enumerate(num):
        out_num.append(source.find(v))
    return out_num


def num_to_decimal(num, source_base):
    total = 0
    for i, v in enumerate(num):
        total += math.pow(source_base, len(num)-1-i)*v
    return int(total)


def decimal_to_num(num, target_base):
    total = []
    while num != 0:
        total.insert(0, num % target_base)
        num = num // target_base
    return total


def num_to_target(num, target):
    out_num = ''
    for i in num:
        out_num += str(target[i])
    return out_num


def find_target(num, source, target):
    source_base = len(source)
    target_base = len(target)
    as_numbers = source_to_numbers(num, source)
    num = num_to_decimal(as_numbers, source_base)
    num = decimal_to_num(num, target_base)
    num = num_to_target(num, target)
    return num


def main():
    cin = sys.stdin.readlines()
    for i, line in enumerate(cin[1:]):
        line = line.split()
        out = find_target(line[0], line[1], line[2])
        print("Case #{}: {}".format(i+1, out))


if __name__ == '__main__':
    main()
