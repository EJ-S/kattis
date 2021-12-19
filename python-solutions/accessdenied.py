import logging


def get_place(string, length, old_time):
    possible_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHHIJKLMNOPQRSTUVWXYZ0123456789'
    len_correct = len(string)
    for char in possible_char:
        string += char
        while len(string) < length:
            string += 'a'
        print(string, flush=True)
        line = input().split()
        result = line[1]
        if result == 'GRANTED':
            return string, 0, True
        time = int(line[2][1:])
        if time == old_time + 9:
            string = string[:len_correct+1]
            return string, time, False
        elif time == old_time + 18:
            string = string[:len_correct+2]
            return string, time, False
        else:
            string = string[:len_correct]


def main():
    logging.basicConfig(level=logging.DEBUG)
    pass_guess = ''
    pass_len = 1
    cont = True
    for i in range(1, 21, 1):
        pass_guess += 'a'
        print(pass_guess, flush=True)
        line = input().split()
        result = line[1]
        if result == 'GRANTED':
            cont = False
            break
        time = int(line[2][1:])
        if time > 5:
            pass_len = i
            break
    pass_guess = ''
    time = 14
    if cont:
        for i in range(pass_len):
            pass_guess, time, result = get_place(pass_guess, pass_len, time)
            if result:
                break


if __name__ == '__main__':
    main()
