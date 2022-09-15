n = int(input())
#for _ in range(n):
#    print(ans[input()])
ans = [0] * 15
ans[0] = 1
ans[1] = 0
ans[2] = 6
for i in range(3, 15):
    ans[i] = (ans[i-1]*i + 24*ans[i-2]*i + 36*ans[i-3]*i - 24*ans[i-2] - 72*ans[i-3])*(i - 1)/ (i * i)
for _ in range(n):
    print(int(ans[int(input())]))
