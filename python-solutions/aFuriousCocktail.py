n, t = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))

print("YES") if (max(times) / t) > (n-1) else print("NO")
