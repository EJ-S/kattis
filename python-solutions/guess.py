def guess(low, up):
    choose = (up+low)//2
    print(choose, flush=True)
    ans = input()
    if ans == 'lower':
        guess(low, choose)
    elif ans == 'higher':
        guess(choose, up)
    elif ans == 'correct':
        return True


def main():
    guess(0, 1001)


if __name__ == '__main__':
    main()
