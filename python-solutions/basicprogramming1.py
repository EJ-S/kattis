def one():
    print(7)


def two(a):
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] == a[1]:
        print("Equal")
    else:
        print("Smaller")


def three(a):
    a.sort()
    print(a[1])


def four(a):
    print(sum(a))


def five(a):
    tot = 0
    for v in a:
        if v % 2 == 0:
            tot += v
    print(tot)


def six(a):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    mod_list = [v%26 for v in a]
    for c in mod_list:
        print(letters[c], end='')

    
def seven(a, n):
    visited = [False]*n
    index = 0
    visited[0] = True
    while True:
        index = a[index]
        if index >= n:
            print("Out")
            break
        elif index == n-1:
            print("Done")
            break
        else:
            if visited[index]:
                print('Cyclic')
                break
            else:
                visited[index] = True




def main():
    n, t = map(int,input().split())
    a = list(map(int,input().split()))
    if t == 1:
        one()
    elif t == 2:
        two(a)
    elif t == 3:
        three(a[0:3])
    elif t == 4:
        four(a)
    elif t == 5:
        five(a)
    elif t ==  6:
        six(a)
    else:
        seven(a, n)


if __name__ == '__main__':
    main()