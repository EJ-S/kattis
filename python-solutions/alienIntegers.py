numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n = input()
for num in n:
    try:
        numbers.remove(int(num))
    except:
        continue
if len(numbers) == 0:
    print("Impossible")
    exit(0)
smaller_number = str(numbers[-1])
for i, num in enumerate(numbers):
    if num > int(n[0]):
        smaller_number = str(numbers[i-1])
        break
if smaller_number < n[0]:
    while len(smaller_number) < len(n):
        smaller_number += str(numbers[-1])
else:
    while len(smaller_number) < len(n)-1:
        smaller_number += str(numbers[-1]) 
numbers.reverse()
larger_number = str(numbers[-1])
for i, num in enumerate(numbers):
    if num < int(n[0]):
        larger_number = str(numbers[i-1])
        break
if larger_number > n[0]:
    while len(larger_number) < len(n):
        larger_number += str(numbers[-1])
else:
    if(numbers[-1] == 0 and len(numbers) > 1):
        larger_number += str(numbers[-2])
        while(len(larger_number) < len(n) + 2):
            larger_number += str(numbers[-1])
    else:
        while len(larger_number) < len(n)+1:
            larger_number += str(numbers[-1])   
small_diff = int(n) - int(smaller_number)
large_diff = int(larger_number) - int(n)

if small_diff < large_diff:
    print(int(smaller_number))
elif large_diff < small_diff:
    print(int(larger_number))
else:
    print(int(smaller_number), int(larger_number))
