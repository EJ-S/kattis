def len_larger(loc, ready, value, test_case):
    if ready[loc]:
        return value[loc]
    best = [1]
    for i in range(loc,len(test_case)):
        if test_case[i] > test_case[loc]:
            best.append(len_larger(i,ready,value,test_case)+1)
    best = (max(best))
    value[loc] = best
    ready[loc] = True
    return best
            
    

def main():
    
    while True:
        output = ''
        test_case = list(map(int, input().split()))
        n = test_case.pop(0)
        if test_case == []:
            break
        ready = [False]*n
        value = [1]*n
        ready[n-1] = True
        for i in range(n):
            len_larger(i,ready,value,test_case)
        max_len = max(value)
        output = str(max_len) + ' '
        start = 0
        min_val = 0
        while max_len > 0:
            indexes = []
            vals = []
            for i in range(start,len(value)):
                if value[i] == max_len and test_case[i] > min_val:
                    indexes.append(i)
                    vals.append(test_case[i])
            min_val = min(vals)
            start = indexes[vals.index(min_val)]
            output += str(min_val) + ' '
            max_len -= 1
        print(output)


if __name__ == '__main__':
    main()
