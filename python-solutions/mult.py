def main():
    n = int(input())
    start = int(input())
    i = 1
    while i < n:    
        num = int(input())
        if num % start == 0:
            print(num)
            start = int(input())
            i += 1
        i += 1


if __name__ == "__main__":
    main()
