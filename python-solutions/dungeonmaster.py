def bfs(dun, root, goal):
    q = []
    q.append(root)
    dun[root[0]][root[1]][root[2]] = "#"
    depths = 0
    first_in_next_layer = q[0]
    while len(q) != 0:
        v = q.pop(0)
        #print("LAYER", depths)
        if v == first_in_next_layer:
            depths += 1
            first_in_next_layer = 0
        if v == goal:
            return depths
        for i, nei in enumerate(neigbours(dun, v)):
            if first_in_next_layer == 0 and i == 0:
                first_in_next_layer = nei
            dun[nei[0]][nei[1]][nei[2]] = "#"
            q.append(nei)
    return -1


def neigbours(dun, node):
    neis = []
    if node[0] != 0:
        if dun[node[0]-1][node[1]][node[2]] != "#":
            neis.append([node[0]-1, node[1], node[2]])
    if node[0] != len(dun) - 1:
        if dun[node[0]+1][node[1]][node[2]] != "#":
            neis.append([node[0]+1, node[1], node[2]])
    if node[1] != 0:
        if dun[node[0]][node[1]-1][node[2]] != "#":
            neis.append([node[0], node[1]-1, node[2]])
    if node[1] != len(dun[0]) - 1:
        if dun[node[0]][node[1]+1][node[2]] != "#":
            neis.append([node[0], node[1]+1, node[2]])
    if node[2] != 0:
        if dun[node[0]][node[1]][node[2]-1] != "#":
            neis.append([node[0], node[1], node[2]-1])
    if node[2] != len(dun[0][0]) - 1:
        if dun[node[0]][node[1]][node[2]+1] != "#":
            neis.append([node[0], node[1], node[2]+1])
    return neis


while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    dungeon = []
    start = []
    end = []
    for _ in range(l):
        layer = []
        for __ in range(r):
            row = input()
            if row.find("S") > -1:
                start = [_,__,row.find("S")]
            if row.find("E") > -1:
                end = [_,__,row.find("E")]
            layer.append(list(row))
        dungeon.append(layer)
        input()
    
    ans = bfs(dungeon, start, end)
    print("Escaped in {} minute(s).".format(ans-1)) if ans > 0 else print("Trapped!")
