n = int(input())

for _ in range(n):
    day, month = input().split()
    day = int(day)
    if month == "Jan":
        if day < 21:
            print("Capricorn")
        else:
            print("Aquarius")
        continue
    if month == "Feb":
        if day < 20:
            print("Aquarius")
        else:
            print("Pisces")
        continue
    if month == "Mar":
        if day < 21:
            print("Pisces")
        else:
            print("Aries")
        continue
    if month == "Apr":
        if day < 21:
            print("Aries")
        else:
            print("Taurus")
        continue
    if month == "May":
        if day < 21:
            print("Taurus")
        else:
            print("Gemini")
        continue
    if month == "Jun":
        if day < 22:
            print("Gemini")
        else:
            print("Cancer")
        continue
    if month == "Jul":
        if day < 23:
            print("Cancer")
        else:
            print("Leo")
        continue
    if month == "Aug":
        if day < 23:
            print("Leo")
        else:
            print("Virgo")
        continue
    if month == "Sep":
        if day < 22:
            print("Virgo")
        else:
            print("Libra")
        continue
    if month == "Oct":
        if day < 23:
            print("Libra")
        else:
            print("Scorpio")
        continue
    if month == "Nov":
        if day < 23:
            print("Scorpio")
        else:
            print("Sagittarius")
        continue
    if month == "Dec":
        if day < 22:
            print("Sagittarius")
        else:
            print("Capricorn")
        continue
