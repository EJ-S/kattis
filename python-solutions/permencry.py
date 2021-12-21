def main():
    while True:
        code = list(map(int,input().split()))
        n = code.pop(0)
        if n == 0:
            break
        msg = input()
        m = len(msg) % n
        if m == 0:
            m = n
        for i in range(n-m):
            msg += ' '
        msg = list(msg)
        out_msg = '\''
        while len(msg) > 0:
            for j in code:
                out_msg += msg[j-1]
            msg = msg[n:]
        out_msg += '\''
        out_msg = str(out_msg)
        print(out_msg)


if __name__ == '__main__':
    main()