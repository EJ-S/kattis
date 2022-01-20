def main():
    n = int(input())
    for _ in range(n):
        line = input().split()
        if line[0] == "Simon" and line[1] == "says":
            print(*line[2:])


if __name__ == "__main__":
    main()