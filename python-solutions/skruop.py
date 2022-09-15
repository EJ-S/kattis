n = int(input())
num = 7
for _ in range(n):
    ins = input()
    if ins == "Skru op!":
        num += 1
        num = min(num, 10)
    else:
        num -= 1
        num = max(0, num)
print(num)
