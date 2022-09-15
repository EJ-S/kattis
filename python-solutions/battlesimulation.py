inp = input()
i = 0
if len(inp) < 3:
    for q in inp:
        if q == "R":
            print("S", end='')
        elif q == "B":
            print("K", end='')
        else:
            print("H",end='')
    exit(0)
while i < len(inp) - 2:
    combo = {"R", "B", "L"}
    for j in range(3):
        if inp[i+j] in combo:
            combo.remove(inp[i+j])
    if len(combo) == 0:
        print("C", end='')
        i += 3
    else:
        if inp[i] == "R":
            print("S", end='')
        elif inp[i] == "B":
            print("K", end='')
        else:
            print("H",end='')
        i += 1
if i < len(inp):
    while i < len(inp):
        if inp[i] == "R":
            print("S", end='')
        elif inp[i] == "B":
            print("K", end='')
        else:
            print("H",end='')
        i += 1
