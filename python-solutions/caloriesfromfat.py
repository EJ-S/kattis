def main():
    isLine = False
    fat_cal = 0
    total_cal = 0
    while(True):
        percent = 100
        line_cal = 0
        line_fat_cal = 0
        fat_percent = 0
        line = input().split()
        if line[0] == "-" and not isLine:
            break
        if line[0] == "-":
            percent = int(((fat_cal/total_cal) * 100) + 0.5)
            print("{}%".format(percent))
            fat_cal = 0
            total_cal = 0
            isLine = False
            continue
        isLine = True
        for i, amount in enumerate(line):
            if amount[-1] == '%':
                if i == 0:
                    fat_percent = int(amount[:-1])
                percent -= int(amount[:-1])
            if amount[-1] == 'C':
                if i == 0:
                    line_fat_cal += int(amount[:-1])
                line_cal += int(amount[:-1])
            if amount[-1] == "g":
                if i == 0:
                    line_fat_cal += 9 * int(amount[:-1])
                    line_cal += 9 * int(amount[:-1])
                elif i == 4:
                    line_cal += 7 * int(amount[:-1])
                else:
                    line_cal += 4 * int(amount[:-1])
        line_cal = (line_cal/percent) * 100
        if fat_percent > 0:
            line_fat_cal += (line_cal/100) * fat_percent
        total_cal += line_cal
        fat_cal += line_fat_cal


if __name__ == "__main__":
    main()
