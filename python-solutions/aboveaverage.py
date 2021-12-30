def main():
    c = int(input())
    for i in range(c):
        line = list(map(int, input().split()))
        n = line[0]
        grades = line[1:]
        grades_sum = sum(grades)
        avg = grades_sum/n
        count = 0
        for grade in grades:
            if grade > avg:
                count += 1
        print("{:.3f}%".format((count/n)*100))

    
if __name__ == '__main__':
    main()