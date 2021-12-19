def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n, m = map(int, input().split())
        data_set = list(map(int, input().split()))
        found = 0
        weights = []
        current = 0
        index = 0
        while index < n:
            num = data_set[index]
            if num < m and found == 0:
                current = 0
                index += 1
                continue
            if num < m and found == 1:
                weights.append(current)
                current = 0
                found = 0
                index += 1
                continue
            if num == m and found == 0:
                found += 1
                m_loc = index + 1
                current += num
                index += 1
                continue
            if num == m and found == 1:
                found = 0
                weights.append(current)
                current = 0
                index = m_loc
                continue
            current += num
            index += 1
        if found == 1:
            weights.append(current)
        print(max(weights))


if __name__ == '__main__':
    main()
