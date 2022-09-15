from math import sqrt

n = int(input())
most_n = n
ans = []
count = 0
count_ans = 0
while True:
    if n % 2 != 0:
        break
    n = n/2
    count += 1
    ans.append(2)
    count_ans = 2
max_count = count
for i in range(3, int(sqrt(most_n))+1, 2):
    count = 0
    while True:
        if n % i != 0:
            break
        count += 1
        n = n/i
        ans.append(i)
    if count > max_count:
        count = max_count
        count_ans = i

if count_ans == 0:
    count_ans = most_n

print(count_ans)
