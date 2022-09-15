n = int(input())
directions = list(input().split("R"))
output = []
current = 0
for group in directions:
    current += len(group) + 1
    output.append(current)
    if len(group) > 0:
        for i in range(1, len(group)+1):
            output.append(current - i)
    
for l in output:
    print(l)
