def get_happy(l):
    happy = 0
    for i, num in enumerate(l):
        happy += ((i+1) * num)
    return happy

n = int(input())
a = list(map(int,input().split()))
running_sum = 0
min_i = -1
min_sum = 0
zero_loc = 0
for i, num in enumerate(a):
    running_sum += num
    if running_sum < min_sum:
        min_sum = running_sum
        min_i = i
    if num == 0:
        zero_loc = i
a.remove(0)
#print(min_i, zero_loc)
if min_i > zero_loc:
    a.insert(min_i, 0)
else:
    a.insert(min_i+1, 0)
#print(a)
print(get_happy(a))
