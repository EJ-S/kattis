def main():
    T = int(input())
    for i in range(T):
        n = int(input())
        person_list = []
        for j in range(n):
            name, order, f = input().split()
            name = name[:-1]
            person = []
            person.append(name)
            order = order.split("-")
            order.reverse()
            o = ""
            for el in order:
                if el == "lower":
                    o += 'c'
                elif el == "middle":
                    o += 'b'
                elif el == "upper":
                    o += 'a'
            while len(o) < 10:
                o += 'b'
            person.append(o)
            person_list.append(person)
        person_list.sort(key=lambda person: person[0])
        person_list.sort(key=lambda person: person[1])
        for person in person_list:
            print(person[0])
        print("==============================")


if __name__ == "__main__":
    main()
