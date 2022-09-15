n, m = map(int, input().split())
groups = tuple(map(int, input().split()))
ptr = 0
sat = 0
num_sat = 0
while ptr != m:
    if sat + groups[ptr] <= n:
        sat += groups[ptr]
        num_sat += 1
    ptr += 1

print(m-num_sat)
