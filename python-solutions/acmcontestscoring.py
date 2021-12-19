import sys


def main():
    cin = sys.stdin.readlines()
    cin.pop(len(cin)-1)
    score = 0
    time = 0
    ans_list = []
    for line in cin:
        data = line.split()
        if data[2] == 'right':
            ans_list.append(data[1])
            score += 1
            time += int(data[0])
    for line in cin:
        data = line.split()
        if ans_list.count(data[1]) == 1 and data[2] == 'wrong':
            time += 20

    print(score, time)


if __name__ == "__main__":
    main()
