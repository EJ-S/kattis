def main():
    while True:
        n = int(input())
        if n == 0:
            break
        words = input().replace(' ','')
        words = words.upper()
        output = [' ']*len(words)
        count = 0
        for i in range(min(n,len(words))):
            place = i
            while place < len(words):
                output[place] = words[count]
                count += 1
                place += n
        output_str = ''
        for c in output:
            output_str += c

        print(output_str)


if __name__ == '__main__':
    main()