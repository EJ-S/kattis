def main():
    N, M, K = map(int, input().split())
    rows = []
    cols = [[0] * N for j in range(M)]
    for _ in range(N):
        rows.append(input())
    for k, row in enumerate(rows):
        for i, c in enumerate(row):
            cols[i][k] = c
    for i in range(M):
        cols[i] = set(cols[i])
    colors = [cols[0]]
    for i in range(M):
        found = False
        for j, s in enumerate(colors):
            if len(s.intersection(cols[i])) != 0:
                colors[j] = colors[j].union(cols[i])
                found = True
        if not found:
            colors.append(cols[i])
    print(len(colors))



if __name__ == "__main__":
    main()
