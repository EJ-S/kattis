import sys


def make_row(bricks, width):
    length = 0
    while len(bricks) != 0 and length + int(bricks[0]) <= width:
        length += int(bricks.pop(0))
    if length == width:
        return True, bricks
    return False, bricks


def main():
    cin = sys.stdin.readlines()
    info = cin[0].split()
    width = int(info[1])
    height = int(info[0])
    bricks = cin[1].split()
    flag = True
    for i in range(height):
        flag, bricks = make_row(bricks, width)
        if not flag:
            break
    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
