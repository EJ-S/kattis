from math import sqrt

n = int(input())
factors = []
while n % 2 == 0:
    n = n//2
    factors.append(2)

for i in range(3, int(sqrt(n))+1,2):
    while n % i == 0:
        n = n//i
        factors.append(i)

if n > 2:
    factors.append(2)

print(len(factors))
