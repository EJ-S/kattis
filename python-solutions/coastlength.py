def bfs(g, s):
    q = []
    q.append(s)
    coastline = 0
    while len(q) != 0:
        node = q.pop(0)
        if node[0] > 0:
            if g[node[0]-1][node[1]] == "0":
                q.append((node[0]-1, node[1]))
                g[node[0]-1][node[1]] = "2"
            if g[node[0]-1][node[1]] == "1":
                coastline += 1
        if node[0] < len(g)-1:
            if g[node[0]+1][node[1]] == "0":
                q.append((node[0]+1, node[1]))
                g[node[0]+1][node[1]] = "2"
            elif g[node[0]+1][node[1]] == "1":
                coastline += 1
        if node[1] > 0:
            if g[node[0]][node[1]-1] == "0":
                g[node[0]][node[1]-1] = "2"
                q.append((node[0], node[1]-1))
            elif g[node[0]][node[1]-1] == "1":
                coastline += 1
        if node[1] < len(g[0])-1:
            if g[node[0]][node[1]+1] == "0":
                g[node[0]][node[1]+1] = "2"
                q.append((node[0], node[1]+1))
            elif g[node[0]][node[1]+1] == "1":
                coastline += 1
    return coastline
         
         
n, m = map(int, input().split())

map_list = []
[map_list.append(input()) for _ in range(n)]

map_list.insert(0, "0"*m)
map_list.append("0"*m)

for i, line in enumerate(map_list):
    line = "0" + line + "0"
    map_list[i] = list(line)

print(bfs(map_list, (0,0)))
