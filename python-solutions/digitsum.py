n = int(input())
for _ in range(n):
    num1, num2 = map(int, input().split())
    num1 = num1 - 1
    num1_copy = str(num1)
    num2_copy = str(num2)
    dig_sum_large = 0
    dig_sum_small = 0
    """
    dig_sum = 0
    for i in range(num1, num2+1):
        s = str(i)
        for c in s:
            dig_sum += int(c)
    print(dig_sum)
    """
    multi = 1
    loop_place = 0
    while num2 > 0:
        #print(num2)
        for i in range(1, 10):
            #print(i)
            if (num2 - i) % 10 < num2 % 10:
                if ((num2 % 10) - i) != 0:
                    #print("{} goes in {} times".format(i, (num2//10)+1))
                    #print("adding", multi*i*((num2//10)+1))
                    dig_sum_large += multi*i*((num2//10)+1)
                else:
                    if loop_place == 0:
                        #print("{} goes in {} times".format(i, (num2//10)+1))
                        #print("adding", multi*i)
                        dig_sum_large += multi*i*((num2//10)+1)
                    else:
                        times = (int(num2_copy[-loop_place:])+1) + ((num2//10)*multi)
                        #print("{} goes in {} times".format(i, times))
                        #print("adding", times*i)
                        dig_sum_large += times*i
            else:
                #print("{} goes in {} times".format(i, (num2//10)))
                #print("adding", multi*i*(num2//10))
                dig_sum_large += multi*i*(num2//10)
        num2 = num2//10
        multi *= 10
        loop_place += 1
    #print(dig_sum_large)
    #"""
    #"""
    multi = 1
    loop_place = 0
    while num1 > 0:
        #print(num2)
        for i in range(1, 10):
            #print(i)
            if (num1 - i) % 10 < num1 % 10:
                if ((num1 % 10) - i) != 0:
                    #print("{} goes in {} times".format(i, (num1//10)+1))
                    #print("adding", multi*i*((num1//10)+1))
                    dig_sum_small += multi*i*((num1//10)+1)
                else:
                    if loop_place == 0:
                        #print("{} goes in {} times".format(i, (num1//10)+1))
                        #print("adding", multi*i)
                        dig_sum_small += multi*i*((num1//10)+1)
                    else:
                        times = (int(num1_copy[-loop_place:])+1) + ((num1//10)*multi)
                        #print("{} goes in {} times".format(i, times))
                        #print("adding", times*i)
                        dig_sum_small += times*i
            else:
                #print("{} goes in {} times".format(i, (num1//10)))
                #print("adding", multi*i*(num1//10))
                dig_sum_small += multi*i*(num1//10)
        num1 = num1//10
        multi *= 10
        loop_place += 1
    print(dig_sum_large - dig_sum_small)
    #"""
