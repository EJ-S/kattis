deg_per_num = 360/40
while True:
    start, num1, num2, num3 = map(int, input().split())
    if start == 0 and num1 == 0 and num2 == 0 and num3 == 0:
        break
    loc = start
    nums = 80
    nums += (loc - num1)%40
    #print("{} SPACES TO MOVE".format((loc-num1)%40))
    loc = num1
    nums += 40
    nums += (num2-loc)%40
    #print("{} SPACES TO MOVE".format((num2-loc)%40))
    nums += (num2 - num3)%40
    print(int(nums*deg_per_num))
