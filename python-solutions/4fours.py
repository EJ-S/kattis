import itertools


def main():
    operators = ('+', '-', '*', '//', '+', '-', '*', '//', '+', '-', '*', '//')
    permutations = tuple(itertools.permutations(operators, 3))
    solution_dict = {}
    for perm in permutations:
        eq = '4 ' + perm[0] + ' 4 ' + perm[1] + ' 4 ' + perm[2] + ' 4'
        ans = eval(eq)
        eq = eq.replace('//', '/')
        solution_dict.update({ans: eq})
    m = int(input())
    for i in range(m):
        n = int(input())
        try:
            eq = solution_dict.__getitem__(n)
            print(eq, '=', n)
        except KeyError:
            print('no solution')


if __name__ == '__main__':
    main()
