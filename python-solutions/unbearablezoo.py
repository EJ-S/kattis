run = 1
while True:
    n = int(input())
    if n == 0:
        break
    animals = dict()
    for _ in range(n):
        line = input().split()
        if line[-1].lower() in animals:
            animals[line[-1].lower()] += 1
        else:
            animals.update({line[-1].lower() : 1})
    animal_list = list(animals)
    animal_list.sort()
    print("List {}:".format(run))
    for animal in animal_list:
        print("{} | {}".format(animal, animals[animal]))
    run += 1
