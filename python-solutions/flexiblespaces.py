def main():
    w, p = map(int, input().split())
    line = input().split()
    segments = [0]
    for s in line:
        segments.append(int(s))
    segments.append(w)
    widths = {w}
    for i in range(len(segments)):
        for j in range(i+1,len(segments)):
            widths.add(segments[j]-segments[i])
    widths_list = list(widths)
    widths_list = sorted(widths_list)
    print(*widths_list)
            


if __name__ == "__main__":
    main()
