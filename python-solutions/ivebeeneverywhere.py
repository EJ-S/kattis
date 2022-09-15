T = int(input())
for _ in range(T):
    places = set()
    n = int(input())
    for __ in range(n):
        places.add(input())
    print(len(places))
