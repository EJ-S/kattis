def find_length(pos, s_list, found):
    possible = []
    for i, el in enumerate(s_list):
        if el < s_list[pos] and i < pos:
            possible.append(i) 
    if len(possible) == 0:
        return 1
    lengths = []
    for p in possible:
        try:
            lengths.append(found[p])
        except:
            lengths.append(find_length(p, s_list, found))

    return max(lengths) + 1


def main():
    s = input()
    s_list = []
    for c in s:
        s_list.append(c)
    lengths = []
    for i in range(len(s_list)):
        lengths.append(find_length(i, s_list, lengths))
    print(26 - max(lengths))


if __name__ == "__main__":
    main()
