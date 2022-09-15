n, t = map(int, input().split())
num_solved = 0
time = 0
tasks = list(map(int, input().split()))
for task in tasks:
    time += task
    if time > t:
        break
    else:
        num_solved += 1
print(num_solved)
