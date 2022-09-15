code = input()
from_last = 3
count = 0
for c in code:
    if c.upper() == c:
        count += 3 - (from_last % 4)
        from_last = 0
    else:
        from_last += 1
print(count)

