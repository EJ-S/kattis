def main():
    maxi = 11
    mini = 0
    while True:
        num = int(input())
        if num == 0:
            break
        resp = input()
        if resp == 'too high' and num < maxi:
            maxi = num
        if resp == 'too low' and num > mini:
            mini = num
        if resp == 'right on':
            if mini < num < maxi:
                print('Stan may be honest')
            else:
                print('Stan is dishonest')
            maxi = 11
            mini = 0

        

if __name__ == '__main__':
    main()