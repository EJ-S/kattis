n = int(input())
coins = list(map(int, input().split()))
temp = 0
lost = 0
value = 1
M = 10**9 + 7
for coin in coins:
    temp = temp >> 1
    if coin % 2 != 0 and temp == 0:
        lost = (lost + value) % M
    temp += coin
    value = (value << 1) % M
print(lost % M)
