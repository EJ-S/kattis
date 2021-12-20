def main():
    n, e = map(int, input().split())
    e = str(2**e)
    count = 0
    for i in range(n+1):
        if str(i).find(e) != -1:
            count += 1
    print(count)




if __name__ == '__main__':
    main()
