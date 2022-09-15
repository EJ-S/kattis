n = int(input())
words = []
for _ in range(n):
    words.append(input()[::-1])

words.sort()
ptr1 = 0
ptr2 = 1
power = 0
while ptr2 != len(words):
    len1 = min(len(words[ptr2]), len(words[ptr1]))
    current_power = 0
    for i in range(len1):
        #print(words[ptr1][i], words[ptr2][i])
        if words[ptr1][i] == words[ptr2][i]:
                current_power += 1
        else:
            break
    if current_power == len1:
        current_power = 0
    ptr2 += 1
    ptr1 += 1
    power = max(power, current_power)

print(power)
