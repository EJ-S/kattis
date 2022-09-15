n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for i in range(n-1,-1,-1):
    print(nums[i])
