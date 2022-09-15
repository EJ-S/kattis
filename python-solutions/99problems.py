num = input()
if int(num) < 100:
    print(99)
    exit(0)

addOnes = 9 - int(num[-1:])
addTwos = 9 - int(num[-2:-1])

num = int(num)
numFinal = num + addOnes + addTwos*10

numSmall = numFinal - 100

print(numFinal) if (numFinal - num) <= (num - numSmall) else print(numSmall)
