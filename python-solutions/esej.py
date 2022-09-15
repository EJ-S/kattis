import random
import string

output = set()
a, b = map(int, input().split())
size = max(a, (b//2) + 1)

while len(output) < size:
    test = ''.join(random.choice(string.ascii_lowercase) for _ in range(14))
    if test not in output:
        output.add(test)

print(*output)
