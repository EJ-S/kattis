import math

while True:
    try:
        n = int(input())
    except:
        exit(0)

    sum = 1
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            if i == n/i:
                sum += i
            else:
                sum += (i + n/i)
    
    if sum == n:
        print(n, "perfect")
    elif abs(n-sum) <= 2:
        print(n, "almost perfect")
    else:
        print(n, "not perfect")
    
