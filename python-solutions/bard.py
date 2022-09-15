n = int(input())
e = int(input())
villagers = [ set() for i in range(n+1)]
songs = set()
for eve in range(e):
    present = list(map(int, input().split()))
    present = present[1:]
    present.sort()
    if present[0] == 1:
        #print("NEW SONG for", present)
        songs.add(eve)
        for v in present:
            villagers[v].add(eve)
         #   print(villagers)
    else:
        #print("BARD NOT HERE")
        all_songs_known = set()
        for v in present:
            all_songs_known = all_songs_known.union(villagers[v])
        for v in present:
            villagers[v] = villagers[v].union(all_songs_known)
    #print(villagers)
for i, v in enumerate(villagers[1:]):
    if v == songs:
        print(i+1)
