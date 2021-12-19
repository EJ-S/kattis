def remove_smallest(price_list):
    try:
        return price_list[0] + price_list[1]
    except IndexError:
        return price_list[0]


def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort()
    cost = 0
    while len(prices) > 3:
        sub_list = [prices.pop(-1), prices.pop(-1), prices.pop(-1)]
        cost += remove_smallest(sub_list)
    prices.reverse()
    cost += remove_smallest(prices)
    print(cost)


if __name__ == "__main__":
    main()
