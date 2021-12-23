def main():
    n = int(input())
    biggest_power = 0
    while True:
        if 2**(biggest_power+1) > n:
            break
        biggest_power += 1
    output = ''
    for i in range(biggest_power+1):
        output += str(2**i) + ' '
    print(biggest_power+1)
    print(output[0:-1])

if __name__ == '__main__':
    main()