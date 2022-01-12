def main():
    N = int(input())
    list_of_temp_sets = []
    room_ranges = []
    k = {0,1,2}
    for i in range(N):
        L, C = map(int, input().split())
        temp_set = []
        for j in range(L, C+1):
            temp_set.append(j)
        list_of_temp_sets.append(temp_set)
    list_of_temp_sets.sort(key = lambda x: x[0])
    room_ranges.append(set(list_of_temp_sets[0]))
    for k in range(N):
        found = False
        for j, s in enumerate(room_ranges):
            if len(set(list_of_temp_sets[k]).intersection(s)) != 0:
                room_ranges[j] = set(list_of_temp_sets[k]).intersection(s)
                found = True
        if not found:
            room_ranges.append(set(list_of_temp_sets[k]))
    print(len(room_ranges))


if __name__ == "__main__":
    main()
