'''
def main():
    m, n = map(int, input().split())
    cluster_sizes = list(map(int, input().split()))
    possible_sizes = {sum(cluster_sizes)}
    for i in range(0, len(cluster_sizes)):
        possible_size = sum(cluster_sizes[0:i]) 
        for j in range(len(cluster_sizes)-1, i-1, -1):
            possible_sizes.add(possible_size)
            possible_size += cluster_sizes[j]
    for _ in range(n):
        if int(input()) in possible_sizes:
            print("Yes")
        else:
            print("No")
    print(possible_sizes)


if __name__ == "__main__":
    main()
'''
m, n = map(int, input().split())
forward_sums = {0}
backward_sums = {0}
col = list(map(int, input().split()))
s = 0
for num in col:
    s += num
    forward_sums.add(s)
max_s = s
s = 0
for i in range(m-1,-1,-1):
    s += col[i]
    backward_sums.add(s)
for _ in range(n):
    found = False
    q = int(input())
    if q > max_s:
        print("No")
        continue
    for s in forward_sums:
        if (q-s) in backward_sums:
            print("Yes")
            found = True
            break
    if not found:
        print("No")
