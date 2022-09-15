n, t = map(int, input().split())
times = [0] * n
a, b, c, times[0] = map(int, input().split())
for i in range(1, n):
    times[i] = (a*times[i-1] + b)%c + 1
times.sort()
total_time, penalty, num_solved = 0, 0, 0
for time in times:
    total_time += time
    if total_time >= t:
        break
    num_solved += 1
    penalty += total_time

print(num_solved, penalty%1000000007)
