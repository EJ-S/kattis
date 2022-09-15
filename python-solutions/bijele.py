pieces_list = [1, 1, 2, 2, 2, 8]
pieces_enter = list(map(int, input().split()))
for piece1, piece2 in zip(pieces_list, pieces_enter):
    print(piece1 - piece2, end=" ")
print("")
