n, k = map(int, input().split())
short_path = n-1
maybe_path = k
maybe_path += ((n-1) % k) + 1
print(maybe_path) if maybe_path < short_path else print(short_path)